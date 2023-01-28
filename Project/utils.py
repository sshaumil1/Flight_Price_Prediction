import numpy as np
import json,pickle,config

class FlightPrice():
    def __init__(self,departure_time,stops,arrival_time,class1,duration,days_left,airline,source_city,destination_city):
        self.departure_time   = departure_time
        self.stops            = stops
        self.arrival_time     = arrival_time
        self.class1           = class1
        self.duration         = duration
        self.days_left        = days_left
        self.airline          = airline
        self.source_city      = source_city
        self.destination_city = destination_city
    def get_models(self):
        with open (config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)
        with open (config.MODEL_PATH, "rb") as f:
            self.model = pickle.load(f)
        with open (config.SCALING_PATH, "rb") as f:
            self.std = pickle.load(f)
    def get_prices(self):
        self.get_models()
        self.cols = self.json_data["columns"]
        test_arr = np.zeros(len(self.cols))
        test_arr[0] = self.json_data["departure_time"][self.departure_time]
        test_arr[1] = self.stops
        test_arr[2] = self.json_data["arrival_time"][self.arrival_time]
        test_arr[3] = self.json_data["class"][self.class1]
        test_arr[4] = self.duration
        test_arr[5] = self.days_left

        airline_index = np.where(self.cols == self.airline)[0]
        test_arr[airline_index] = 1
        source_city_index = np.where(self.cols == self.source_city)[0]
        test_arr[source_city_index] = 1
        dest_city_index = np.where(self.cols == self.destination_city)[0]
        test_arr[dest_city_index] = 1

        scalled_data = self.std.transform([test_arr])
        price = self.model.predict(scalled_data)
        return price

