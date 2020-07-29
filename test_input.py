""" test_input.py
A suite of tests for input.py. """

import random
import string
import input
import unittest
import tempfile

""" Cases:
Plaintext: Get a string, get a file.
Key: Get a string, get a file.

"""
def create_random_string():
    return ''.join(random.choices(string.ascii_letters,
                          k=random.randrange(5, 20)))


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = input.parser

    def test_to_string_file(self):
        # Make up some random stuff.
        file_name = create_random_string()
        file_contents = create_random_string()
        # Create fake file.
        fo, location = tempfile.mkstemp()
        with open(location, 'w') as f:
            f.write(file_contents)
        self.assertEqual(file_contents, input.to_string(location))

    def test_to_string_text(self):
        a = create_random_string()
        self.assertEqual(a, input.to_string(a))

    def test_spaces(self):
        pass

    def test_case(self):
        pass

    def test_punctuation(self):
        pass

if __name__ == "__main__":
    unittest.main()
