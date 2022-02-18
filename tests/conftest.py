import airflow
import mock
import pytest


@pytest.fixture
def mock_airflow(monkeypatch):
    mock_airflow_instance = mock.MagicMock()
    monkeypatch.setattr(airflow, "Airflow", mock_airflow_instance)
    return mock_airflow_instance


class DummyAirflow:
    @staticmethod
    def return_favorite_number():
        return 0


@pytest.fixture(autouse=True)
def mock_airflow_with_dummy_class(monkeypatch):
    mock_airflow_instance = mock.MagicMock()
    monkeypatch.setattr(airflow, "Airflow", mock_airflow_instance)
    mock_airflow_instance.return_value = DummyAirflow()
    return mock_airflow_instance
