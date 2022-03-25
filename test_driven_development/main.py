import logging
import re


def add(input: str = None) -> str:
    '''adds numbers from a string'''
    if not isinstance(input, str):
        raise TypeError(f"The {input=} is of incorrect type")
    logging.info(f"received string value {input}")
    if not re.match("^[0-9,\n]*$", input):
        raise ValueError(f"The {input=} is not valid")

    if not input: # == "":
        return "0"

    return str(sum([int(i) for i in re.split(r",|\n", input)]))
