import pandas as pd
import processing.constants as constants
from processing.airport import extract_us_airport, data_prepare
from processing.airline import prepare_airline_delay_data
from plot import plot_count, plot_delay

ann_x = [2011, 2017, 2014, 2018, 2011, 2018, 2018,
             2018, 2008, 2009, 2009, 2013, 2009, 2018,
             2009, 2018, 2015, 2013, 2015, 2017, 2010,
             2010, 2009,
             ]
ann_y = [9.7, 11.8, 1.3, 26.5, 15.7, 7.08, 20.4, 33, 26.5, 22.6, -1, 22, 22.7, 15.4, 21, 16.7, 19.5, 7.2, 7.8, 15,
         14.3, 7.4, 10]


def clean_airport_data():
    """
    This function cleans the original worldwide airport data by removing the NA and outlier data. Then it stores the
    cleaned airport data as a csv file.
    """
    original_airports = pd.read_csv(constants.AIRPORT_DATA_PATH)
    cleaned_us_airports = extract_us_airport(original_airports)
    cleaned_us_airports.to_csv(constants.CLEANED_AIRPORT_DATA_PATH)


def plot_dep_count_by_airport_and_state_yearly():
    """
    This function plots the yearly departure flight count from 2009-2018 for different airports and states
    """
    df_dep_count_list_by_year, df_dep_count_by_state_list_by_year = data_prepare(constants.TARGET_COUNT,
                                                                                 constants.DIRECTION_DEPARTURE,
                                                                                 constants.TIME_YEAR)

    plot_count.plot_count(df_dep_count_list_by_year, df_dep_count_by_state_list_by_year, "ORIGIN_COUNT",
               "US Domestic Airline Departure Count (Origin)")


def plot_arr_count_by_airport_and_state_yearly():
    """
    This function plots the yearly arrival flight count from 2009-2018 for different airports and states
    """
    df_dep_count_list_by_year, df_dep_count_by_state_list_by_year = data_prepare(constants.TARGET_COUNT,
                                                                                 constants.DIRECTION_ARRIVAL,
                                                                                 constants.TIME_YEAR)
    plot_count.plot_count(df_dep_count_list_by_year, df_dep_count_by_state_list_by_year, "DEST_COUNT",
               "US Domestic Airline Arrival Count (DEST)")


def plot_throughpupt_by_apiports_and_state_yearly():
    df_count_list, df_count_by_state_list = data_prepare(constants.TARGET_THROUGHPUT,
                                                         constants.DIRECTION_ARRIVAL,
                                                         constants.TIME_YEAR)
    plot_count.plot_count(df_count_list, df_count_by_state_list, "COUNT", "US Domestic Airline Throughput")


def plot_dep_delay_by_airports_and_state_yearly():
    df_dep_delay_list_by_year, df_dep_delay_by_state_list_by_year = data_prepare(constants.TARGET_DELAY,
                                                                                 constants.DIRECTION_DEPARTURE,
                                                                                 constants.TIME_YEAR)
    plot_delay.plot_delay(df_dep_delay_list_by_year, df_dep_delay_by_state_list_by_year, "DEP_DELAY",
               "US Domestic Airline Departure Delay (Origin)")


def plot_arr_delay_by_airports_and_state_yearly():
    df_arr_delay_list_by_year, df_arr_delay_by_state_list_by_year = data_prepare(constants.TARGET_DELAY,
                                                                                 constants.DIRECTION_ARRIVAL,
                                                                                 constants.TIME_YEAR)
    plot_delay.plot_delay(df_arr_delay_list_by_year, df_arr_delay_by_state_list_by_year, "ARR_DELAY",
               "US Domestic Airline ARR Delay (DEST)")


def plot_dep_delay_by_airports_and_state_monthly():
    df_dep_delay_list_by_month, df_dep_delay_by_state_list_by_month = data_prepare(constants.TARGET_DELAY,
                                                                                   constants.DIRECTION_DEPARTURE,
                                                                                   constants.TIME_MONTH)
    plot_delay.plot_delay(df_dep_delay_list_by_month, df_dep_delay_by_state_list_by_month, "DEP_DELAY",
               "US Domestic Airline Departure Delay (Origin)")


def plot_arr_delay_by_airports_and_state_monthly():
    df_arr_delay_list_by_month, df_arr_delay_by_state_list_by_month = data_prepare(constants.TARGET_DELAY,
                                                                                   constants.DIRECTION_ARRIVAL,
                                                                                   constants.TIME_MONTH)
    plot_delay.plot_delay(df_arr_delay_list_by_month, df_arr_delay_by_state_list_by_month, "ARR_DELAY",
               "US Domestic Airline Arrival Delay (Dest)")


def plot_airline():
    df_total_delay = prepare_airline_delay_data()
    carrier_list = sorted(list(set(df_total_delay['OP_CARRIER'].to_list())))

