

import pandas as pd
import os
##requires pip install sqlalchemy in codespaces
from sqlalchemy import create_engine
from time import time

##need to pip install psycopg2-binary'
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
##engine.connect()


data_url = '/workspaces/Data-Engineering-Bootcamp/yellow_tripdata_1000.csv'
csv_name = data_url.split('/')[-1]
df = pd.read_csv(data_url, nrows=50)
df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

df_iter = pd.read_csv(data_url,iterator=True, chunksize=100)


df = next(df_iter)
df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists = 'replace')




####iterate through batches. I ran low on memory but should work in a better VM
while True:
#for x in df_iter:
    t_start = time()
    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.to_sql(name='yellow_taxi_data', con=engine, if_exists = 'append')
    t_end = time()
    print('Inserted another chunk..., to %.3f seconds'% (t_end-t_start)) 

