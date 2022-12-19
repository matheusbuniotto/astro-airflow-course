from airflow import DAG
#from airflow.operators.dummy import DummyOperator
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

### Define a dag object
default_args: dict 
default_args = {
    'retry' : 5,
    'retry_delay' : timedelta(minutes=5) } 


def _download_data(**kwargs):
    with open('/tmp/myfile.txt') as f:
        f.write('myfile')

with DAG(dag_id='simple_dag', schedule_interval = None, 
    default_args = default_args,
    catchup=False,
    start_date = datetime(2022, 12, 1)) as dag:
        
    downloading_data = PythonOperator(
        task_id = 'download_data',
        python_callable = _download_data
    )

    wait_for_data = FileSensor(
        task_id = 'wait_for_data',
        fs_conn_id = 'fs_default_test',
        filepath = 'myfile.txt' 
    )

    processing_data = BashOperator(
        task_id="processing_data",
        bash_command='exit 0'
    )
        
downloading_data >> wait_for_data >> processing_data