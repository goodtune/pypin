import os
import pypin
import sys

import unittest

PYTHON_VERSION = tuple(sys.version_info)[:2]


class SimpleTest(unittest.TestCase):

    def setUp(self):
        api_key = os.environ.get('API_KEY', '')
        self.api = pypin.API(api_key=api_key, debug=True)

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    @unittest.skipIf(PYTHON_VERSION < (2, 7), 'Python 2.7 required.')
    def test_list_charges(self):
        charges = self.api.list_charges()
        self.assertIsInstance(charges, dict)
