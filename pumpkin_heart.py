import pygame
import sys
from pumpkin import Pumpkin
from TileMap import TileMap
from healtbar import HealtBar
from bat import Bat


class Pumpkin_Heart:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.tilemap = TileMap(self.screen)
        self.damagetilemap = TileMap(self.screen)
        self.itemtilemap = TileMap(self.screen)

        self.PosTiles()
        self.pumpkin = Pumpkin(self.screen, self)
        self.healthbar = HealtBar(self)
        self.bat = Bat(self.screen, self)

    def PosTiles(self):
        self.tilemap.AddTile('semla.png', 10, 21)
        self.tilemap.AddTile('semla.png', 11, 20)
        self.tilemap.AddTile('semla.png', 10, 20)
        self.tilemap.AddTile('semla.png', 9, 20)
        self.tilemap.AddTile('semla.png', 12, 19)
        self.tilemap.AddTile('semla.png', 11, 19)
        self.tilemap.AddTile('semla.png', 10, 19)
        self.tilemap.AddTile('semla.png', 9, 19)
        self.tilemap.AddTile('semla.png', 8, 19)
        self.tilemap.AddTile('semla.png', 13, 18)
        self.tilemap.AddTile('semla.png', 12, 18)
        self.tilemap.AddTile('semla.png', 11, 18)
        self.tilemap.AddTile('semla.png', 10, 18)
        self.tilemap.AddTile('semla.png', 9, 18)
        self.tilemap.AddTile('semla.png', 8, 18)
        self.tilemap.AddTile('semla.png', 7, 18)
        self.tilemap.AddTile('semla_trova_kamen.png', 14, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 13, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 12, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 11, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 10, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 9, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 8, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 7, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 6, 17)
        self.tilemap.AddTile('semla.png', 28, 21)
        self.tilemap.AddTile('semla.png', 29, 20)
        self.tilemap.AddTile('semla.png', 28, 20)
        self.tilemap.AddTile('semla.png', 27, 20)
        self.tilemap.AddTile('semla.png', 30, 19)
        self.tilemap.AddTile('semla.png', 29, 19)
        self.tilemap.AddTile('semla.png', 28, 19)
        self.tilemap.AddTile('semla.png', 27, 19)
        self.tilemap.AddTile('semla.png', 26, 19)
        self.tilemap.AddTile('semla.png', 31, 18)
        self.tilemap.AddTile('semla.png', 30, 18)
        self.tilemap.AddTile('semla.png', 29, 18)
        self.tilemap.AddTile('semla.png', 28, 18)
        self.tilemap.AddTile('semla.png', 27, 18)
        self.tilemap.AddTile('semla.png', 26, 18)
        self.tilemap.AddTile('semla.png', 25, 18)
        self.tilemap.AddTile('semla_trova_kamen.png', 32, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 31, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 30, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 29, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 28, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 27, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 26, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 25, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 24, 17)
        self.tilemap.AddTile('doska.png', 23, 17)
        self.tilemap.AddTile('doska.png', 22, 17)
        self.tilemap.AddTile('doska.png', 21, 17)
        self.tilemap.AddTile('doska.png', 17, 17)
        self.tilemap.AddTile('doska.png', 16, 17)
        self.tilemap.AddTile('doska.png', 15, 17)
        self.tilemap.AddTile('voda2.png', 5, 17)
        self.tilemap.AddTile('voda.png', 5, 18)
        self.tilemap.AddTile('voda.png', 5, 19)
        self.tilemap.AddTile('voda.png', 5, 20)
        self.tilemap.AddTile('voda.png', 5, 21)

        self.damagetilemap.AddDamageTile('igla.png', 23, 16, 0.5)

        self.itemtilemap.AddItemTile('igla.png', 26, 16,'Sedge')
        self.itemtilemap.AddItemTile('igla.png', 25, 16, 'Sedge')
        self.itemtilemap.AddItemTile('igla.png', 24, 16, 'Sedge')

    def KeyDownHandler(self, event):
        # проверяем что шип не = нан
        if self.pumpkin != None:
            # билдим клавишу
            if event.key == pygame.K_d:
                # можем двиготся в право
                self.pumpkin.isRight = True
                # билдим клавишу
            elif event.key == pygame.K_a:
                # можем двиготся в лево
                self.pumpkin.isLeft = True
            elif event.key == pygame.K_SPACE and not self.pumpkin.isJumping and not self.pumpkin.isFolling:
                self.pumpkin.StartJumping()
            elif event.key == pygame.K_e:
                self.pumpkin.TriggerAction()
            elif event.key == pygame.K_p:
                self.pumpkin.Drop()

    def KeyUpHandler(self, event):
        # проверяем что шип не = нан
        if self.pumpkin != None:
            # проверяем клавишу
            if event.key == pygame.K_d:
                # идем на право
                self.pumpkin.isRight = False
                # проверяем клавишу
            elif event.key == pygame.K_a:
                # идем на лево
                self.pumpkin.isLeft = False
        if event.key == pygame.K_q:
            # можем выходить
            sys.exit()

    def CheckEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # проверка нажатия
            elif event.type == pygame.KEYDOWN:
                self.KeyDownHandler(event)
            elif event.type == pygame.KEYUP:
                self.KeyUpHandler(event)

    def Start(self):
        while True:
            # Обновление экрана (fps)
            self.CheckEvent()
            self.screen.fill((33, 174, 234))

            if self.pumpkin is not None:
                self.pumpkin.update()
                self.pumpkin.Blitme()

                self.healthbar.update()
                self.healthbar.blitme()

                self.bat.Blitme()

            self.tilemap.Blitme()
            self.damagetilemap.Blitme()
            self.itemtilemap.Blitme()

            pygame.display.flip()


if __name__ == '__main__':
    game = Pumpkin_Heart()
    game.Start()
