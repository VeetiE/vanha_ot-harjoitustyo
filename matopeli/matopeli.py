from ast import Pass
from unicodedata import name
from xml.etree.ElementTree import ProcessingInstruction
import pygame
import sys
import tkinter
import sqlite3
import random

class Loads:
    def __init__(self):
        self.name=name
        self.points=points

    def highest_score(self):
        pass
        

class Snake:
    def __init__(self):
        self.lenght=1
        self.pos=[((SCREEN_W/2), (SCREEN_H/2))]
        self.dir=random.choice([UP,DOWN,LEFT,RIGHT])
        self.color=(17,24,47)

        
    
    def move(self):
        


    def draw(self):
        pass



class Food:
    def __init__(self):
        pass


    def randomize_pos(self):
        pass

    def draw(self):
        pass



SCREEN_W=600
SCREEN_H=600

LEFT=(-1,0)
RIGHT=(1,0)
DOWN=(0,1)
UP=(0,-1)


def main():
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_W, screen_height), 0, 32)
