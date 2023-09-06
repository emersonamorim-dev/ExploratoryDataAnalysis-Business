from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Definindo funções a serem usadas nos Operators

def extract_user_activity():
    print("Data extracted for user activity")

def transform_user_activity():
    print("User activity data transformed")

def load_user_activity():
    print("Transformed user activity data loaded to target")

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
dag = DAG('user_activity_pipeline',
          default_args=default_args,
          description='An ETL pipeline for user activity data',
          # Executa diariamente
          schedule_interval=timedelta(days=1),  
          )

# Definindo os Operators
t1 = PythonOperator(task_id='extract_user_activity', python_callable=extract_user_activity, dag=dag)
t2 = PythonOperator(task_id='transform_user_activity', python_callable=transform_user_activity, dag=dag)
t3 = PythonOperator(task_id='load_user_activity', python_callable=load_user_activity, dag=dag)

# Definindo a ordem das tarefas
t1 >> t2 >> t3
