import re
from typing import Callable


def generator_numbers(text: str):
    pattern = r"[+-]?\b\d+(?:\.\d+)?\b"

    # Collecting all real numbers in the text into the list
    numbers = [float(n) for n in re.findall(pattern, text)]

    for number in numbers:
        yield number


def sum_profit(text: str, func: Callable):
    sum = 0

    for number in func(text):
        sum += number

    return sum


TEST_TEXT = "Some numbers: 3.14, -15.2, 6, 0.001, -2, +3, and 5.0"


def main():
    print(sum_profit(TEST_TEXT, generator_numbers))


if __name__ == "__main__":
    main()
