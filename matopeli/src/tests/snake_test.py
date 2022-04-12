import unittest
from entities.snake import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_snake_lenght_beginning(self):
        self.assertEqual(self.snake.lenght, 1)

    def test_snake_starting_position(self):
        self.assertEqual(self.snake.pos, [(300.0, 300.0)])

    def test_snake_find_head(self):
        self.assertEqual(self.snake.find_head(), (300, 300))

    def test_new_game_resets_lenght(self):
        self.snake.lenght = 3
        self.snake.new_game()
        self.assertEqual(self.snake.lenght, 1)

    def test_new_game_resets_pos(self):
        self.snake.pos = [(330, 360)]
        self.snake.new_game()
        self.assertEqual(self.snake.pos, [(300, 300)])

    def test_new_game_resets_score(self):
        self.snake.score = 3
        self.snake.new_game()
        self.assertEqual(self.snake.score, 0)
