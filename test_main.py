""" I don't know how to deal with that other test file,
so I'm just going to make a new one. """

""" test_main.py
Tests the cipher for correctness. """

import unittest
from input import StringBuilder, restrict_key
from main import processing_main


class CipherTester(unittest.TestCase):
    def encipher(self, case='lower', spaces='strip', newlines='strip', punctuation='strip'):
        """ Utility. """
        s = StringBuilder(self.plaintext,
                          case=case,
                          spaces=spaces,
                          newlines=newlines,
                          punctuation=punctuation)
        return s.encipher(self.key)


class TestSimplestCiphering(CipherTester):
    def setUp(self):
        self.plaintext = "Abcd"
        self.key = "b"

    def test_basic(self):
        self.assertEqual("bcde", self.encipher())

    def test_caps(self):
        self.assertEqual("BCDE", self.encipher(case='upper'))
        self.assertEqual("Bcde", self.encipher(case='replace'))

class TestPunctuatedCiphering(CipherTester):
    def setUp(self):
        self.plaintext = "ab,cd.e!"
        self.key = "a"

    def test_strip(self):
        self.assertEqual("abcde", self.encipher())

    def test_preservation(self):
        self.assertEqual(self.plaintext, self.encipher(punctuation='preserve'))

    def test_replacement(self):
        self.assertEqual(self.plaintext, self.encipher(punctuation='replace'))

class TestHenryCiphering(CipherTester):
    def setUp(self):
        self.plaintext = "Henry, Henry"
        self.key = "a"

    def test_punctuation(self):
        with self.subTest():
            self.assertEqual(self.encipher(punctuation='preserve'),
                             "henry,henry")

        with self.subTest():
            self.assertEqual(self.encipher(punctuation='replace'),
                             "henry,henry")

    def test_capitalization(self):
        ciphertext = self.encipher(case='lower', spaces='preserve', punctuation='preserve')

        with self.subTest():
            self.assertEqual("henry, henry", ciphertext)

        with self.subTest():
            self.assertEqual("henry, henry",
                             self.encipher(case='lower', spaces='preserve', punctuation='preserve'))
    
        with self.subTest():
            self.assertEqual(self.encipher(case='upper'),
                             "HENRYHENRY")

    def test_spaces(self):
        self.assertEqual(self.encipher(spaces="preserve"),
                         "henry henry")

if __name__ == "__main__":
    unittest.main()
