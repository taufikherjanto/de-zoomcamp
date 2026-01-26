# Module 1 Homework: Docker & SQL

## Question 1. Understanding docker first run

Run docker with the `python:3.13` image in an interactive mode, use the entrypoint `bash`.
```
docker run --rm -it python:3.13 bash
python -m pip --version
```
What's the version of pip in the python:3.13 image?
- 25.3  <---
- 24.3.1
- 24.2.1
- 23.3.1

## Question 2. Understanding docker composing
```
services:
  db:
    container_name: postgres
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - '5432:5432'
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
      PGADMIN_DEFAULT_PASSWORD: "pgadmin"
    ports:
      - "8080:80"
    volumes:
      - vol-pgadmin_data:/var/lib/pgadmin  

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data
```
Given the docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?
- postgres:5433
- localhost:5432
- db:5433
- postgres:5432
- db:5432 <---

## Question 3.



## Question 4.



## Question 5.



## Question 6.


## Question 7.
