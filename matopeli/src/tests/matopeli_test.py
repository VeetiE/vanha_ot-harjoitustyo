import unittest

from matopeli import SnakeGame


class TestMatopeli(unittest.TestCase):
    def setUp(self):
        self.snake_game=SnakeGame()

    def test_snake_lenght_beginning(self):
        self.assertEqual(self.snake_game.snake.lenght,1)

    def test_snake_starting_position(self):
        self.assertEqual(self.snake_game.snake.pos,(300,300))


    def test_snake_find_head(self):
        self.assertEqual(self.snake_game.snake.find_head(),(300,300))
        
        