import csv
from collections import defaultdict

import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import matplotlib as plt

def StatDelayFrequency(data_files):
    '''Read the csv file then counting delay frequency for each reason.
    data_files: csv file names
    Output: return tuple of percentage.
    '''
    n_carrier_delay = 0
    n_weather_delay = 0
    n_nas_delay = 0
    n_security_delay = 0
    n_late_delay = 0

    n_carrier_500 = 0
    n_weather_500 = 0
    n_nas_500 = 0
    n_security_500 = 0
    n_late_500 = 0
    for name in data_files:
        df_airline = pd.read_csv(name)
        carrier_delay = df_airline['CARRIER_DELAY'].dropna()
        weather_delay = df_airline['WEATHER_DELAY'].dropna()
        nas_delay = df_airline['NAS_DELAY'].dropna()
        security_delay = df_airline['SECURITY_DELAY'].dropna()
        late_delay = df_airline['LATE_AIRCRAFT_DELAY'].dropna()

        n_carrier_delay += len(carrier_delay[0<carrier_delay])
        n_carrier_500 += len(carrier_delay[carrier_delay>500])

        n_weather_delay += len(weather_delay[0<weather_delay])
        n_weather_500 += len(weather_delay[weather_delay>500])
        
        n_nas_delay += len(nas_delay[0<nas_delay])
        n_nas_500 += len(nas_delay[nas_delay>500])
        
        n_security_delay += len(security_delay[0<security_delay])
        n_security_500 += len(security_delay[security_delay>500])
        
        n_late_delay += len(late_delay[0<late_delay])
        n_late_500 += len(late_delay[late_delay>500])
        
    delay_sum = n_carrier_delay + n_weather_delay + n_nas_delay + n_security_delay + n_late_delay
    delay_500 = n_carrier_500 + n_weather_500 + n_nas_500 + n_security_500 + n_late_500
    percent_all = np.array([n_carrier_delay, n_weather_delay, n_nas_delay, n_security_delay, n_late_delay])/delay_sum
    percent_500 = np.array([n_carrier_500, n_weather_500, n_nas_500, n_security_500, n_late_500])/delay_500
    percent_less = np.array([n_carrier_delay, n_weather_delay, n_nas_delay, n_security_delay, n_late_delay]) - np.array([n_carrier_500, n_weather_500, n_nas_500, n_security_500, n_late_500])
    return [percent_all, percent_500, percent_less]
        
def PlotPie(percent_500, percent_less):
    '''Plot the pie by plotly.
    Input: percent 
    '''
    labels = ['CARRIER','WEATHER','NAS','SECURITY','LATE_AIRCRAFT']
    fig = make_subplots(rows=1, cols=2,specs=[[{"type": "domain"}, {"type": "domain"}]],)

    fig.add_trace(go.Pie(labels=labels, values=percent_less, name="<500 mins"),
                  row=1, col=1)
    fig.add_trace(go.Pie(labels=labels, values=percent_500, name=">500 mins"),
                  row=1, col=2)

    fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    fig.update_layout(
        height=600, width=800, title_text="Delay Reasons",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='<500min', x=0.15, y=0.5, font_size=15, showarrow=False),
                     dict(text='>500min', x=0.85, y=0.5, font_size=15, showarrow=False)])
    fig.show()

def PlotPieDemon():
    '''Plot the demon of delay reason distribution.
    '''
    data_files = ['./data/2018.csv']
    [percent_all, percent_500, percent_less] = StatDelayFrequency(data_files)
    PlotPie(percent_500, percent_less)

if __name__ =='__main__':
    root = './'
    data_airport = root+'clean_airports.csv'
    data_files = []
    for i in range(10):
        data_files.append(root+'airline_delay_and_cancellation_data/'+str(2009+i)+'.csv')
        
    [percent_all, percent_500, percent_less] = StatDelayFrequency(data_files)
    
    PlotPie(percent_500, percent_less)
        