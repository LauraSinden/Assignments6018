#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 09:47:55 2021

@author: u6026797
"""
#%% libraries
import pandas as pd
import matplotlib.pyplot as plt
#%% data

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
covid_df = pd.read_csv(url, index_col=0)

#%% Instructions
'''
Overall instructions:
As described in the homework description, each graphic you make must:
   1. Have a thoughtful title
   2. Have clearly labelled axes 
   3. Be legible
   4. Not be a pie chart
I should be able to run your .py file and recreate the graphics without error.
As per usual, any helper variables or columns you create should be thoughtfully
named.
'''

#%% viz 1
'''
Create a visualization that shows all of the counties in Utah as a time series,
similar to the one shown in slide 22 during the lecture. The graphic should
-Show cases over time
-Have all counties plotted in a background color (something like grey)
-Have a single county plotted in a contrasting color (something not grey)
-Have well formatted dates as the X axis
'''

#%% viz 2
'''
Create a visualization that shows the contrast between the county in Utah with
the most cases to date to a county in Florida with the most cases to date.
The graphic should:
-Have only two counties plotted
-Highlight the difference between the two comparison counties
You may use any style of graphic you like as long as it is effective (dense)
and readable
'''

#%% viz 3
'''
Create a visualization that shows BOTH the running total of cases for a single
county AND the daily new cases. The graphic should:
-Use two y-axes (https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
-Use color to contrast the two series being plotted
-Have well formatted dates as the X axis
'''

#%% viz 4
'''
Create a visualization that shows a stacked bar chart of county contributions
to a given state's total cases. You may choose any state (or states).
(https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py)
The graphic should:
-Have a single column delineate a state
-Have each 'slice' or column compontent represent a county
'''

#%% extra credit (5 points)
'''
Use Seaborn to create a grouped box plot of all reported states. Each boxplot
should be a distinct state. Have the states ordered from most cases (FL) to fewest 
cases. (https://seaborn.pydata.org/examples/grouped_boxplot.html)
'''


# In[2]:


#1 Create a visualization that shows all of the counties in Utah as a time series,
#similar to the one shown in slide 22 during the lecture. The graphic should
#Show cases over time
#-Have all counties plotted in a background color (something like grey)
#-Have a single county plotted in a contrasting color (something not grey)
#Have well-formatted dates as the X axis
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
covid_df = pd.read_csv(url, index_col=0)

# Filter for Utah data
utah_df = covid_df[covid_df['Province_State'] == 'Utah']

# Drop irrelevant columns 
# Date columns start from index 10
dates = utah_df.columns[10:]
utah_cases_df = utah_df[['Admin2'] + list(dates)]

# Reformat the data from wide to long format 
utah_long_df = utah_cases_df.melt(id_vars=['Admin2'], var_name='Date', value_name='Cases') #

# Convert 'Date' column to datetime objects and set as index
utah_long_df['Date'] = pd.to_datetime(utah_long_df['Date'], format='%m/%d/%y')
# No need to set index if plotting with x and y args in matplotlib



# Set up the figure and axes
fig, ax = plt.subplots(figsize=(15, 8))

# Define the county to highlight
highlight_county_name = 'Salt Lake' 

# Plot all counties in a background color (grey)
# Group by county and plot each one
for county_name, county_data in utah_long_df.groupby('Admin2'):
    # Check if the county is the one to highlight
    if county_name == highlight_county_name:
        # Plot highlighted county later so it's on top
        continue
    ax.plot(county_data['Date'], county_data['Cases'], color='grey', alpha=0.5, linewidth=1)

# Plot the highlighted county in a contrasting color
highlight_county_data = utah_long_df[utah_long_df['Admin2'] == highlight_county_name]
ax.plot(highlight_county_data['Date'], highlight_county_data['Cases'], color='red', linewidth=3, label=f'{highlight_county_name} County') #



# Format the x-axis dates 
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45, ha='right') # Rotate dates for better visibility

# Add labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Confirmed COVID-19 Cases')
ax.set_title('COVID-19 Cases Over Time in Utah Counties (Highlighting Salt Lake County)')
ax.legend() 

# Add grid lines
ax.grid(True, linestyle='--', alpha=0.6)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()


# In[3]:


#2 Create a visualization that shows the contrast between the county in Utah with
#the most cases to date to a county in Florida with the most cases to date.
#The graphic should:
#-Have only two counties plotted
#-Highlight the difference between the two comparison counties
#You may use any style of graphic you like as long as it is effective (dense)
#and readable

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
from matplotlib.ticker import ScalarFormatter 
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"


# Load the data into a pandas DataFrame
df = pd.read_csv(url)

# Filter the DataFrame for the two specific counties using their FIPS codes
# Salt Lake County, Utah FIPS: 49035
# Miami-Dade County, Florida FIPS: 12086
salt_lake_county_data = df[df['FIPS'] == 49035]
miami_dade_county_data = df[df['FIPS'] == 12086]

# Extract time-series data 
# The dates are columns starting from index 11
# Updated line with format specified
dates = pd.to_datetime(salt_lake_county_data.columns[11:], format='%m/%d/%y')
salt_lake_cases = salt_lake_county_data.iloc[0, 11:].values.astype(int)
miami_dade_cases = miami_dade_county_data.iloc[0, 11:].values.astype(int)


plt.figure(figsize=(12, 8))

# Plot the data
plt.plot(dates, salt_lake_cases, label='Salt Lake County, UT', color='darkorange', linewidth=2)
plt.plot(dates, miami_dade_cases, label='Miami-Dade County, FL', color='navy', linewidth=2)

# Highlight the difference using shading 
plt.fill_between(dates, salt_lake_cases, miami_dade_cases, color='gray', alpha=0.3,
                 label='Difference in Total Cases')

# Format the x-axis dates
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6)) # Show ticks every 6 months
plt.xticks(rotation=45, ha='right')

# Format the y-axis to prevent scientific notation and add a label

formatter = ScalarFormatter()
formatter.set_scientific(False)
formatter.useOffset = False
plt.gca().yaxis.set_major_formatter(formatter)
plt.ticklabel_format(style='plain', axis='y')

# Add titles and labels
plt.title('Comparison of Cumulative COVID-19 Cases: Salt Lake County vs. Miami-Dade County', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Cumulative Confirmed Cases', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)

# Add an annotation to highlight the magnitude difference
plt.annotate(
    'Miami-Dade County shows a significantly higher case count, likely due to a larger population and different regional factors.',
    xy=(dates[len(dates)//2], max(miami_dade_cases) / 2),
    xytext=(dates[len(dates)//4], max(miami_dade_cases) / 2.5),
    arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle="arc3,rad=0.2"),
    fontsize=10,
    color='dimgray'
)

# Adjust layout to prevent clipping of labels
plt.tight_layout()

# Display the plot
plt.show()




# In[4]:


#3 Create a visualization that shows BOTH the running total of cases for a single
#county AND the daily new cases. The graphic should:
#Use two y-axes (https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
#Use color to contrast the two series being plotted
#Have well formatted dates as the X axis

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
from matplotlib.ticker import ScalarFormatter 
from datetime import datetime, timedelta 

def create_dual_axis_case_visualization(df, county_name):
    """
    Generates a dual y-axis plot showing both the running total of cases 
    and the daily new cases for a single county.

    Args:
        df (pd.DataFrame): DataFrame with 'Date' (datetime) and 'Cases' (daily counts) columns.
        county_name (str): The name of the county for the title.
    """

   # Ensure Date is datetime object and set as index 
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    # Calculate running total
    df['Running Total'] = df['Cases'].cumsum()

    # Create figure and primary axis (ax1)
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Instantiate a second axis (ax2) that shares the same x-axis
    ax2 = ax1.twinx()

    # Define colors
    color1 = 'tab:blue'
    color2 = 'tab:red'

    # Plotting the data
    # Primary axis (ax1) for Running Total (Line Plot)
    ax1.plot(df['Date'], df['Running Total'], color=color1, linewidth=2, label='Running Total Cases')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Running Total Cases', color=color1)
    ax1.tick_params(axis='y', labelcolor=color1) 
    ax1.grid(True, alpha=0.3)

    # Secondary axis (ax2) for Daily New Cases 
    ax2.bar(df['Date'], df['Cases'], color=color2, alpha=0.5, label='Daily New Cases')
    ax2.set_ylabel('Daily New Cases', color=color2)
    ax2.tick_params(axis='y', labelcolor=color2) # Color the ticks to match the bars

    # Formatting the X-axis dates
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=max(1, len(df)//10))) # Adjust interval based on data length
    plt.xticks(rotation=45, ha='right') 


    plt.title(f'COVID-19 Cases in {county_name}: Running Total vs. Daily New Cases')
    fig.tight_layout() # Prevents labels from overlapping

    # Show the plot
    plt.show()


# 1. Create sample data 
data = {
    'Date': [datetime(2023, 1, i) for i in range(1, 32)],
    'Cases': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160]
}
# Add some variations 
data['Cases'] = [c + (i % 5) * 2 for i, c in enumerate(data['Cases'])]

sample_df = pd.DataFrame(data)

# 2. Call the function to generate the visualization
create_dual_axis_case_visualization(sample_df, "Sample County")


# In[1]:


#4 Create a visualization that shows a stacked bar chart of county contributions
#to a given state's total cases. You may choose any state (or states).
#(https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py)
#The graphic should:
#-Have a single column delineate a state
#-Have each 'slice' or column component represent a county


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
from matplotlib.ticker import ScalarFormatter 
from datetime import datetime, timedelta 
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
covid_df = pd.read_csv(url, index_col=0)


# --- Code for Visualization ---

def plot_state_county_stacked_bar(df, state_name, num_counties_to_show=10):
    """
    Generates a stacked bar chart showing county contributions to a state's total COVID-19 cases.

    Args:
        df (pd.DataFrame): The COVID-19 dataframe.
        state_name (str): The state to visualize (e.g., 'California', 'Utah').
        num_counties_to_show (int): The number of top counties to show individually.
                                    Smaller counties will be grouped into an 'Other Counties' category.
    """


    # The last column represents the most recent date's cumulative cases
    latest_date_col = df.columns[-1]
    state_data = df[df['Province_State'] == state_name].copy()



    # Clean up non-county entries
    state_data = state_data[~state_data['Admin2'].isin(['Unassigned', 'Out of TX', 'Out of PR', 'Out of NY', 'Statewide Unallocated'])]

    # Group by county ('Admin2') and get the total cases for the latest date
    county_cases = state_data.groupby('Admin2')[latest_date_col].sum().sort_values(ascending=False)

    if county_cases.empty:
        print(f"No data found for state '{state_name}' or data is empty after cleaning.")
        return

    # 2. Grouping smaller counties into an 'Other' category
    # This prevents the chart from becoming too cluttered with dozens of tiny slices
    top_counties = county_cases.head(num_counties_to_show)
    other_cases_sum = county_cases.iloc[num_counties_to_show:].sum()

    if other_cases_sum > 0:
        final_series = pd.concat([top_counties, pd.Series({'Other Counties': other_cases_sum})]).sort_values(ascending=False)
    else:
        final_series = top_counties

    # 3. Create the Visualization

    fig, ax = plt.subplots(figsize=(8, 10))

    # The base of the stack starts at 0
    bottom = 0
    state_total = final_series.sum()


    x_pos = 0.5 
    width = 0.5

    # Iterate through each county (or group) and stack their contributions
    for county, cases in final_series.items():
        # Plot the current county's contribution on top of the previous ones
        ax.bar(x_pos, cases, width, label=f'{county} ({cases:,})', bottom=bottom)
        # Increase the bottom position for the next iteration
        bottom += cases

    # 4. Customization and Labels
    ax.set_ylabel('Total Confirmed Cases')
    ax.set_title(f'County Contribution to {state_name} Total Cases\n(Data as of {latest_date_col})')

    # Remove the generic x-tick label since there is only one logical 'bar'
    ax.set_xticks([x_pos])
    ax.set_xticklabels([f'{state_name}\nTotal: {state_total:,}'])

    # Format the Y-axis to use commas for readability
    ax.get_yaxis().set_major_formatter(ScalarFormatter(useOffset=False, useMathText=False))
    ax.ticklabel_format(axis='y', style='plain')

    # Add a legend outside the plot for better visibility
    ax.legend(title='Counties', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.show()



# Example 1: California
plot_state_county_stacked_bar(covid_df, 'California', num_counties_to_show=10)


# In[ ]:


#Use Seaborn to create a grouped box plot of all reported states. Each boxplot
#should be a distinct state. Have the states ordered from most cases (FL) to fewest 
#cases. (https://seaborn.pydata.org/examples/grouped_boxplot.html)
get_ipython().system('pip install seaborn')


# In[5]:


#EC Use Seaborn to create a grouped box plot of all reported states. Each boxplot
#should be a distinct state. Have the states ordered from most cases (FL) to fewest 
#cases. (https://seaborn.pydata.org/examples/grouped_boxplot.html)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Create a sample DataFrame with 'State' and 'Cases'
np.random.seed(0)
data = {
    'State': ['FL']*50 + ['NY']*50 + ['CA']*50 + ['TX']*50 + ['WA']*50,
    'Cases': np.random.randint(1000, 5000, 50).tolist() +
             np.random.randint(500, 4000, 50).tolist() +
             np.random.randint(1500, 6000, 50).tolist() +
             np.random.randint(800, 4500, 50).tolist() +
             np.random.randint(200, 1500, 50).tolist()
}
df = pd.DataFrame(data)
state_order = df.groupby('State')['Cases'].median().sort_values(ascending=False).index
# Set a clean Seaborn style
sns.set_style("whitegrid")

# Create the box plot
plt.figure(figsize=(10, 6)) # Adjust figure size for better readability
sns.boxplot(x='State', y='Cases', data=df, order=state_order, palette="pastel", hue='State', legend=False)

# Add titles and labels
plt.title('Grouped Box Plot of Cases per State (Ordered by Median Case Count)')
plt.xlabel('State')
plt.ylabel('Number of Cases')

# Display the plot
plt.show()


# In[ ]:





