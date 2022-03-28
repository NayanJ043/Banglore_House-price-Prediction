import json
import pickle
import numpy as np

__area_type = None
__location = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bath,balcony,bhk,area_type):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    try :
        area_index = __data_columns.index(area_type.lower())
    except:
        area_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    if loc_index >= 0 :
        x[loc_index] = 1
    if area_index >= 0 :
        x[area_index] = 1
    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __location
    global __area_type

    with open ("./artifacts/columns.json" , 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[4:244]
        __area_type = __data_columns[244:]

    global __model
    if __model is None:
        with open('./artifacts/banglore_home_price_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __location

def get_area_type():
    return __area_type

def get_data_columns():
    return __data_columns

if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_area_type())
    print(get_estimated_price('1st Phase JP Nagar', 2850 , 2 , 1 ,2,'Carpet Area'))
    print(get_estimated_price('1st Phase JP Nagar', 2850, 2, 1, 2, 'Plot  Area'))
    print(get_estimated_price('Indira Nagar', 1000 , 5 , 2,3 ,'Plot  Area'))