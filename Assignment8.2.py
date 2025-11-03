#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question 1 (15 Points)
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
Question 2 (15 Points)
Change the order of columns of a dataframe. Interchange columns 'a' and 'c'.
Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
Question 3 (15 Points)
Change the order of columns of a dataframe. Create a generic function to interchange two columns, without
hardcoding column names.
Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
Question 4 (15 Points)
Format or suppress scientific notations in a pandas dataframe. Suppress scientific notations like ‘e-03’ in df and
print upto 4 numbers after decimal.
Input
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
df
#> random
#> 0 3.474280e-03
#> 1 3.951517e-05
#> 2 7.469702e-02
#> 3 5.541282e-28
Desired Output
#> random
#> 0 0.0035
> 1 0.0000
#> 2 0.0747
#> 3 0.0000
Question 5 (15 Points)
Create a new column that contains the row number of nearest column by euclidean distance. Create a new column
such that, each row contains the row number of nearest row-record by euclidean distance.
Input

df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1),
columns=list('pqrs'), index=list('abcdefghij'))
df
# p q r s
# a 57 77 13 62
# b 68 5 92 24
# c 74 40 18 37
# d 80 17 39 60
# e 93 48 85 33
# f 69 55 8 11
# g 39 23 88 53
# h 63 28 25 61
# i 18 4 73 7
# j 79 12 45 34
Desired Output
df
# p q r s nearest_row dist
# a 57 77 13 62 i 116.0
# b 68 5 92 24 a 114.0
# c 74 40 18 37 i 91.0
# d 80 17 39 60 i 89.0
# e 93 48 85 33 i 92.0
# f 69 55 8 11 g 100.0
# g 39 23 88 53 f 100.0
# h 63 28 25 61 i 88.0
# i 18 4 73 7 a 116.0
# j 79 12 45 34 a 81.0

Question 6 (15 Points)

Correlation is a statistical technique that shows how two variables are related. Pandas dataframe.corr() method is
used for creating the correlation matrix. It is used to find the pairwise correlation of all columns in the dataframe.
Any na values are automatically excluded. For any non-numeric data type columns in the dataframe it is ignored.
Input
data = {'A': [45, 37, 0, 42, 50],
B': [38, 31, 1, 26, 90],
'C': [10, 15, -10, 17, 100],
'D': [60, 99, 15, 23, 56],
'E': [76, 98, -0.03, 78, 90]
}





# In[ ]:


get_ipython().system('pip install numpy')
get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')


# In[1]:


#Compute the euclidean distance between series (points) p and q, without using a packaged formula.
import pandas as pd
import math
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
difference = p -q
squared_difference = difference **2
sum_of_squared_difference = squared_difference.sum()
euclidean_distance = math.sqrt(sum_of_squared_difference)
print(f"THe Euclidean distance between series p and q is:{euclidean_distance}")


# In[2]:


#Question 2 
#Change the order of columns of a dataframe. Interchange columns 'a' and 'c'.
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(20).reshape(-1, 5),columns=list('abcde'))
print("Original DataFrame:")
print(df)
new_order = ['c','b','a','d','e']
df = df[new_order]
print("\nDataFrame with interchanged 'a' and 'c' columns:")
print(df)



# In[3]:


#Question 3Change the order of columns of a dataframe. Create a generic function to interchange two columns, without
#hardcoding column names.
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
def swap_column(df, col1_name, col2_name):
    """
    Args:
    df(pd.DataFrame): The input DataFrame.
    col1_name(str): The name of the first column to swap.
    col2_name(str): The name of the second column to swap.
    Returns:
       pd.DataFrame: The DataFrame with the two columns interchanged.
    """
    cols = list(df.columns)
    idx1 = cols.index(col1_name)
    idx2 = cols.index(col2_name)
    cols[idx1], cols[idx2] = cols[idx2], cols[idx1]
    return df[cols]

df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
print("Original DataFrame:")
print(df)
df_swapped = swap_column(df, 'a', 'c')
print("DataFrame after swapping 'a' and 'c'")
print(df_swapped)


# In[6]:


#Question 4 
#Format or suppress scientific notations in a pandas dataframe. Suppress scientific notations like ‘e-03’ in df and
#print upto 4 numbers after decimal.
import pandas as pd
import numpy as np
data = {'random': [3.474280e-03, 3.951517e-05, 7.469702e-02, 5.541282e-28]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

pd.set_option('display.float_format', '{:.4f}'.format)

print("\nFormatted DataFrame (no scientific notation, 4 decimals):")
print(df)


# In[4]:


#Question 5 
#Create a new column that contains the row number of nearest column by euclidean distance. Create a new column
#such that, each row contains the row number of nearest row-record by euclidean distance.
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1),
columns=list('pqrs'), index=list('abcdefghij'))
print("Original DataFrame (Note: values will be random):")
print(df)
def find_nearest_row(current_index, df_data):
    """Calculates the Euclidean distance from the current row to all other rows
    and returns the index and distance of the nearest neighbor."""

    current_row_values = df_data.loc[current_index].values
    min_distance = np.inf
    nearest_index = None
    for other_index, other_row in df_data.iterrows():
        # Skip calculating distance to itself
        if other_index == current_index:
            continue

        other_row_values = other_row.values 
        distance = np.sqrt(np.sum((current_row_values - other_row_values)**2))

        if distance < min_distance:
            min_distance = distance
            nearest_index = other_index
    return pd.Series([nearest_index, round(min_distance, 1)], index=['nearest_row', 'dist'])
nearest_neighbors_info = df.apply(lambda row: find_nearest_row(row.name, df), axis=1)
df[['nearest_row', 'dist']] = nearest_neighbors_info

print("\nDataFrame with nearest row information:")
print(df)            



# In[5]:


#Question 6
#Correlation is a statistical technique that shows how two variables are related. Pandas dataframe.corr() method is
#used for creating the correlation matrix. It is used to find the pairwise correlation of all columns in the dataframe.
#Any na values are automatically excluded. For any non-numeric data type columns in the dataframe it is ignored.
import pandas as pd
import numpy as np
data = {
    'A': [45, 37, 0, 42, 50],
    'B': [38, 31, 1, 26, 90],
    'C': [10, 15, -10, 17, 100],
    'D': [60, 99, 15, 23, 56],
    'E': [76, 98, -0.03, 78, 90]}
df = pd.DataFrame(data)
print("Original DataFrame;")
print(df)
correlation_matrix = df.corr()
print("\nCorrelation Matrix(using df.corr()):")
print(correlation_matrix)


# In[ ]:




