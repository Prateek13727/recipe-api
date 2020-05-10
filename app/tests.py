from django.test import TestCase
from app.calc import add, substract


class CalcTests(TestCase):
    def test_add_number(self):
        self.assertEqual(add(3, 8), 11)

    def test_substract_number(self):
        self.assertEqual(substract(5, 11), 6)
