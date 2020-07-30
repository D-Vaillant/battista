"""

Two separate problems: Input and the processing. I'll figure out what I want the interface to be ahead of time.

INPUT -> dict with whatever information I need
{"plaintext":"", "key":None}
"""
import sys
import string
from functools import partial
from collections import Counter
import itertools


def processing_main(plaintext, key, alphabet=string.ascii_letters, preserved=None):
    if plaintext == "":
        print("No text entered.")
        sys.exit(1)
    if key is None:
        # Either prompt user, or:
        raise Exception("Need to pass in a key.")

    """ Zip the two together, use it to calculate new entry in output. """
    """ Then starmap it. """

    if preserved is None: preserved = []
    ciphertext_arr = itertools.starmap(
                       partial(sum_letters, alphabet=alphabet, preserve=preserved),
                       zip(plaintext, itertools.cycle(key)))
    return ''.join([_ for _ in ciphertext_arr])


    # I can do an array of indices, and build it up.
    # "I AM HERE" -> [1, 4]
    # "IMBACK" -> []
    # "    ff " -> [0, 1, 2, 3, 6]
""" How to deal with spaces? Either:
        * strip em, either throw out or put back in later
        * consider them as characters
        * strip em, sprinkle in random spaces

Stripping them means I deal with them on a different level.
"""

# def classify_char(a):
#     """ There's different kinds of characters. """
#     # could be an enum
#     num = ord(a)
#     if ord('a') <= num or num <= ord('z'):
#         return "lowercase"
#     if ord('A') <= num or num <= ord('Z'):
#         return "uppercase"


# def classify_str(s):
#       """ We want to know a global state about the whole string
#       in some of our "per-letter" transforms. """
#       out = dict()
#       classifications = [classify_char(c) for c in s]
#       counts = Counter(classifications)
#       # If everything is lowercase.



def validate_input(input, alphabet):
    for letter in input:
        if letter in alphabet: continue
        else:
            raise Exception("Plaintext must be contained in the alphabet.")
    return True


def sum_letters(a, b, alphabet=string.ascii_letters, preserve=[]):
    """ Given two letters, returns their "sum".
    alphabet has to be something we can access via index.
    If we enter None, we'll just get None. Error handle that later. """

    """ [33, 46] U [58, 64] U [91, 94] U [123, 126] : punctuation
            Some are more or less useful.
        [48, 57] : numerals
        [65, 90]: uppercase letters
        [97, 122]: lowercase letters
    """

    # If our character isn't in the alphabet, we either strip it or preserve it.
    # To that end, we pass a list of characters we want to preserve.
    # If it's in that list, keep it. Otherwise, return the empty string.
    if a in preserve: return a
    if a not in alphabet: return ''
    # Probably don't need this.
    baseline = 0
    offset = baseline + (alphabet.index(a) + alphabet.index(b) - 2*baseline)%len(alphabet)

    return alphabet[offset]
