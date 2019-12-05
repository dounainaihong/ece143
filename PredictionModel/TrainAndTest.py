import csv
import os
from collections import defaultdict

import numpy as np
import pandas as pd

import tensorflow as tf
from tensorflow.keras import layers

from ModelClass import *

def EncodeAirline(airline):
    '''Change the classes to one-hot code.'''
    
    airline_set = {'F9':0, 'B6':1, 'EV':2, 'OO':3, 'UA':4, 'AA':5, 'WN':6, 'DL':7, 'HA':8, 'AS':9}
    airline_hotkey = [0]*len(airline_set)
    if airline in airline_set:
        airline_hotkey[airline_set[airline]] += 1
    return airline_hotkey
    
    
def EncodeDelayData(df_airline, airport_info):
    ''''Change the dataframe to array of training set.
    Format: X: [encoded_airline, lat, longtitude, elevation_ft, month-day].
    '''
    
    train_set = []
    test_set = []
    label_train = []
    label_test = []
    N_data = len(df_airline)
    delay_types=['WEATHER_DELAY','CARRIER_DELAY','NAS_DELAY','SECURITY_DELAY','LATE_AIRCRAFT_DELAY']
    airline_set = {'F9':0, 'B6':1, 'EV':2, 'OO':3, 'UA':4, 'AA':5, 'WN':6, 'DL':7, 'HA':8, 'AS':9}
    for k in range(N_data):
        carrier = df_airline['OP_CARRIER'][k]
        if carrier not in airline_set: continue
        date = df_airline['FL_DATE'][k].split('-')
        month = [int(date[1]+date[2])]
        airport_out = df_airline['ORIGIN'][k]
        airport_in = df_airline['DEST'][k]
        airport_out_info = airport_info[airport_out]
        airport_in_info = airport_info[airport_in]
        carrier_hotkey = EncodeAirline(carrier)
        data_row = carrier_hotkey+airport_out_info+airport_in_info+month
        train_set.append(data_row)
        y = int(any(df_airline[delay_type][k]>0 for delay_type in delay_types))
        label_train.append(y)
        
    return (train_set, label_train)
    
def EncodeCancelData(df_airline, airport_info):
    '''Encode the cancellation data to array of training set.
    Format X: [encoded_airline, lat, longtitude, elevation_ft, month-day] 
    '''
    train_set = []
    test_set = []
    label_train = []
    label_test = []
    N_data = len(df_airline)
    delay_types=['WEATHER_DELAY','CARRIER_DELAY','NAS_DELAY','SECURITY_DELAY','LATE_AIRCRAFT_DELAY']
    airline_set = {'F9':0, 'B6':1, 'EV':2, 'OO':3, 'UA':4, 'AA':5, 'WN':6, 'DL':7, 'HA':8, 'AS':9}
    for k in range(N_data):
        carrier = df_airline['OP_CARRIER'][k]
        if carrier not in airline_set: continue
        date = df_airline['FL_DATE'][k].split('-')
        month = [int(date[1]+date[2])]
        airport_out = df_airline['ORIGIN'][k]
        airport_in = df_airline['DEST'][k]
        airport_out_info = airport_info[airport_out]
        airport_in_info = airport_info[airport_in]
        carrier_hotkey = EncodeAirline(carrier)
        data_row = carrier_hotkey+airport_out_info+airport_in_info+month
        if len(data_row)<16: continue
        #print(data_row)
        train_set.append(data_row)
        y = df_airline['CANCELLED'][k]
        label_train.append(y)
        
    return (train_set, label_train)
    
    
def GetAirportInfo():
    '''Get airport info from data.
    '''
    df_airport = pd.read_csv('airports.csv')
    airport_info = defaultdict(list)
    airline_name = {'9E':'Endeavor Air',
                    'AA':'American Airlines', 
                    'AS':'Alaska Airlines',
                    'B6':'JetBlue', 
                    'CO':'Continental Airlines', 
                    'DL':'Delta Air Lines', 
                    'EV':'Atlantic Southeast Airlines', 
                    'F9':'Frontier Airlines', 
                    'FL':'AirTran', 
                    'G4':'Allegiant Air',
                    'HA':'Hawaiian Airlines',
                    'MQ':'Envoy Air', 
                    'NK':'Spirit Airlines', 
                    'NW':'Northwest Airlines', 
                    'OH':'Comair',
                    'OO':'SKYWEST',
                    'UA':'United Airlines',
                    'US':'US Airways', 
                    'VX':'Virgin America', 
                    'WN':'Southwest Airlines',
                    'XE':'ExpressJet', 
                    'YV':'Mesa Airlines',
                    'YX':'Midwest Express', 
                   }

    hasiata = df_airport['iata_code'].notnull()
    for k in range(len(df_airport)):
        if not hasiata[k]: continue 
        iata = df_airport['iata_code'][k]
        elevation = df_airport['elevation_ft'][k] if df_airport['elevation_ft'][k]>0 else 0
        airport_info[iata] = [float(df_airport['latitude_deg'][k]),
                                float(df_airport['longitude_deg'][k]),
                                elevation]
    return airport_info

