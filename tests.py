import main
import sys
import string
from functools import partial

def test_binary_function(func, *args, log_successes=False, **kwargs):
    """ arguments are pairs of the form ( (a, b), expected_answer ). """
    for (a, b), expected in args:
        outcome = func(a, b, **kwargs)
        if expected != outcome:
            print("'{}'+'{}'='{}' ..! expected '{}'".format(a, b, outcome, expected))
        elif log_successes:
            print("'{}'+'{}'='{}' ... passed".format(a, b, outcome))

test_sum_letters = partial(test_binary_function, main.sum_letters)
test_main = partial(test_binary_function, main.processing_main)

lower_cases = [
        (('a', 'a'), 'a'),
        (('a', 'b'), 'b'),
        (('b', 'a'), 'b'),
        (('b', 'j'), 'k'),
        (('j', 'q'), 'z'),
]

upper_cases = [
        (('A', 'A'), 'A'),
        (('A', 'B'), 'B'),
        (('B', 'A'), 'B'),
        (('B', 'J'), 'K'),
        (('J', 'Q'), 'Z'),
]

words = [
    (("EVERYTHING IS GOOD BUT ALSO BAD", "KEY"),
        "ZCBCRRMLQ MQ QSMN FSD EJCS ZKH"),
    (("", ""),
        ""),
    ]

"""
    (("", ""),
        ""),
    (("", ""),
        ""),
"""


if __name__ == "__main__":
    ls = bool(sys.argv[1]) if len(sys.argv) > 1 else False

    test_sum_letters(*lower_cases, log_successes=ls,
            alphabet=string.ascii_lowercase)
    print()
    test_sum_letters(*upper_cases, log_successes=ls,
            alphabet=string.ascii_uppercase)
    print()
    test_main(*words, log_successes=ls,
            alphabet=string.ascii_uppercase)

