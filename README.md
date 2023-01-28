# Flight_Price_Prediction
**The objective of the case study is to analyse the flight bookings data obtained by “Ease My Trip” website and to conduct various statistical hypothesis tests in order to get meaningful information from it. A thorough study of the data will aid in the discovery of valuable insights that will be of enormous value to passengers. Overall, I had to build a model that can precisely predict the ticket price.**

#### Brain Storming
By getting problem of the client, i have some questions in my mind, which are follow

**a)** Does price vary with Airlines?

**b)** How is the price affected when tickets are bought in just 1 or 2 days before departure?

**c)** Does ticket price change based on the departure time and arrival time?

**d)** How the price changes with change in Source and Destination?

**e)** How does the ticket price vary between Economy and Business class?, etc

#### Data is seperated in to two parts:
one for **economy class** tickets and another for **business class** tickets.

**A total of 300261 distinct flight booking options are available. And these are for 50 days, from February 11th to March 31st, 2022.**

#### Initial Preprocessing:
**There was highly noise in the data. So, I have done some cleaning and also drived some relevent featues from the given data**

I drived new featue named class to specify in which class the ticket was booked

I drived new new featute named flight by adding ch_code and num_code of the flight

I drived new feature days left by subtracting the booking date from journey date (Booking date was 10/02/2022)

#### now we have clean data for our model

The various features of the cleaned dataset are explained below:

**1) Airline:** The name of the airline company is stored in the airline column. It is a categorical feature having 6 different airlines.

**2) Flight:** Flight stores information regarding the plane's flight code. It is a categorical feature.

**3) Source City:** City from which the flight takes off. It is a categorical feature having 6 unique cities.

**4) Departure Time:** This is a derived categorical feature obtained created by grouping time periods into bins. It stores information about the departure time and have 6 unique time labels.

**5) Stops:** A categorical feature with 3 distinct values that stores the number of stops between the source and destination cities.

**6) Arrival Time:** This is a derived categorical feature created by grouping time intervals into bins. It has six distinct time labels and keeps information about the arrival time.

**7) Destination City:** City where the flight will land. It is a categorical feature having 6 unique cities.

**8) Class:** A categorical feature that contains information on seat class; it has two distinct values: Business and Economy.

**9) Duration:** A continuous feature that displays the overall amount of time it takes to travel between cities in hours.

**10)Days Left:** This is a derived characteristic that is calculated by subtracting the trip date by the booking date.

**11) Price:** Target variable stores information of the ticket price.

#### EDA
**Q1. Does price vary with Airlines?**

**Ans:** The answer is yes Trujet is the cheapest airline and Vistara is the most expansive one.

**Q2. How is the price affected when tickets are bought in just 1 or 2 days before departure?**

**Ans:** Yes price is affected when tickets are bought in just 1 or 2 days before

**Q3. Does ticket price change based on the departure time and arrival time?**

**Ans: a. departure vs ticket price**

Ticket Price is More for the Flights when the Departure Time is at Night

Ticket Price is almost equal for flights Having Departure time at Early_morning , Morning and Evening

Ticket Price is Low for the Flights Having Departure Time at Late_night

**b. Arrival Time Vs Ticket Price**

Ticket Price is More for the Flights when the Arrival Time is at Evening

Ticket Price is almost equal for flights Having Arrival time is at Morning and Night

Ticket Price is Low for the Flights Having Arrival Time at Late_night as same as Departure Time

**Q4. How the price changes with change in Source and Destination?**

**Ans: a. Source City Vs Ticket Price**

Ticket Price is More for the Flights whose Source City is Kolkata

Ticket Price is almost equal for flights Having Source Cities as Mumbai and chennai , delhi and Bangalore

Ticket Price is Low for the Flights Having Source City as Hydrabad

**b. Destination City Vs Ticket Price**

Ticket Price is More for the Flights whose Destination City is kolkata and Delhi

Ticket Price is almost equal for flights Having Destination Cities as Mumbai and Bangalore

Ticket Price is Low for the Flights Having Destination City as Chennai

**Q5. How does the ticket price vary between Economy and Business class?**

**Ans:** The business class price is higher than economy class

#### Feature Engineering 
After getting all the insights from the data, I had all the knowledge like only one feature has outliers. But we can not replace acctual duration of the travel. So, I went for featuer scaling in place of replacing them. Also, I had to do some preprocessing like encoding. In encoding, I had nominal as well as ordinal data. That's why I used replace function for ordinal data and Onehot encoder and pd.get_dummies for nominal data. 

#### Feature Selection 
I did not want to drop any featuer except flight featue only. As I had less number of features, So if more features was droped, it can be cause for underfitting(undercutting) the model. That's why i did not drop any feature except flight.

#### Model selection and training
After splitting the data for training as well as testing purpose, first I checked r2 of different models without scaling. Then I scaled the data and checked the r2 score of same models. Finally I choose Random Forest for model training. And after training the model, I went for evaluation. Model did not need optimization. 

#### Exportation of model for production
Finally, I exported the model file, scalling model file and json file for deployment. 

#### Web Frame Works (Flask)
I wrote api in flask and tested with the help of **Postman**.

#### GitHub
Lastly, I created a new reposatory and push my code and files to GitHub.


