""" input.py:
Handles the input.

I'm going to implement the CharacterContainer class here.
"""

# Okay, I'm in the weeds and this is just. Not fun to implement!

import sys
import os.path
import argparse

def to_string(txt, open_func=open):
    """ Just something we do. """
    if txt == '-':
        txt = sys.stdin
    try:
        with open_func(txt, 'r') as file:
            output = file.read().strip()
    # TODO: Make sure to account for all of the ways that this could fail.
    except FileNotFoundError:
        output = txt
    return output


parser = argparse.ArgumentParser(description='Vigenere cipher utility.')
parser.set_defaults(
        newlines='preserve',
        spaces='strip',
        case='lower',
        punctuation='strip')

# TODO: Allow stdin by using '-' for plaintext.

# Plaintext: Accepts a string or a file location. 
parser.add_argument('plaintext', type=to_string)

# Key: Accepts a string or a file location.
parser.add_argument('--key', type=to_string, required=True)

# Default options
# Spaces: Strip
# Punctuation: Strip
# Case: Normalize to lowercase.
# New lines: Preserve

# Other options
# Newline options used before space options
parser.add_argument('--strip-newlines',
        action='store_const',
        const='strip',
        dest='newlines')  # All newlines replaced with spaces

spaces = parser.add_mutually_exclusive_group()
spaces.add_argument('--preserve-spaces',
        action='store_const',
        const='preserve',
        dest='spaces')  # Keep spaces

spaces.add_argument('--replace-spaces',
        action='store_const',
        const='replace',
        dest='spaces')  # Include spaces in alphabet

case = parser.add_mutually_exclusive_group()
case.add_argument('--upper-case',
        action='store_const',
        const='upper',
        dest='case')  # Normalize to uppercase

case.add_argument('--preserve-case',
        action='store_const',
        const='preserve',
        dest='case') # Keep capitalization

case.add_argument('--replace-case',
        action='store_const',
        const='replace',
        dest='case') # Include uppercase in alphabet

punctuation = parser.add_mutually_exclusive_group()
punctuation.add_argument('--preserve-punctuation',
        action='store_const',
        const='preserve',
        dest='punctuation')  # Keep punctuation

punctuation.add_argument('--replace-punctuation',
        action='store_const',
        const='replace',
        dest='punctuation')  # Include punctuation in alphabet


# Specify a string of things we want to preserve. Supersedes others.
# Kind of silly, but useful to have these mechanisms in place.
# TODO: Don't know how to do this.
# parser.add_argument('--preserve')  # Remove symbols from plaintext, reinsert
# parser.add_argument('--replace')  # Add symbols to alphabet

"""
Keep mechanism: Characters are stripped out of the plaintext and then reinserted.
Implementation: We'll create two arrays: one with the stripped characters,
    We'll use '' in the blank spots, and something something.
"""

class StringBuilder:
    """ Part of this is the derivation of the alphabet.
    I'm not sure how I'm going to do stuff with `key`. Do I
    process it as well? Do I force the alphabet to include everything
    that `key` has? """
    def __init__(self, plaintext, key, **kwargs):
        # takes a dict:
        # {'spaces', 'newlines', 'case', 'punctuation', 'preserve', 'replace'}
        self.plaintext = plaintext
        self.key = key
        self.alphabet = string.ascii_lowercase

        if kwargs['case'] == 'upper':
            self.alphabet = string.ascii_uppercase
        elif kwargs['case'] == 'replace':
            self.alphabet += string.ascii_uppercase

        if kwargs['spaces']: pass


# Output: prints.
if __name__ == "__main__":
    print(parser.parse_args())
