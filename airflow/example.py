from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    print("Lấy dữ liệu API")

def transform():
    print("Làm sạch dữ liệu")

def load():
    print("Lưu vào database")

with DAG(
    dag_id="orders_etl",
    start_date=datetime(2026, 11, 1),
    schedule="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="extract",
        python_callable=extract
    )

    t2 = PythonOperator(
        task_id="transform",
        python_callable=transform
    )

    t3 = PythonOperator(
        task_id="load",
        python_callable=load
    )

    t1 >> t2 >> t3