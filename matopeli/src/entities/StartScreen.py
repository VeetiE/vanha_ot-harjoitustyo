
import pygame ,sys
from SnakeGame import SnakeGame
screen=pygame.display.set_mode((600,600))
class Button():
    def __init__(self, x, y, image, scale):
        width=image.get_width()
        height=image.get_height()
        self.image=pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.click=False
        
    


    def draw(self):
        button_action=False
        mouse_pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]==1 and self.click==False:
                self.click=True
                self.button_action==True
            if pygame.mouse.get_pressed()[0]==0:
                self.click=False
        screen.blit(self.image, (self.rect.x,self.rect.y))
        return button_action

class MainScreen():
    def __init__(self) -> None:
    
        self.play_img=pygame.image.load('assets/Play.png')
        self.load_img=pygame.image.load('assets/Load.png')
        self.exit_img=pygame.image.load('assets/Quit.png')

        self.play_button=Button(200,200,self.play_img, 0.3)
        self.quit_button=Button(200,300,self.exit_img,0.3)

        self.MainLoop()

    def MainLoop(self):
        while True:
            screen.fill((0,0,0))
            if self.play_button.draw()==True:
                SnakeGame()
            self.quit_button.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

MainScreen()


