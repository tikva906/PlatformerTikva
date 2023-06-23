import pygame
from pygame.sprite import Sprite
from pygame.rect import Rect

class Bat(Sprite):
    tasks = {1: # номер задания
                 {1: 2} #   ключ - айди предметра, значение - это кол-во, которое надо принести
             }
    currenttask = 1
    def __init__(self,screen, game, handler = None):
        super().__init__()
        self.Screen = screen
        self.ScreenRect = self.Screen.get_rect()
        self.image = pygame.image.load("Images/monstr.png")
        # Получить сетку этой картинки
        self.rect = self.image.get_rect()
        self.Spawn()
        self.tilemap = game.tilemap
        self.game = game
        self.inventory = []
        self.handler = handler

        self.count = len(self.game.itemtilemap.group.sprites()) # TODO могут быть не только нужные объекты



    def Spawn(self):
        self.rect.x = 230
        self.rect.y = 630


    def Blitme(self):
        self.Screen.blit(self.image,self.rect)

    def AddToInventory(self, item):
        self.inventory.append(item)

        if len(self.inventory) >= self.count:
            if self.handler != None:
                self.handler()





