import pygame
from pygame.sprite import Sprite

class Tile(Sprite):
    def __init__(self,screen, texture,width,height,x,y):
        super().__init__()
        self.Screen = screen
        self.ScreenRect = self.Screen.get_rect()
        self.image = self.LoadImage(texture,width,height)
        # Получить сетку этой картинки
        self.rect = self.image.get_rect()
        self.Pos(x, y)

    def Pos(self,x,y):
        self.rect.left = x
        self.rect.top = y

    def Blitme(self):
        self.Screen.blit(self.image,self.rect)

    def update(self):
        pass

    def LoadImage(self, texture, width, height):
        image = pygame.image.load(f"Images/{texture}")
        image = pygame.transform.scale(image, (width, height))
        return image
