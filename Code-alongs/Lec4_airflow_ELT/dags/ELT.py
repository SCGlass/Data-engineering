from airflow.decorators import dag, task_group, task
from datetime import datetime


@dag(dag_id= "queue_time_ELT", start_date=datetime(2023,8,15))
def queue_time_ELT():
    pass

queue_time_ELT()