from pygame.sprite import Sprite
import pygame

class Button(Sprite):
    def __init__(self, name, style, size, text, antialias, txtColorCort, backColorCort, game):
        super().__init__()
        self.screen = game.screen
        self.name = name
        self.game = game
        self.antialias = antialias
        self.txtColorCort = txtColorCort
        self.backColorCort = backColorCort
        self.style = style
        self.size = size
        self.SetText(text)

    def SetText(self, text):
        font = pygame.font.SysFont(self.style, self.size)
        self.btn_text = font.render(text, self.antialias, self.txtColorCort, self.backColorCort)
        self.rect = self.btn_text.get_rect()

    def update(self):
        pass

    def CheckButtonClick(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.game.InvokeBtnEvent(self.name)

    def blitme(self):
        self.screen.blit(self.btn_text, self.rect)