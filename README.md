1. Postgres and PgAdmin [optional] setup : https://medium.com/@mateus2050/setting-up-postgresql-and-pgadmin-using-docker-on-macos-66cd7d275328
2. Do `docker inspect <postgres_container_name/id>` , get the `gateway` and add it to the hostname in pgadmin for pgadmin to recognise the locally hosted postgres.

Now Postgres pod should be up and running

*** Good video to understand dbt : https://www.youtube.com/watch?v=M8oi7nSaWps ***  

1. Clone this repo
2. Do `docker inspect <postgres_container_name/id>` , get the `gateway` and replace the `host` already present as `172.17.0.1` with your gateway ip in data_ingesion.py file. 
3. Build the docker file : `docker build . -t air_dbt:v1`
4. Followed by : `docker compose up -d`

5. To run airflow in terminal :  
  a. Exec into the airflow container : `docker exec -it airflow-air_dbt-1 /bin/sh`  
  b. To list existing dags : `airflow dags list`  
  c. To run the data_ingesion dag run : `airflow tasks test csv_to_postgres_dag load_csv_to_postgres 2024-01-01`  
  d. To run the dbt_dag dag run : `airflow tasks test dbt_pipeline dbt_run 2024-01-01`  

6. To run in UI :
   a. portfoward the airflow container  
   b. To login username : `admin` , password will be present under `airflow/standalone_admin_password.txt`  
   c. Some times the new dags does not appear on the UI, might have to do `docker compose down` then `docker compose up`.  
