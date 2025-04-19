# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime
# import pandas as pd
# import psycopg2

# default_args = {
#     'owner': 'airflow',
#     'start_date': datetime(2024, 1, 1),
# }


# def load_csv_to_postgres():
#     df = pd.read_csv('/opt/airflow/dataset/Online_Retail.csv', encoding='ISO-8859-1')

#     conn = psycopg2.connect(
#         host='172.17.0.1', database='postgres', user='postgres', password='admin', port='5432'
#     )
#     cur = conn.cursor()
#     for _, row in df.iterrows():
#         cur.execute(
#             """
#             INSERT INTO public.retail_table (InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country)
#             VALUES (%s, %s, %s,%s, %s, %s,%s, %s)
#         """,
#             (
#                 row['InvoiceNo'],
#                 row['StockCode'],
#                 row['Description'],
#                 row['Quantity'],
#                 row['InvoiceDate'],
#                 row['UnitPrice'],
#                 row['CustomerID'],
#                 row['Country'],
#             ),
#         )

#     conn.commit()
#     cur.close()
#     conn.close()


# with DAG(
#     'csv_to_postgres_dag', default_args=default_args, schedule_interval=None, catchup=False
# ) as dag:
#     task_load = PythonOperator(
#         task_id='load_csv_to_postgres', python_callable=load_csv_to_postgres
#     )
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import psycopg2

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}


def load_csv_to_postgres():
    df = pd.read_csv('/opt/airflow/dataset/Online_Retail.csv', encoding='ISO-8859-1')

    conn = psycopg2.connect(
        host='172.17.0.1', database='postgres', user='postgres', password='admin', port='5432'
    )
    cur = conn.cursor()

    # ✅ Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS public.retail_info_table (
            InvoiceNo TEXT,
            StockCode TEXT,
            Description TEXT,
            Quantity INTEGER,
            InvoiceDate TIMESTAMP,
            UnitPrice NUMERIC,
            CustomerID TEXT,
            Country TEXT
        )
    """)

    for _, row in df.iterrows():
        cur.execute(
            """
            INSERT INTO public.retail_info_table (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
            (
                row['InvoiceNo'],
                row['StockCode'],
                row['Description'],
                row['Quantity'],
                row['InvoiceDate'],
                row['UnitPrice'],
                row['CustomerID'],
                row['Country'],
            ),
        )

    conn.commit()
    cur.close()
    conn.close()


with DAG(
    'csv_to_postgres_dag', default_args=default_args, schedule_interval=None, catchup=False
) as dag:
    task_load = PythonOperator(
        task_id='load_csv_to_postgres', python_callable=load_csv_to_postgres
    )
