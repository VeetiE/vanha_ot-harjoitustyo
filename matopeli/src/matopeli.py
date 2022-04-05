
import pygame
import sys
import random

#GLOBAL VARIABLES
SCREEN_W=600
SCREEN_H=600
SCREEN=pygame.display.set_mode((SCREEN_W,SCREEN_H))
LEFT=(-1,0)
RIGHT=(1,0)
DOWN=(0,1)
UP=(0,-1)

snake_block_size=30
grid_width=SCREEN_W/snake_block_size
grid_height=SCREEN_H/snake_block_size
class Loads:
    def __init__(self):
        pass

    def highest_score(self):
        pass


class Snake:
    def __init__(self):
        self.lenght=1
        self.pos=[((SCREEN_W/2), (SCREEN_H/2))]
        self.beginning_pos=[((SCREEN_W/2), (SCREEN_H/2))]
        self.dir=random.choice([UP,DOWN,LEFT,RIGHT])
        self.color=(17,24,47)
        self.score=0
    def find_head(self):
        return self.pos[0]
    
    def move(self):
        current=self.pos[0]
        x,y=self.dir
        new = (((current[0]+(x*snake_block_size))%SCREEN_W), (current[1]+(y*snake_block_size))%SCREEN_H)
        self.pos.insert(0,new)
        if len(self.pos)>self.lenght:
            self.pos.pop()

    def new_game(self):
        self.score=0
        self.lenght=1
        self.pos=self.beginning_pos

    def turn(self, point):
        if self.lenght>1 and (point[0]*-1,point[1]*-1)==self.dir:
            return
        else:
            self.dir=point

    def draw(self, surface):
        for i in self.pos:
            r=pygame.Rect((i[0],i[1]), (snake_block_size,snake_block_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216,228), r,1)


    

def DrawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0,int(grid_width)):
            if (x+y)%2==0:
                r=pygame.Rect((x*snake_block_size,y*snake_block_size),(snake_block_size,snake_block_size))
                pygame.draw.rect(surface,(255,0,0),r)
            else:
                rr=pygame.Rect((x*snake_block_size,y*snake_block_size),(snake_block_size,snake_block_size))
                pygame.draw.rect(surface,(127,127,127),rr)



class Food:
    def __init__(self):
        pass


    def randomize_pos(self):
        pass

    def draw(self):
        pass

    def check_collision(self):
        pass

class SnakeGame:
    def __init__(self) -> None:
        

        pygame.init()
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode((SCREEN_W,SCREEN_H),0,32)

        self.snake=Snake()

        self.surface=pygame.Surface(self.screen.get_size())
        self.surface=self.surface.convert()
        DrawGrid(self.surface)

        self.score_font=pygame.font.SysFont('Ariel', 80)
        self.score_text=self.score_font.render('Score: '+str(self.snake.score), True, (0,0,0))
        self.score_box=self.score_text.get_rect()
        self.game_loop()
    
    def game_loop(self):
        while True:
            self.clock.tick(10)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        self.snake.turn(LEFT)
                    elif event.key==pygame.K_RIGHT:
                        self.snake.turn(RIGHT)
                    elif event.key==pygame.K_UP:
                        self.snake.turn(UP)
                    elif event.key==pygame.K_DOWN:
                        self.snake.turn(DOWN)
            
            
            DrawGrid(self.surface)
            self.snake.move()
            self.snake.draw(self.surface)
            self.screen.blit(self.surface,(0,0))
            self.screen.blit(self.score_text,self.score_box)
            pygame.display.update()
           

SnakeGame()

    
    