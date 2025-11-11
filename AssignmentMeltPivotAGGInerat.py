#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install -U ucimlrepo')
get_ipython().system('pip install pandas')



# In[ ]:


#Melt
#Pivot
#Aggregation
#Iteration
#Groupby
from ucimlrepo import fetch_ucirepo 

# fetch dataset 
breast_cancer = fetch_ucirepo(id=14) 

# data (as pandas dataframes) 
X = breast_cancer.data.features 
y = breast_cancer.data.targets 

# metadata 
print(breast_cancer.metadata) 

# variable information 
print(breast_cancer.variables) 


# In[3]:


#1 Melt
import pandas as pd
from ucimlrepo import fetch_ucirepo
breast_cancer = fetch_ucirepo(id=14)

X = breast_cancer.data.features 
y = breast_cancer.data.targets
df = pd.concat([X,y], axis = 1)

print("---Original Wide DataFrame(Head) ---")
print(df.head())
print("\nDataFrame Shape:", df.shape)

melted_df = pd.melt(df, var_name= 'feature_name', value_name= 'feature_value')
print("\n---Melted Long DataFrame(Head) ---")
print(melted_df.head())
print("\nDataFrame Shape:", melted_df.shape)




# In[4]:


#2 Pivot
#run previous steps to get melted
import pandas as pd
from ucimlrepo import fetch_ucirepo 
breast_cancer = fetch_ucirepo(id=14) 
X = breast_cancer.data.features 
y = breast_cancer.data.targets 
df = pd.concat([X, y], axis=1)
df['ID'] = df.index # Add the ID column
melted_df = pd.melt(df, id_vars=['ID'], var_name='feature_name', value_name='feature_value')
#pivot
pivoted_df = melted_df.pivot(index='ID', 
                             columns='feature_name', 
                             values='feature_value')

print("--- Pivoted Wide DataFrame (Head) ---")
print(pivoted_df.head())
print("\nDataFrame Shape:", pivoted_df.shape)


# In[5]:


#3 Aggregation
#run previous steps to get melted_df
import pandas as pd
from ucimlrepo import fetch_ucirepo 
breast_cancer = fetch_ucirepo(id=14) 
X = breast_cancer.data.features 
y = breast_cancer.data.targets 
df = pd.concat([X, y], axis=1)
df['ID'] = df.index # Add the ID column
melted_df = pd.melt(df, id_vars=['ID'], var_name='feature_name', value_name='feature_value')
print("--- Total counts for all features in melted format ---")

melted_agg = melted_df.groupby(['feature_name', 'feature_value']).size().reset_index(name='count')

print(melted_agg)


# In[2]:


#4 Iteration note I used iteruples() instead of iterrows
import pandas as pd
from ucimlrepo import fetch_ucirepo 
breast_cancer = fetch_ucirepo(id=14) 
X = breast_cancer.data.features 
y = breast_cancer.data.targets 
df = pd.concat([X, y], axis=1)

print("--- Iterating using itertuples() ---")
for row in df.itertuples():
    print(f"ID:{row.Index},Age:{row.age},Class:{row.Class}")
    if row.Index >=4:
        break


# In[1]:


# 5Groupby
import pandas as pd
from ucimlrepo import fetch_ucirepo 
breast_cancer = fetch_ucirepo(id=14) 
X = breast_cancer.data.features 
y = breast_cancer.data.targets 
df = pd.concat([X, y], axis=1)
class_counts = df.groupby('Class').size()

print("--- Counts per Class ---")
print(class_counts)


# In[ ]:




