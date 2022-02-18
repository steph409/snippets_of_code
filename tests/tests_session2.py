import pytest
import airflow
import pandas as pd
import os


@pytest.mark.parametrize("test_input,expected", [(3, 9), (0, 0), (1, 1), pytest.param(3, 19, marks=pytest.mark.xfail)])
def test_calculate_square(test_input, expected):
    assert airflow.calculate_square(test_input) == expected


@pytest.mark.parametrize("file_name", os.listdir("data/input/"))
def test_my_preprocessing(file_name):
    df = pd.read_csv(f"data/input/{file_name}.csv")
    output = airflow.Airflow().preprocessing(df)
    output_expected = pd.read_csv(f"data/output_expected/{file_name}.csv")
    pd.testing.assert_frame_equal(output, output_expected)
