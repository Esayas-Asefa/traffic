import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

import matplotlib.pyplot as plt
import seaborn as sns


def prep_traffic(df):
    
    column_mapping = {'Distance(mi)': 'distance', 'Temperature(F)': 'temp', 'Wind_Chill(F)': 'wind_chill', 
                  'Humidity(%)': 'humidity', 'Pressure(in)': 'pressure', 'Visibility(mi)': 'visibility', 
                  'Wind_Speed(mph)': 'wind_speed_mph', 'Precipitation(in)': 'precipitation'
                  }
    states_to_filter = ['CA', 'TX']
    df = df[df['state'].isin(states_to_filter)]
    df.rename(columns=column_mapping, inplace=True)
    df.dropna(subset=['city'], inplace=True)
    df.dropna(subset=['zipcode'], inplace=True)
    df.rename(columns=lambda x: x.lower(), inplace=True)
    df.columns = df.columns.str.lower()
    df.drop(columns=['start_lat', 'start_lng', 'end_lat', 'end_lng', 'timezone', 'airport_code', 'weather_timestamp', 
                  'source', 'civil_twilight', 'nautical_twilight', 'astronomical_twilight', 'description'], inplace=True)
    df.replace({True: 1, False: 0}, inplace=True)
    desired_date = '2021-01-01'
    df['start_time'] >= desired_date
    df['start_time'] = pd.to_datetime(df['start_time'], format='%Y-%m-%d')
    df['end_time'] = pd.to_datetime(df['end_time'], format='%Y-%m-%d')
    df['start_date'] = df['start_time'].dt.date
    df['start_date'] = pd.to_datetime(df['start_date'], format='%Y-%m-%d')
    df['start_time_'] = df['start_time'].dt.time
    df['end_date'] = df['end_time'].dt.date
    df['end_date'] = pd.to_datetime(df['end_date'], format='%Y-%m-%d')
    df['day_of_week'] = df['start_time'].dt.weekday
    df['month'] = df['start_time'].dt.month
    df['len_of_affect'] = df.end_time - df.start_time
    def get_season(month):
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        elif month in [9, 10, 11]:
            return 'Autumn'
        else:
            return 'Unknown'
    df['season'] = df['start_date'].dt.month.apply(get_season)
    df= df.sort_values(by=['zipcode', 'street'], ascending=[False, True])
    df.drop(columns=['end_time', 'end_date', 'start_time', 'start_date'], axis=1, inplace=True)
    df.replace({'Day': 1, 'Night': 0}, inplace=True)    
    return df
    

def prep_output(df):
    
    df.drop(columns=['amenity', 'bump', 'crossing', 'give_way', 'railway', 'roundabout', 'station', 'no_exit', 'stop', 'traffic_calming', 'traffic_signal', 'street', 'junction', 'turning_loop'], inplace=True)    
    df['zipcode'] = df['zipcode'].astype('category')
    df['duration'] = pd.to_timedelta(df['len_of_affect'])
    states_to_filter = ['TX']
    df = df[df['state'].isin(states_to_filter)]
    df.drop(columns=['len_of_affect'], inplace=True)  
    df.dropna(subset=['weather_condition'], inplace=True)
    df.dropna(subset=['sunrise_sunset'], inplace=True)
    df.dropna(subset=['wind_direction'], inplace=True)
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])
    df.drop(columns = 'end_time')    
    df.set_index('start_time', inplace=True)
    df = df.drop(columns = 'end_time')
    df = df.drop(columns = 'start_date')
    df = df.drop(columns = 'start_time_')
    df = df.drop(columns = 'end_date')
    df['duration'] = df['duration'].dt.total_seconds() / 3600


    return df 

def remove_class(df):
    df = df.drop(columns = 'weather_condition')
    df = df.drop(columns = 'city')
    df = df.drop(columns = 'state')
    df = df.drop(columns = 'county')
    df = df.drop(columns = 'zipcode')
    df = df.drop(columns = 'country')
    
    mapping_season = {'Winter': 1, 'Spring': 2, 'Summer': 3, 'Autumn': 4}
    df['season'] = df['season'].replace(mapping_season)
    
    mapping_wind_direction = {'North': 1, 'NNW': 1, 'N': 1, 'NNE': 1, 'NE': 1, 'NW': 1, 'N': 1, 'East': 2, 'E': 2, 'ESE': 2, 'ENE': 2, 'South': 3, 'S': 3, 'SSE': 3, 'SE': 3, 'SW': 3, 'SSW': 3, 'West': 4, 'WNW': 4, 'WSW': 4, 'W': 4}
    df['wind_direction'] = df['wind_direction'].replace(mapping_wind_direction)
    
    values_to_drop = ['CALM', 'VAR', 'Variable']
    # Drop rows containing the specified values
    df = df[~df['wind_direction'].isin(values_to_drop)]
    df['wind_direction'] = df['wind_direction'].astype(int)

    
    return df
    
def remove_outliers(df):
    
        #got rid of outliers across all continuous variable features of impact outside of 3 standard deviations
    columns_to_filter = ['distance', 'temp', 'wind_chill', 'humidity', 'pressure', 'visibility', 'wind_speed_mph', 'precipitation', 'duration']
    
    threshold = 3
    
    # Calculate z-scores for the specified columns
    z_scores = df[columns_to_filter].apply(lambda x: np.abs((x - x.mean()) / x.std()))
    
    # Filter the DataFrame to exclude rows with outliers in any of the columns
    df = df[(z_scores <= threshold).all(axis=1)]
    
        #getting rid of weather conditions that don't happen enough to be of any significant impact on the dataset since there are 144 weather condition classificaitons
    
    #condition_counts = df['weather_condition'].value_counts()
    
    # Step 2: Filter out the weather conditions that occur less than 70,000 times
    #filtered_conditions = condition_counts[condition_counts >= 70000].index
    
    # Step 3: Remove the rows corresponding to the filtered weather conditions
    #df_filtered = df[df['weather_condition'].isin(filtered_conditions)]
    
    return df
    
    
def split_data(df):
    '''Split into train, validate, test with a 60/20/20 ratio'''
    train_validate, test = train_test_split(df, test_size=.2, random_state=42)
    train, validate = train_test_split(train_validate, test_size=.25, random_state=42)
    return train, validate, test