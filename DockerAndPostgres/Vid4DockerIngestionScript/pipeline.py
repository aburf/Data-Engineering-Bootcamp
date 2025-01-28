#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os


# In[3]:


pd.__version__
os.getcwd()


# In[4]:


data_url = '/workspaces/Data-Engineering-Bootcamp/yellow_tripdata_1000.csv'
csv_name = data_url.split('/')[-1]
df = pd.read_csv(data_url, nrows=50)
df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


# In[5]:


df.head()


# In[7]:


##requires pip install sqlalchemy in codespaces
from sqlalchemy import create_engine


# In[9]:


##need to pip install psycopg2-binary
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[10]:


engine.connect()


# In[11]:


###get  an approach for creating this table in postgres
print(pd.io.sql.get_schema(df, name='yellow_taxi_data',con=engine))


# In[12]:


df_iter = pd.read_csv(data_url,iterator=True, chunksize=100)


# In[13]:


df = next(df_iter)
len(df)
df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


# In[14]:


df.head(n=0)


# In[15]:


df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists = 'replace')


# In[16]:


get_ipython().run_line_magic('time', "df.to_sql(name='yellow_taxi_data', con=engine, if_exists = 'append')")


# In[17]:


from time import time


# In[18]:


####iterate through batches. I ran low on memory but should work in a better VM

for x in df_iter:
    t_start = time()
    df = next(df_iter)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.to_sql(name='yellow_taxi_data', con=engine, if_exists = 'append')
    t_end = time()
    print('Inserted another chunk..., to %.3f seconds'% (t_end-t_start)) 


# In[ ]:




