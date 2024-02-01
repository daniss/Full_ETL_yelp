from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from transform import transform

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 1, 1),
    'email': ['test@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

def just_a_function():
    print("I'm going to show you something :)")

dag = DAG(
    'full_etl_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1)
)

run_just_all = PythonOperator(
    task_id='run_just_a_function',
    python_callable=transform,
    dag=dag
)

run_just_all