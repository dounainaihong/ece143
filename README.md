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
 /data: 
 stores all of the data expect for the flights data, which we need to download to here.
 
 /model: 
 
 /plot:
 stores all of the functions we will use to plot graphs directly
     
 / prediction
 
 / processing:
 stores all of the modules we will use to process our data and do the analysis.
 
 
 main.py: provides the up-level interfaces for users to the analysis and visualizations.
 
 
 
 
 ### Run Locally
 ##### data prepare
 * Downloading flights data we have extracted from OST_R from [our online data storage](https://drive.google.com/drive/folders/1Fw1NGhDOesngb_MywLFVDQXJtfUl37CN?usp=sharing), and put all of csv files
 from 2009.csv-2018.csv to the ./data directory.
 * For the other three datasets, we already downloaded them into the ./data/ directory.
 
 ##### data clean
 For the airlines and flights data, we will clean the data in different specific logics parts.
 Here we will clean the airports data by removing all of the useless and NA airports information, 
 
 ```
 # in the linux command line, run the command:
 python processing/clean.py
 ```

 ##### process & visualization
 We build the processing parts into different modules in the processing/. For each specific analysis, it calls different processing modules internally.
 
 To simplify the users' operations, this repo directly provides the most up-level interface for users to do the visualization. 
 
 To show the visualizations, please either setup the jupyter notebook and run the **final.ipynb** or run as the following steps.
 
 1. enter the python3 command line
     ```
        location: current root directory for this project
        run the linux command: python3
        description: enter the python command line and follow the following python commands. 
     ``` 
 2. run the python command lines for different analysis.
     ```
      # import the main modules which provides the up-level interfaces for virsualizations.
      >> import main
      
      # plot the airline route distributions over states
      >> main.plot_airline_routes()
      
      # plot the airline delay history
      >> main.plot_airline_history()
      
      # plot the average yearly arrival delay for airports and states
      >> main.plot_arr_delay_by_airports_and_state_yearly()
     ```
     note: You can run any functions in the main.py here for any visualizations you want.
 