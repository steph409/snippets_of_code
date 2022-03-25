import pytest

from main import add


def test_tautology():
    assert True == True


def test_add_return_string():
    assert isinstance(add("22,1"), str)


@pytest.mark.parametrize("arg", ["hello", "22,hello", "hello,22", " ", "22, 1", "175,\n35"])
def test_add_return_value_error(arg):
    with pytest.raises(ValueError):
        add(arg)


def test_add_return_type_error():
    """
    check type error raised
    """
    with pytest.raises(TypeError):
        add(0)



@pytest.mark.parametrize("arg,out", [("22", "22"), ("", "0"), ("22,1", "23"), ("1\n2,3", "6")])
def test_add_return_sum(arg, out):
    assert add(arg) == out
