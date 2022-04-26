import random
import pygame




class Food:
    def __init__(self):
        self.food_size=30
        self.pos = (0, 0)
        self.color = (102, 205, 170)
        self.randomize_pos()

    def randomize_pos(self):
        self.random_number = random.randint(1, 19)*self.food_size
        self.pos = (self.random_number, self.random_number)

    def draw(self, surface):

        r = pygame.Rect(
            (self.pos[0], self.pos[1]), (self.food_size, self.food_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)


