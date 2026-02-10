#### Question 1. What is count of records for the 2024 Yellow Taxi Data? (1 point)
0,332,093

#### Question 2. Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables. What is the estimated amount of data that will be read when this query is executed on the External Table and the Table? (1 point)
0 MB for the External Table and 155.12 MB for the Materialized Table

#### Question 3. Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. Now write a query to retrieve the PULocationID and DOLocationID on the same table. Why are the estimated number of Bytes different? (1 point)
BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.
BigQuery stores table data in columnar format, meaning it stores each column separately. Column-oriented databases are particularly efficient at scanning individual columns over an entire dataset.


#### Question 4. Question 4. How many records have a fare_amount of 0? (1 point)
8,333

Question 5. What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID (Create a new table with this strategy) (1 point)
Partition by tpep_dropoff_datetime and Cluster on VendorID
Clustered tables sort data based on user-defined sorting properties. Data in these clustered columns is sorted into storage blocks whose size is adaptively adjusted based on the table size. However, when you run a query that filters based on a clustered column, BigQuery only scans the relevant blocks based on that clustered column, not the entire table or table partition. In a combined approach that uses table partitions and clustering, table data is first divided into partitions, then the data within each partition is clustered based on the clustering column. With this approach, you can achieve more detailed sorting, as shown in the following diagram:


#### Question 6. Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (inclusive). Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 5 and note the estimated bytes processed. What are these values? (1 point)
310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

#### Question 7. Where is the data stored in the External Table you created? (1 point)
GCP Bucket

#### Question 8. It is best practice in Big Query to always cluster your data: (1 point)
False
Although grouping tables with clustered tables can simplify data queries, you will not receive an accurate query cost estimate before the query execution is complete because the number of storage blocks to be scanned is unknown. The final cost is determined after the query execution is complete and is based on the specific storage blocks that have been scanned.

#### Question 9. Write a `SELECT count(*)` query FROM the materialized table you created. How many bytes does it estimate will be read? Why? (not graded)
0 bytes, even though writing count(*) is like asking the database to count all the data in the database, which should result in a very large cost, BigQuery has a metadata cache that stores information about the characteristics of the datasets in the database and the queries to access them, so when accessing queries with count(*), BigQuery will only retrieve the data count from the metadata without scanning the data per column ('INFORMATION_SCHEMA. TABLE_STORAGE')
