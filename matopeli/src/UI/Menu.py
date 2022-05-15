import pygame
from random import randint
from database_connection import get_database_connection
class Menu:
    def __init__(self) -> None:
        self.db=get_database_connection()
        self.highscore=self.db.execute('SELECT score FROM Users ORDER BY score DESC LIMIT 1;').fetchall()
        self.date=self.db.execute('SELECT day, month, year FROM Users ORDER BY score DESC LIMIT 1').fetchall()
        self.screen=pygame.display.set_mode((600,600),0,32)
        self.screen.fill((0,0,0))
        self.font = pygame.font.SysFont('Time New Roman', 60)
        #Title Text
        self.title = self.font.render('SNAKE', False, (0,255,0))
        self.titleRect = self.title.get_rect()
        self.titleRect.center = (600//2 , 100)
        
        
        #High Score Text
        self.high = self.font.render('High Score: ' + f'{self.highscore[0][0]}', False, (255,0,255))

        self.highRect = self.high.get_rect()
        self.highRect.center = (600//2, 600//2)

        #Date Text
        
        self.date = self.font.render(f'Date: {self.date[0][0]}/{self.date[0][1]}/{self.date[0][2]}', False, (255,0,255))
        self.dateRect = self.high.get_rect()
        self.dateRect.center = (600//2, 600-200)
        
        
        #Start Text
        self.start = self.font.render('Press Space to Start', False, ((randint(0,255),randint(0,255),randint(0,255))))
        self.startRect = self.start.get_rect()
        self.startRect.center = (600//2 , 600 - 50)

    def draw(self):
        self.screen.blit(self.title, self.titleRect)
        self.screen.blit(self.date, self.dateRect)
        self.screen.blit(self.high, self.highRect)
        self.screen.blit(self.start, self.startRect)