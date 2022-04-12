import random
import pygame
from snake import Snake


class Food:
    def __init__(self):
        self.snake = Snake()

        self.pos = (0, 0)
        self.color = (102, 205, 170)
        self.snake = Snake()
        self.randomize_pos()

    def randomize_pos(self):
        self.random_number = random.randint(1, 19)*self.snake.snake_block_size
        self.pos = (self.random_number, self.random_number)

    def draw(self, surface):

        r = pygame.Rect(
            (self.pos[0], self.pos[1]), (self.snake.snake_block_size, self.snake.snake_block_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)
