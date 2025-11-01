#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')


# In[ ]:


# -*- coding: utf-8 -*-

#%% Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%% Importing Data
flights_data = pd.read_csv('flights.csv')
flights_data.head(10)
weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()
#%% Pandas Data Filtering/Sorting Question Answering
#use flights_data

#Question 1 How many flights were there from JFK to SLC? Int
q_1 
#Question 2 How many airlines fly to SLC? Should be int
q_2 
#Question 3 What is the average arrival delay for flights to RDU? float
q_3
#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
q_4 
#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)
q_5 
#Question 6 Which date has the largest average arrival delay? pd slice with date and float
q_6 
#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
q_7
#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
q_8 
#%% Numpy Data Filtering/Sorting Question Answering
#Use weather_data_np
#Question 9 How many observations were made in Feburary? Int
q_9 
#Question 10 What was the mean for humidity in February? Float
q_10
#Question 11 What was the std for humidity in February? Float
q_11


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#%% Importing Data
flights_data = pd.read_csv('flights.csv')
flights_data.head(10)
weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()


# In[1]:


#Question 1 How many flights were there from JFK to SLC? Int
#q_1 import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
flights_data = pd.read_csv('flights.csv')
filtered_flights = flights_data[
    (flights_data['origin'] == 'JFK') & 
    (flights_data['dest'] == 'SLC')]
q_1 = len(filtered_flights)
print(f"There were {q_1} flights from JFK to SLC.")
print(f"The result is stored in the variable 'q_1': {q_1}")


# In[2]:


#Question 2 How many airlines fly to SLC? Should be int
#q_2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
flights_data = pd.read_csv('flights.csv') 
flights_to_slc = flights_data[flights_data['dest'] == 'SLC']
q_2 = flights_to_slc['carrier'].nunique()
print(f"There are {q_2} airlines that fly to SLC.")
print(f"The result is stored in the variable 'q_2': {q_2}")


# In[3]:


#Question 3 What is the average arrival delay for flights to RDU? float
#q_3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
flights_data = pd.read_csv('flights.csv')
flights_to_rdu = flights_data[flights_data['dest'] == 'RDU']
q_3 = flights_to_rdu['arr_delay'].mean()
print(f"Average arrival delay for flights to RDU: {q_3:.2f} minutes")
print(f"The result (float) is stored in the variable 'q_3': {q_3}")


# In[4]:


#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
#q_4 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
flights_data = pd.read_csv('flights.csv')
all_flights_to_sea = flights_data[flights_data['dest'] == 'SEA']
total_to_sea_count = len(all_flights_to_sea)
nyc_to_sea_flights = all_flights_to_sea[
    (all_flights_to_sea['origin'] == 'JFK') | 
    (all_flights_to_sea['origin'] == 'LGA')]
nyc_to_sea_count = len(nyc_to_sea_flights)
q_4 = nyc_to_sea_count / total_to_sea_count
print(f"Total flights to SEA: {total_to_sea_count}")
print(f"Flights from NYC to SEA: {nyc_to_sea_count}")
print(f"Proportion: {q_4:.4f}")
print(f"The result (float) is stored in the variable 'q_4': {q_4}")


# In[ ]:


#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)
#q_5 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
flights_data = pd.read_csv('flights.csv')
flights_data['date'] = flights_data['year'].astype(str) + '/' + \
                       flights_data['month'].astype(str) + '/' + \
                       flights_data['day'].astype(str)
daily_avg_delays = flights_data.groupby('date')['dep_delay'].mean()
date_with_max_delay = daily_avg_delays.idxmax()
max_avg_delay_value = daily_avg_delays.loc[date_with_max_delay]
q_5 = pd.Series(
    {'date': date_with_max_delay, 'max_avg_dep_delay': max_avg_delay_value})
print(f"The date with the largest average departure delay is:")
print(q_5)


# In[5]:


#Question 6 Which date has the largest average arrival delay? pd slice with date and float
#q_6 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
flights_data = pd.read_csv('flights.csv')
flights_data['date'] = flights_data['year'].astype(str) + '/' + \
                       flights_data['month'].astype(str) + '/' + \
                       flights_data['day'].astype(str)
daily_avg_arr_delays = flights_data.groupby('date')['arr_delay'].mean()
date_with_max_arr_delay = daily_avg_arr_delays.idxmax()
max_avg_arr_delay_value = daily_avg_arr_delays.loc[date_with_max_arr_delay]
q_6 = pd.Series({'date': date_with_max_arr_delay, 'max_avg_arr_delay': max_avg_arr_delay_value})
print(f"The date with the largest average arrival delay is:")
print(q_6)


# In[6]:


#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
#q_7
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
flights_data = pd.read_csv('flights.csv')
nyc_flights = flights_data[flights_data['origin'].isin(['JFK', 'LGA'])]
nyc_flights_clean = nyc_flights.dropna(subset=['distance', 'air_time'])
nyc_flights_clean = nyc_flights.dropna(subset=['distance', 'air_time']).copy() 
nyc_flights_clean['speed'] = nyc_flights_clean['distance'] / nyc_flights_clean['air_time']
fastest_flight_index = nyc_flights_clean['speed'].idxmax()
q_7 = nyc_flights_clean.loc[fastest_flight_index, ['tailnum', 'speed']]
print(f"The fastest flight from JFK/LGA has the following details (speed in miles/minute):")
print(q_7)
print(f"The result (pd slice) is stored in the variable 'q_7'.")








# In[7]:


#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
#q_8
weather_data_pd = pd.read_csv('weather.csv')
q_8 = weather_data_pd.fillna(0)
print("All NaN values in the weather_data_pd DataFrame have been replaced with 0s.")
print(f"The resulting DataFrame is stored in the variable 'q_8'.")


# In[8]:


#Question 9 How many observations were made in Feburary? Int
#q_9 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()
february_data = weather_data_pd[weather_data_pd['month'] == 2]
q_9 = len(february_data)
print(f"Number of observations made in February: {q_9}")
print(f"The result is stored in the integer variable 'q_9': {q_9}")


# In[9]:


#Question 10 What was the mean for humidity in February? Float
#q_10
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()
february_data = weather_data_pd[weather_data_pd['month'] == 2]
q_10 = february_data['humid'].mean()
print(f"Mean humidity in February: {q_10:.4f}")
print(f"The result is stored in the float variable 'q_10': {q_10}")


# In[10]:


##Question 11 What was the std for humidity in February? Float
#q_11
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()
february_data = weather_data_pd[weather_data_pd['month'] == 2]
q_11 = february_data['humid'].std()
print(f"The standard deviation for humidity in February was: {q_11:.4f}")
print(f"The result (float) is stored in the variable 'q_11': {q_11}")


# In[ ]:




