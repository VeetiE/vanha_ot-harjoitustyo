import unittest
from matopeli import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake=Snake()

    def test_snake_lenght_beginning(self):
        self.assertEqual(self.snake.lenght,1)

    def test_snake_starting_position(self):
        self.assertEqual(self.snake.pos,[(300.0,300.0)])


    def test_snake_find_head(self):
        self.assertEqual(self.snake.find_head(),(300,300))
        
        