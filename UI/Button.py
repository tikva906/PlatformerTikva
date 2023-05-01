from pygame.sprite import Sprite
import pygame

class Button(Sprite):
    def __init__(self, name, style, size, text, antialias, txtColorCort, backColorCort, game):
        super().__init__()
        self.screen = game.screen
        self.name = name
        self.game = game

        self.initialize(style, size, text, antialias, txtColorCort, backColorCort)

    def initialize(self, style, size, text, antialias, txtColorCort, backColorCort):
        font = pygame.font.SysFont(style, size)
        self.btn_text = font.render(text, antialias, txtColorCort, backColorCort)
        self.rect = self.btn_text.get_rect()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.CheckButtonClick()

    def CheckButtonClick(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.game.InvokeBtnEvent(self.name)

    def blitme(self):
        self.screen.blit(self.btn_text, self.rect)