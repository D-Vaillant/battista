""" test_input.py
A suite of tests for input.py. """

import random
import string
from input import StringBuilder, to_string, parser
import unittest
import tempfile

""" Cases:
Plaintext: Get a string, get a file.
Key: Get a string, get a file.

"""
def create_random_string(alphabet=string.ascii_letters):
    return ''.join(random.choices(alphabet,
                          k=random.randrange(80, 100)))


class TestGeneralUtilities(unittest.TestCase):
    def setUp(self):
        self.parser = parser

    def test_to_string_file(self):
        # Make up some random stuff.
        file_name = create_random_string()
        file_contents = create_random_string()
        # Create fake file.
        fo, location = tempfile.mkstemp()
        with open(location, 'w') as f:
            f.write(file_contents)
        self.assertEqual(file_contents, to_string(location))

    def test_to_string_text(self):
        a = create_random_string()
        self.assertEqual(a, to_string(a))


class TestStringBuilder(unittest.TestCase):
    def setUp(self):
        pass

    def test_capitalization(self):
        input_string = create_random_string(alphabet=string.ascii_letters)

        self.assertEqual(input_string.lower(),
                         StringBuilder(input_string, "").plaintext)
        self.assertEqual(string.ascii_lowercase,
                         StringBuilder(input_string, "").alphabet)

        self.assertEqual(input_string.lower(),
                         StringBuilder(input_string, "", case='lower').plaintext)
        self.assertEqual(string.ascii_lowercase,
                         StringBuilder(input_string, "", case='lower').alphabet)

        self.assertEqual(input_string.upper(),
                         StringBuilder(input_string, "", case='upper').plaintext)
        self.assertEqual(string.ascii_uppercase,
                         StringBuilder(input_string, "", case='upper').alphabet)

        self.assertEqual(input_string,
                        StringBuilder(input_string, "", case='replace').plaintext)
        self.assertEqual(string.ascii_letters,
                        StringBuilder(input_string, "", case='replace').alphabet)


    def test_newlines(self):
        input_string = list(create_random_string(alphabet=string.ascii_lowercase))
        input_string[random.randrange(1, 3)] = '\n'
        input_string[random.randrange(4, len(input_string))] = '\n'
        input_string = ''.join(input_string)

        self.assertEqual(input_string,
                         StringBuilder(input_string, "").plaintext)
        self.assertEqual(['\n'],
                         StringBuilder(input_string, "").preserved)

        self.assertEqual(input_string,
                         StringBuilder(input_string, "", newlines='preserve').plaintext)
        self.assertEqual(['\n'],
                         StringBuilder(input_string, "", newlines='preserve').preserved)

        self.assertEqual(input_string.replace('\n', ' '),
                        StringBuilder(input_string, "", newlines='strip', spaces='preserve').plaintext)
        self.assertEqual(input_string.replace('\n', ''),
                        StringBuilder(input_string, "", newlines='strip').plaintext)
        self.assertEqual([],
                        StringBuilder(input_string, "", newlines='strip').preserved)


    def test_spaces(self):
        input_string = list(create_random_string(alphabet=string.ascii_lowercase+string.whitespace))
        input_string[random.randrange(1, 3)] = ' '
        input_string[random.randrange(4, len(input_string))] = ' '
        input_string = ''.join(input_string)

        self.assertEqual(input_string.replace(' ', ''),
                         StringBuilder(input_string, "").plaintext)

        self.assertEqual(input_string.replace(' ', ''),
                         StringBuilder(input_string, "", spaces='strip').plaintext)

        self.assertEqual(input_string,
                         StringBuilder(input_string, "", newlines='preserve', spaces='replace').plaintext)
        self.assertEqual(string.ascii_lowercase + ' ',
                         StringBuilder(input_string, "", newlines='preserve', spaces='replace').alphabet)


if __name__ == "__main__":
    unittest.main()
