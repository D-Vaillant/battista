""" input.py:
Handles the input.

I'm going to implement the CharacterContainer class here.
"""

import os.path
import argparse

parser = argparse.ArgumentParser(description='Vigenere cipher utility.')

# TODO: Allow stdin by using '-' for plaintext.

# Plaintext: Accepts a string or a file location. 
parser.add_argument('plaintext')

# Key: Accepts a string or a file location.
parser.add_argument('--key')

# Default options
# Spaces: Strip
# Punctuation: Strip
# Case: Normalize to lowercase.
# New lines: Preserve

# Other options
# Newline options used before space options
parser.add_argument('--strip-newlines')  # All newlines replaced with spaces

parser.add_argument('--preserve-spaces')  # Keep spaces
parser.add_argument('--replace-spaces')  # Include spaces in alphabet

parser.add_argument('--upper-case')  # Normalize to uppercase
parser.add_argument('--preserve-case')  # Keep capitalization
parser.add_argument('--replace-case')  # Include uppercase in alphabet

parser.add_argument('--preserve-punctuation')  # Keep punctuation
parser.add_argument('--replace-punctuation')  # Include punctuation in alphabet

# TODO: Could reevaluate how I want this handled.

# Specify a string of things we want to preserve. Supersedes others.
# Kind of silly, but useful to have these mechanisms in place.
parser.add_argument('--preserve')  # Remove symbols from plaintext, reinsert
parser.add_argument('--replace')  # Add symbols to alphabet

"""
Keep mechanism: Characters are stripped out of the plaintext and then reinserted.
Implementation: We'll create two arrays: one with the stripped characters,
    We'll use '' in the blank spots, and something something.
"""

def to_string(txt):
    try:
        with open(txt, 'r') as file:
            output = txt.read()
    # TODO: Make sure to account for all of the ways that this could fail.
    except FileNotFoundError:
        output = txt
    return output


class StringBuilder:
    def __init__(self, plaintext, key, **kwargs):
        pass

# Output: prints.
