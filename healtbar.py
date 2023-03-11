from pygame.rect import Rect
import pygame
class HealtBar:
    def __init__(self, game):
        self.game = game
        self.decor = pygame.image.load("Images/healfbar.png")
        self.decorRect = self.decor.get_rect()
        self.healthbar = Rect(0,0,200,34) # как создается рект, точно ли так?
        self.PosHealthBar()
        self.healthbar.center = self.decorRect.center
        self.staticbar = Rect(0,0,200,34)
        self.staticbar.center = self.healthbar.center

    def PosHealthBar(self):
        self.decorRect.x = 30
        self.decorRect.y = 30

    def update(self):
        health = self.game.pumpkin.health
        self.healthbar.width = health * 2

    def blitme(self):
        # правильно отрисовал рект с нужным цветом
        pygame.draw.rect(self.game.screen,(9,1,74), self.staticbar)
        pygame.draw.rect(self.game.screen,(182,39,49), self.healthbar)
        self.game.screen.blit(self.decor, self.decorRect)
