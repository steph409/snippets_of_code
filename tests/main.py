import airflow

if __name__ == '__main__':
    n = 10
    import pandas as pd

    df = pd.read_csv("XX")
    df_initial = df.copy()

    df.rolling_mean()


    def add_one(a):
        a += 1
        return a


    b = add_one(n)
    print(n, b)

    # airflow_instance = airflow.Airflow()
    # airflow_instance.talk()
# nb = airflow_instance.return_favorite_number()
