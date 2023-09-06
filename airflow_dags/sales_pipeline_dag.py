from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Definindo funções a serem usadas nos Operators
def extract_sales_data():

    pass

def transform_sales_data():
    pass

def load_sales_data():
    pass

# Definindo os argumentos padrão
default_args = {
    'owner': 'you',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Definindo a DAG
dag = DAG('sales_pipeline',
          default_args=default_args,
          description='A sales ETL pipeline',
          # Executa diariamente
          schedule_interval=timedelta(days=1),  
          )

# Definindo os Operators
t1 = PythonOperator(task_id='extract_sales_data', python_callable=extract_sales_data, dag=dag)
t2 = PythonOperator(task_id='transform_sales_data', python_callable=transform_sales_data, dag=dag)
t3 = PythonOperator(task_id='load_sales_data', python_callable=load_sales_data, dag=dag)

# Definindo a ordem das tarefas
t1 >> t2 >> t3
