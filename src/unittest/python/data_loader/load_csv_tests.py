"""
This file is used to test the methods located in
load_csv.py. Testing is very important! It ensures
changes made do not change/remove previously expected
functionality from method.

Every test file must end with the word tests.

Every test method must start with test_

A test should not only test what is expected, but
also test what should not occur.

Every test class must take unittest.TestCase as
a parameter
"""
from meter_analysis.data_loader.load_csv import CSVLoader
import unittest


class CSVLoaderTest(unittest.TestCase):

    def test_load_csv_prints_correct_string(self):
        self.assertEqual(
            CSVLoader.load_csv(),
            "hello world!",
            "load_csv did not return 'hello world!'"
        )

    def test_load_csv_does_not_return_empty_string(self):
        self.assertNotEqual(
            CSVLoader.load_csv(),
            "",
            "load_csv was an empty string"
        )
