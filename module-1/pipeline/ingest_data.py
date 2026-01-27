#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

# Read data parquet
df_parquet = pd.read_parquet('green_tripdata_2025-11.parquet')

# Convert to csv
df_parquet.to_csv("green_tripdata_2025-11.csv", index=False)

len(df_parquet)

# Read data csv
file_data = "green_tripdata_2025-11.csv"
df = pd.read_csv(file_data)

# Print df
df

# Check data types
df.dtypes

# Check data shape
df.shape

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "lpep_pickup_datetime",
    "lpep_dropoff_datetime"
]

# Create engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

# Get DDL schema
print(pd.io.sql.get_schema(df, name='green_trip_data', con=engine))

# Create the table
df.head(n=0).to_sql(name='green_trip_data', con=engine, if_exists='replace')

# Separate data (chunk)
df_iter = pd.read_csv(
    file_data,
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=10000,
)

get_ipython().system('uv add tqdm')

for df_chunk in tqdm(df_iter):
    df_chunk.to_sql(name='green_trip_data', con=engine, if_exists='append')



