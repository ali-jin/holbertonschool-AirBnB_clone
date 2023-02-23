import unittest
from models.state import State


class test_place(unittest.TestCase):
    def test_state(self):
        self.assertEqual(State.name, "")
