import airflow


def test_airflow_favorite_number():
    airflow_instance = airflow.Airflow()
    nb = airflow_instance.return_favorite_number()
    assert isinstance(nb, int)


def test_airflow_called(mock_airflow):
    airflow_instance = airflow.Airflow()
    mock_airflow.assert_called_once()


def test_airflow_not_called(mock_airflow):
    print("some stuff happening where airflow should never be started")
    # airflow_instance = airflow.Airflow()
    mock_airflow.assert_not_called()


def test_square_of_2():
    nb = airflow.calculate_square(2)
    assert nb == 4


def test_square_of_0():
    nb = airflow.calculate_square(0)
    assert nb == 0


def test_square_of_minus_1():
    nb = airflow.calculate_square(-1)
    assert nb == 1

