import airflow

if __name__ == '__main__':
    airflow_instance = airflow.Airflow()
    airflow_instance.talk()
    nb = airflow_instance.return_favorite_number()