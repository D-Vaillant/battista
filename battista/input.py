""" input.py:
Handles the input.

I'm going to implement the CharacterContainer class here.
"""

# Okay, I'm in the weeds and this is just. Not fun to implement!

from main import processing_main
import string
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
    def __init__(self, plaintext, key="", **kwargs):
        # takes a dict:
        # {'spaces', 'newlines', 'case', 'punctuation', 'preserve', 'replace'}
        # case : lower | upper | replace
        # spaces : strip | preserve | replace
        # newlines : preserve | strip
        # punctuation: strip | replace | preserve
        self.plaintext = plaintext
        self.preserved = []

        # Enforce keyword arguments.
        kwargs['case'] = kwargs.get('case', 'lower')
        self.caps = kwargs['case']
        if kwargs['case'] == 'upper':
            self.plaintext = self.plaintext.upper()
            self.alphabet = string.ascii_uppercase
        elif kwargs['case'] == 'lower':
            self.plaintext = self.plaintext.lower()
            self.alphabet = string.ascii_lowercase
        elif kwargs['case'] == 'replace':
            self.alphabet = string.ascii_letters

        kwargs['newlines'] = kwargs.get('newlines', 'preserve')
        if kwargs['newlines'] == 'strip':
            self.plaintext = self.plaintext.replace('\n', ' ')
        else:
            self.preserved += ['\n']

        kwargs['spaces'] = kwargs.get('spaces', 'strip')
        if kwargs['spaces'] == 'strip':
            self.plaintext = self.plaintext.replace(' ', '')
        elif kwargs['spaces'] == 'replace':
            self.alphabet += ' '
        elif kwargs['spaces'] == 'preserve':
            self.preserved += [' ']

        kwargs['punctuation'] = kwargs.get('punctuation', 'strip')
        if kwargs['punctuation'] == 'strip':
            pass
        elif kwargs['punctuation'] == 'preserve':
            self.preserved += string.punctuation
        elif kwargs['punctuation'] == 'replace':
            self.alphabet += string.punctuation

    def __str__(self):
        return "Plaintext: {}".format(self.plaintext)

    def encipher(self, key):
        """ Given a key, returns the ciphertext. """
        if self.caps == 'lower':
            key = key.lower()
        elif self.caps == 'upper':
            key = key.upper()
        key = filter(lambda x: x in self.alphabet, key)
        return processing_main(self.plaintext, key, alphabet=self.alphabet, preserved=self.preserved)

def restrict_key(k, alphabet):
    return filter(lambda x: x in alphabet, k)
    

def initialize_parser():
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
    parser.add_argument('--strip-newlines',
            action='store_const',
            const='strip',
            dest='newlines')  # All newlines replaced with spaces
    # Spaces
    spaces = parser.add_mutually_exclusive_group()
    spaces.add_argument('--strip-spaces',
            action='store_const',
            const='strip',
            dest='spaces')  # Remove spaces
    spaces.add_argument('--preserve-spaces',
            action='store_const',
            const='preserve',
            dest='spaces')  # Keep spaces
    spaces.add_argument('--replace-spaces',
            action='store_const',
            const='replace',
            dest='spaces')  # Include spaces in alphabet
    # Capitalization
    case = parser.add_mutually_exclusive_group()
    case.add_argument('--lower-case',
            action='store_const',
            const='lower',
            dest='case')  # Normalize to uppercase
    case.add_argument('--upper-case',
            action='store_const',
            const='upper',
            dest='case')  # Normalize to uppercase
    case.add_argument('--replace-case',
            action='store_const',
            const='replace',
            dest='case') # Include uppercase in alphabet
    # Punctuation
    punctuation = parser.add_mutually_exclusive_group()
    punctuation.add_argument('--strip-punctuation',
            action='store_const',
            const='strip',
            dest='punctuation')  # Keep punctuation
    punctuation.add_argument('--preserve-punctuation',
            action='store_const',
            const='preserve',
            dest='punctuation')  # Keep punctuation
    punctuation.add_argument('--replace-punctuation',
            action='store_const',
            const='replace',
            dest='punctuation')  # Include punctuation in alphabet

    return parser


# Output: prints.
if __name__ == "__main__":
    parser = initialize_parser()
    p = parser.parse_args()
    s = StringBuilder(p.plaintext,
                      case=p.case,
                      spaces=p.spaces,
                      newlines=p.newlines,
                      punctuation=p.punctuation)
    k = restrict_key(p.key, s.alphabet)
    ciphertext = processing_main(s.plaintext, k, s.alphabet)
    print(ciphertext)
