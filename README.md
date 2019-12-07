## The Analysis of the Flight Delay and Cancellation

### Goal
This project aims at exploring the US flights data over the past 10 years 
(2009-2018) by analyzing and visualizing important features in terms of 
 delay and cancellation. We analyzed this data from different aspects including 
 airlines/airports/states and from different time ranges such as yearly/monthly.
 
 
 ### Data Source
 * Flight data: [OST_R open dataset](https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time)
    * 2009-2018 US Domestic Flights data
    * Including info such as 
    ``` 
   Date, arrival delay, departure delay, departure/arrival airports, airline carriers, etc. 
    ```      
  * WorldWide Airport Data: [OurAirports](https://ourairports.com/data/)
  * Airline code to Airline name: scrapped from Google
   ```
    AA => American Airlines, F9 => Frontier Airlines
   ```
   
  * US states & region data: [Github US states data set](https://github.com/cphalpert/census-regions/blob/master/us%20census%20bureau%20regions%20and%20divisions.csv)
 
 ### Environment Requirements
 * Programming Language
   * Python3.6
  
 * Python Packages required
      * pandas >= 0.25.0
      * plotly >= 4.3.0
      * tensorflow >= 2.0.0
      * keras 2.3.1
      * numpy
      * matlablib
      

 ### File Structure
 
 
 
 ### Run Locally
 ##### data prepare
 * Downloading flights data we have extracted from OST_R from [our online data storage](https://drive.google.com/drive/folders/1Fw1NGhDOesngb_MywLFVDQXJtfUl37CN?usp=sharing), and put all of csv files
 from 2009.csv-2018.csv to the ./data directory.
 * For the other three datasets, we already downloaded them into the ./data/ directory.
 
 ##### data clean
 ```
 
 
 
 ```
 
 ##### process & virsualization
 
 ##### Build Neural Network to Predict Delay/Cancellation
 
 a) Modify the raw data into prediction model features.
 
-> location: prediction/train_test.py

 -> run command: python prediction/train_test.py modify_data

-> description: The files reads in the data from "./data" folder and convert airline, airport location, flight time information to learning features array. The modified data will be saved in "./data/delay" for delay model and "./data/cancel" for cancel model.

b) Train the Machine Learning Models.
 
-> location: prediction/train_test.py

 -> run command: python prediction/train_test.py train

-> description: The files reads in the data from "./data/delay" or "./data/cancel" folders. Then it tuning the prediction model as training. The trained model will be saved into "./model/delay" or "./model/cancel" respectively.

c) Test the prediction models.
 
-> location: prediction/train_test.py

 -> run command: python prediction/train_test.py test

-> description: The files reads in the prediction model from "./model/delay" or "./model/cancel" folders. Then it predicts whether flights will delay according to the flights' information stored in "./data/delay". It is the same as cancel except the file path. The prediction accuracy will be shown once test has been done.
