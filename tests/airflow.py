class Airflow:
    def talk(self):
        print("I AM AIRFLOW")

    @staticmethod
    def return_favorite_number():
        return 42


def calculate_square(number: int) -> int:
    if number >= 0:
        return number * number
    return "i don't know the answer"
