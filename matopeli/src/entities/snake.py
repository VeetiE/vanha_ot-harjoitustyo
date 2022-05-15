import random
import pygame
from database_connection import get_database_connection
from datetime import date


class Snake:
    def __init__(self):
        self.db = get_database_connection()
        self.screen_size = 600
        self.snake_block_size = 30
        self.day = date.today().day
        self.month = date.today().month
        self.year = date.today().year

        self.left = (-1, 0)
        self.right = (1, 0)
        self.down = (0, 1)
        self.up = (0, -1)
        self.lenght = 1
        self.pos = [((self.screen_size/2), (self.screen_size/2))]
        self.beginning_pos = [((self.screen_size/2), (self.screen_size/2))]
        self.dir = random.choice([self.up, self.down, self.left, self.right])
        self.color = (17, 24, 47)
        self.score = 0

    def find_head(self):
        return self.pos[0]

    def move(self):
        current = self.pos[0]
        x, y = self.dir
        new = (((current[0]+(x*self.snake_block_size)) % self.screen_size),
               (current[1]+(y*self.snake_block_size)) % self.screen_size)
        if len(self.pos) > 2 and new in self.pos[2:]:
            self.db.execute(
                f'INSERT INTO Users VALUES ({self.score}, {self.day}, {self.month}, {self.year});')
            self.new_game()
        else:

            self.pos.insert(0, new)
            if len(self.pos) > self.lenght:
                self.pos.pop()

    def new_game(self):
        self.lenght = 1
        self.score = 0

        self.pos = [(self.screen_size/2, self.screen_size/2)]
        self.dir = random.choice([self.up, self.down, self.left, self.right])

    def turn(self, point):
        if self.lenght > 1 and (point[0]*-1, point[1]*-1) == self.dir:
            return
        else:
            self.dir = point

    def draw(self, surface):
        for i in self.pos:
            r = pygame.Rect(
                (i[0], i[1]), (self.snake_block_size, self.snake_block_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)
