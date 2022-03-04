from utils import log, log_execution


@log_execution
def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    r = add_numbers(209, 3)
    print(f"this is the main. the result is {r}")


class Student:
    def __init__(self, age):
        self.age = age

    def tell_age(self):
        return self.age

    @staticmethod
    def say_hello():
        return "hi"
