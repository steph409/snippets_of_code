import airflow
import mock


# @mock.patch('airflow.Airflow')
def mock_airflow(monkeypatch):
    def mock_talk():
        print("BUT I WANT TO BE AIRFLOW")
    monkeypatch.talk = mock_talk
    return monkeypatch


if __name__ == '__main__':
    airflow_instance = airflow.Airflow()
    airflow_instance.talk()