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

""" A class makes the most sense for this. """
class CipherProcessor:
    def __init__(self, plaintext, key, alphabet, **options):
        self.plaintext = plaintext
        self.key = itertools.cycle(key)
        self.alphabet = alphabet
        self.options = options

        self._ciphertext = ""

    @property
    def ciphertext(self):
        return self._ciphertext


    """ devise a sequence of functions that wrap around like an onion,
    stripping the string down to the simplified alphabet and then
    building it back up again """
    def add_strands(self):
        ciphertext_arr = itertools.starmap(
                           partial(sum_letters, alphabet=self.alphabet),
                           zip(self.plaintext, self.key))
        return ''.join([_ for _ in ciphertext_arr])


def processing_main(plaintext, key, alphabet=string.ascii_letters):
    if plaintext == "":
        print("No text entered.")
        sys.exit(1)
    if key is None:
        # Either prompt user, or:
        raise Exception("Need to pass in a key.")

    """ Zip the two together, use it to calculate new entry in output. """
    """ Then starmap it. """

    C = CipherProcessor(plaintext, key, alphabet)
    return C.add_strands()


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


def sum_letters(a, b, alphabet=string.ascii_letters):
    """ Given two letters, returns their "sum".
    mod_length means that we have more than just lowercase/uppercase. """

    """ [33, 46] U [58, 64] U [91, 94] U [123, 126] : punctuation
            Some are more or less useful.
        [48, 57] : numerals
        [65, 90]: uppercase letters
        [97, 122]: lowercase letters
    """
    # This way, I can break it up into different alphabets and have it work.
    baseline = 0
    offset = baseline + (alphabet.index(a) + alphabet.index(b) - 2*baseline)%len(alphabet)
    return alphabet[offset]
