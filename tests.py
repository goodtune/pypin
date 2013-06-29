import os
import pypin

from unittest import TestCase

class SimpleTest(TestCase):

    def setUp(self):
        api_key = os.environ.get('API_KEY', '')
        self.api = pypin.API(api_key=api_key, debug=True)

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_list_charges(self):
        charges = self.api.list_charges()
        self.assertIsInstance(charges, dict)
