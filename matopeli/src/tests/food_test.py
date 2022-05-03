import unittest
from entities.food import Food


class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food()

    def test_pos_randomizer_works(self):
        first_pos = self.food.pos
        second_pos = self.food.randomize_pos()
        self.assertNotEqual(first_pos, second_pos)
