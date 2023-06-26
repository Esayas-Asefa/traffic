'''
Acquire traffic data

Functions:
- get_traffic_data
'''

##### IMPORTS #####
#import os
import numpy as np
import pandas as pd

def get_traffic_data():
    
    df = pd.read_csv('originial-traff-csv.zip')
    """
    This function reads traffic data from a CSV file or from kaggle.com and caches it locally for future
    use.
    :return: The function `get_traffic_data()` returns a pandas DataFrame containing information about different
    traffic incidents. If the data is already cached locally in a CSV file named 'original-traff-csv.zip', it reads the
    data from the file and returns it. Otherwise, it fetches the data from two different URLs on
    kaggle, combines them into a single DataFrame, saves the data to a CSV file named 'originial-traff-csv.zip',
    """
    # filename of csv
   # filename='original-traff-csv.zip'
    # if cached data exist
    #if os.path.isfile(filename):
    #    return pd.read_csv(filename)
    # wrangle from kaggle.com if not cached
    #else:
        # kaggle links
    #    df = pd.read_csv('https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents')
    return df