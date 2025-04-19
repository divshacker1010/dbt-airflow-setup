from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='dbt_pipeline',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['dbt'],
) as dag:
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /opt/airflow/dbt && dbt run --select stockcode_filter.sql',
    )