def ModifyDelayData(data_files):
    '''Read the raw data from data_files and convert them into ml training format.
    '''
    airport_info = GetAirportInfo()
    for file_id in range(len(data_files)):
        print('File Name:', data_files[file_id])
        df_airline = pd.read_csv(data_files[file_id])
        if not os.path.exists('./mldata'):
            os.mkdir('./mldata')
        if not os.path.exists('./mldata/delay'):
            os.mkdir('./mldata/delay')
        mldata_path = './mldata/delay/train_set_%d.csv' %file_id
        data_set, label = EncodeDelayData(df_airline, airport_info)
        pd.DataFrame(data_set).to_csv(mldata_path)
        with open(mldata_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            for k, row in enumerate(data_set):
                csv_writer.writerow(row+[label[k]])
                
def ModifyCancelData(data_files):
    '''Read the raw data from data_files and convert them into ml training format.
    '''
    airport_info = GetAirportInfo()
    for file_id in range(len(data_files)):
        print('File Name:', data_files[file_id])
        df_airline = pd.read_csv(data_airline[file_id])
        if not os.path.exists('./mldata'):
            os.mkdir('./mldata')
        if not os.path.exists('./mldata/cancel'):
            os.mkdir('./mldata/cancel')
        mldata_path = './mldata/cancel/train_set_%d.csv' %file_id
        data_set, label = EncodeCancelData(df_airline, airport_info)
        pd.DataFrame(data_set).to_csv(mldata_path)
        with open(mldata_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile,  delimiter=',')
            for k, row in enumerate(data_set):
                csv_writer.writerow(row+[label[k]])

def TrainDelayModel():
    '''Train delay prediction model.
    '''
    
    # model initialization
    delay_agent = PredictModel(17)
    delay_agent.model.summary()

    # mini-batch training
    for epoch in range(100):
        file_id = epoch%10
        print('Total Epoch=', epoch)
        mldata_path = './mldata/delay/train_set_%d.csv' %file_id
        
        data_set = pd.read_csv(mldata_path, header=None)
        n_data = len(data_set)
        train_set = np.array(data_set.iloc[(n_data//10)*(epoch//10):(n_data//10)*(epoch//10+1),0:17])
        
        label = np.array(data_set.iloc[(n_data//10)*(epoch//10):(n_data//10)*(epoch//10+1),17])
        
        train_set = train_set[~np.isnan(label)]
        label = label[~np.isnan(label)]
        delay_agent.TrainModel(train_set, label, model_id=epoch, sub_epochs=1)
    return delay_agent
    
def TrainCancelModel():
    '''Train cancel prediction model.
    '''
    
    # model initialization
    cancel_agent = PredictModel(17)
    cancel_agent.model.summary()

    # mini-batch training
    for epoch in range(100):
        file_id = epoch%10
        print('Total Epoch=', epoch)
        mldata_path = './mldata/cancel/train_set_%d.csv' %file_id
        
        data_set = pd.read_csv(mldata_path, header=None)
        n_data = len(data_set)
        train_set = np.array(data_set.iloc[(n_data//10)*(epoch//10):(n_data//10)*(epoch//10+1),0:17])
        
        label = np.array(data_set.iloc[(n_data//10)*(epoch//10):(n_data//10)*(epoch//10+1),17])
        
        train_set = train_set[~np.isnan(label)]
        label = label[~np.isnan(label)]
        delay_agent.TrainModel(train_set, label, model_id=epoch, sub_epochs=1)

def TestModel(agent, mode='delay'):
    '''Test the model.
    '''
    
    test_set_path = os.path.join('./mldata',mode,'train_set_9.csv'
    data_set = pd.read_csv(test_set_path, header=None)
    n_data = len(data_set)
    test_set = np.array(data_set.iloc[0:n_data,0:17])
    label = np.array(data_set.iloc[0:n_data,17])
    test_set = test_set[~np.isnan(label)]
    label = label[~np.isnan(label)]
    y_predict = agent.model.predict(test_set)
    accuracy = sum(y_predict==label)/n_data
    return accuracy
    
if __name__=='__main__':
    root = './'
    data_airport = root+'clean_airports.csv'
    data_files = []
    for i in range(10):
        data_files.append(root+'airline_delay_and_cancellation_data/'+str(2009+i)+'.csv')
        
    ModifyDelayData(data_files)
    ModifyCancelData(data_files)
    delay_agent = TrainDelayModel() 
    cancel_agent = TrainCancelModel()
    delay_accuracy = TestModel(delay_agent, mode='delay')
    cancel_accuracy = TestModel(cancel_agent, mode='cancel')
    