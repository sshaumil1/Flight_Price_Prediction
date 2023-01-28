from flask import Flask, render_template,jsonify,request
import numpy as np
from Project.utils import FlightPrice
import config

app = Flask(__name__)
@app.route("/")
def get_checked():
    return render_template

@app.route("/Flight_Price_Prediction",methods =["GET"])
def get_predicted_price():
    data = request.form
    departure_time = data["departure_time"]
    stops          = int(data["stops"])
    arrival_time   = data["arrival_time"]
    class1         = data["class"]
    duration       = eval(data["duration"])
    days_left      = int(data["days_left"])
    airline        = data["airline"]
    source_city    = "source_city_" + data["source_city"]
    destination_city = "destination_city_" + data["destination_city"]
    obj = FlightPrice(departure_time,stops,arrival_time,class1,duration,days_left,airline,source_city,destination_city)
    price = obj.get_prices()
    return jsonify({"Result": f"The Flight Ticket Price is:: Rs. {np.around(price[0],3)} Only"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = config.PORT_NUMBER)