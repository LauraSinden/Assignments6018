#!/usr/bin/env python
# coding: utf-8

# In[5]:


#The library I used was SQLAlchemy. I used the database that I built for BMI 6203  

# SQLAlchemy is a powerful and widely-used open-source SQL toolkit and Object Relational Mapper (ORM) for Python. 
#It provides a flexible and efficient way for Python applications to interact with various types of relational databases.
#SQLAlchemy empowers Python developers to work with relational databases more effectively,
#whether by constructing SQL queries programmatically or by using an object-oriented approach to manage data.


# In[6]:


get_ipython().system('pip install -U ucimlrepo')
get_ipython().system('pip install pandas')
get_ipython().system('pip install sqlalchemy pandas')
from sqlalchemy import create_engine
import pandas as pd

from sqlalchemy import create_engine, inspect
import pandas as pd



# In[7]:


#Find the assays table
from sqlalchemy import create_engine, inspect
import pandas as pd

engine = create_engine(r'sqlite:///C:\Users\Laura\Downloads\ARUPlitelabdatabase.db')


# Create an inspector object
inspector = inspect(engine)

# Get list of all table names in the connected database
table_names = inspector.get_table_names()

print(f"Connected to database file. Found tables: {table_names}")


query = "SELECT * FROM Assays"

# Rerun the read_sql command
df = pd.read_sql(query, engine)
print(df.head())


# In[8]:


#Find the patient table
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import inspect

# Use a raw string (r prefix) and the correct file extension/path
correct_db_path = r'sqlite:///C:\Users\Laura\Downloads\ARUPlitelabdatabase.db'

engine = create_engine(correct_db_path)

# Verify connection and list tables
inspector = inspect(engine)
table_names = inspector.get_table_names()

print(f"Connected to database file. Found tables: {table_names}")

# If "Patient" appears in the output list, run your query:
if "Patient" in table_names:
    correct_table_name = "Patient" 
    query = f"SELECT * FROM {correct_table_name};"
    df = pd.read_sql(query, engine)
    print(df.head())
else:
    print(f"The 'Patient' table was not found. Found tables: {table_names}")


# In[9]:


#Find order_Id for each assay
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import inspect

# Use a raw string (r prefix) and the correct file extension/path
correct_db_path = r'sqlite:///C:\Users\Laura\Downloads\ARUPlitelabdatabase.db'

engine = create_engine(correct_db_path)

# Verify connection and list tables
inspector = inspect(engine)
table_names = inspector.get_table_names()

print(f"Connected to database file. Found tables: {table_names}")

# If "Patient" appears in the output list, run your query:
if "Patient" in table_names:
    correct_table_name = "Assays" 
    query = f"SELECT * FROM {correct_table_name};"
    df = pd.read_sql(query, engine)
    print(df.head())
else:
    print(f"The 'Patient' table was not found. Found tables: {table_names}")


# In[10]:


#what is the name of the client who ordered the most testosterone tests
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import inspect
 #Assuming your previous imports and 'engine' creation are still active:
engine = create_engine(r'sqlite:///C:\Users\Laura\Downloads\ARUPlitelabdatabase.db')

# 1. Define the SQL query

sql_query = """
SELECT 
    P."Client_Account" AS ClientName,
    COUNT(A."70130 Testosterone") AS TestosteroneTestCount
FROM 
    "Physician" AS P
JOIN 
    "Orders" AS O ON P."Physician ID" = O."Physician_ID"
JOIN 
    "Assays" AS A ON O."Order ID" = A."Order ID"
WHERE 
    A."70130 Testosterone" = 1
GROUP BY 
    ClientName
ORDER BY 
    TestosteroneTestCount DESC
LIMIT 1;
"""

# Execute the query
result_df = pd.read_sql(sql_query, engine)

# Print the result
if not result_df.empty:
    client_name = result_df["ClientName"].iloc[0]
    count = result_df["TestosteroneTestCount"].iloc[0]
    print(f"The client who ordered the most testosterone tests is: {client_name}")
    print(f"Total testosterone tests ordered: {count}")
else:
    print("No results found. Please check your data or column values (e.g., ensure the test value is exactly 1).")






# In[11]:


# Assuming 'engine' is already defined and working:
engine = create_engine(r'sqlite:///C:\Users\Laura\Downloads\ARUPlitelabdatabase.db')

# Inspect columns for both tables
assays_columns = pd.read_sql("PRAGMA table_info(Assays);", engine)['name'].tolist()
physicians_columns = pd.read_sql("PRAGMA table_info(Physician);", engine)['name'].tolist() # Assuming table name is 'Physicians'

print(f"Assays columns: {assays_columns}")
print(f"Physicians columns: {physicians_columns}")


# In[ ]:




