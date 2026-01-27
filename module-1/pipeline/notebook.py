#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd

# Read data parquet
df_parquet = pd.read_parquet('green_tripdata_2025-11.parquet')

# Convert to csv
df_parquet.to_csv("green_tripdata_2025-11.csv", index=False)

len(df_parquet)


# In[76]:


# Read data csv
file_data = "green_tripdata_2025-11.csv"
df = pd.read_csv(file_data)


# In[88]:


# Print df
df


# In[89]:


# Check data types
df.dtypes


# In[90]:


# Check data shape
df.shape


# In[91]:


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


# In[92]:


# Create engine
from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[93]:


# Get DDL schema
print(pd.io.sql.get_schema(df, name='green_trip_data', con=engine))


# In[94]:


# Create the table
df.head(n=0).to_sql(name='green_trip_data', con=engine, if_exists='replace')


# In[95]:


# Separate data (chunk)
df_iter = pd.read_csv(
    file_data,
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=10000,
)


# In[96]:


get_ipython().system('uv add tqdm')


# In[97]:


from tqdm.auto import tqdm


# In[98]:


for df_chunk in tqdm(df_iter):
    df_chunk.to_sql(name='green_trip_data', con=engine, if_exists='append')


# In[ ]:





# In[67]:





# In[ ]:





# In[ ]:





# In[ ]:




