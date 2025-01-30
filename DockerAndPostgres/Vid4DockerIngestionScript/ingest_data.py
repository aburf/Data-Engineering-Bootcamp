
import pandas as pd
import argparse
import os  
##requires pip install sqlalchemy in codespaces
from sqlalchemy import create_engine
from time import time

##user, password, host, port, database name,  table name
##url of the csv

def main(params):
        user=params.user
        password = params.password
        host = params.host
        port = params.port
        db = params.db
        table_name = params.tabe_name
        data_url = params.url ##'/workspaces/Data-Engineering-Bootcamp/yellow_tripdata_1000.csv'
        csv_name = data_url.split('/')[-1]

    os.system(f"wget {url} -O {csv_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter = pd.read_csv(csv_name,iterator=True, chunksize=100)
    
    df = next(df_iter)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists = 'replace')
    df.to_sql(name=table_name, con=engine, if_exists='append')
    
    while True: 

        try:
            t_start = time()
            
            df = next(df_iter)

            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            df.to_sql(name=table_name, con=engine, if_exists='append')

            t_end = time()

            print('inserted another chunk, took %.3f second' % (t_end - t_start))

        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                        description='Ingest csv data to postgres',
                        epilog='bottomo text')
    parser.add_argument('--user')
    parser.add_argument('--password')
    parser.add_argument('--host')
    parser.add_argument('--port')
    parser.add_argument('--db')
    parser.add_argument('--table_name')
    parser.add_argument('--url')

    args = parser.parse_args()

    main(args)