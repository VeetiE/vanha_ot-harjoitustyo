from entities.snake import Snake
from entities.food import Food
from UI.Menu import Menu
import pygame
import sys


def DrawGrid(surface):
    snake_block_size = 30
    grid_size = 600/snake_block_size
    for y in range(0, int(grid_size)):
        for x in range(0, int(grid_size)):
            if (x+y) % 2 == 0:
                r = pygame.Rect((x*snake_block_size, y*snake_block_size),
                                (snake_block_size, snake_block_size))
                pygame.draw.rect(surface, (255, 0, 0), r)
            else:
                rr = pygame.Rect(
                    (x*snake_block_size, y*snake_block_size), (snake_block_size, snake_block_size))
                pygame.draw.rect(surface, (127, 127, 127), rr)


class SnakeGame:
    def __init__(self) -> None:
        self.screen_w = 600
        self.screen_h = 600
        self.snake_block_size = 30
        self.playing = False

        self.left = (-1, 0)
        self.right = (1, 0)
        self.down = (0, 1)
        self.up = (0, -1)

        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.screen_w, self.screen_h), 0, 32)

        self.snake = Snake()
        self.food = Food()
        self.menu = Menu()

        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.game_loop()

    def draw(self):

        if self.playing == True:

            DrawGrid(self.surface)
            self.snake.move()
            self.snake.draw(self.surface)
            self.food.draw(self.surface)
            self.score_font = pygame.font.SysFont('Ariel', 80)
            self.score_text = self.score_font.render(
                'Score: '+str(self.snake.score), True, (0, 0, 0))
            self.score_box = self.score_text.get_rect()
            self.screen.blit(self.surface, (0, 0))
            self.screen.blit(self.score_text, self.score_box)
        else:
            self.menu.draw()

        pygame.display.update()

    def game_loop(self):

        while True:
            self.clock.tick(10)
            if self.playing:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.snake.turn(self.left)
                        elif event.key == pygame.K_RIGHT:
                            self.snake.turn(self.right)
                        elif event.key == pygame.K_UP:
                            self.snake.turn(self.up)
                        elif event.key == pygame.K_DOWN:
                            self.snake.turn(self.down)
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.playing = True

            if self.snake.find_head() == self.food.pos:
                self.snake.score += 1
                self.snake.lenght += 1
                self.food.randomize_pos()

            self.draw()


def main():
    SnakeGame()


if __name__ == '__main__':
    main()
