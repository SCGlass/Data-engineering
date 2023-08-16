from airflow.decorators import dag, task_group, task
from datetime import datetime
from include.setup import setup_directories

@dag(dag_id = "que_time_ELT", start_date=datetime(2023,8,16))
def queue_time_ELT():
    setup = setup_directories

    setup

queue_time_ELT()