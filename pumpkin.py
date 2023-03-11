import pygame
from pygame.sprite import Sprite
from pygame.rect import Rect
import threading

class Pumpkin(Sprite):
    def __init__(self,screen, game):
        super().__init__()
        self.Screen = screen
        self.ScreenRect = self.Screen.get_rect()
        self.image = pygame.image.load("Images/pumpkin.png")
        # Получить сетку этой картинки
        self.rect = self.image.get_rect()
        self.Spawn()
        self.tilemap = game.tilemap
        self.game = game
        self.damagetilemap = game.damagetilemap
        self.lastDirection = 1 # -1 - влево, 1 - вправо

    def SetItemsRect(self):
        firstItemsRect = self.itemsRect[0]
        secondItemsRect = self.itemsRect[1]

        firstItemsRect.left = self.rect.left
        secondItemsRect.right = self.rect.right

        firstItemsRect.bottom = self.rect.top
        secondItemsRect.bottom = self.rect.top


    def Spawn(self):
        self.health = 100
        self.rect.x = 200
        self.rect.y = 100
        self.isRight = False
        self.isLeft = False
        self.isJumping = False
        self.isFolling = False
        self.y_StartJumping = self.rect.y
        self.inventory = []
        self.itemsRect = (Rect(0, 0, self.rect.width // 3, self.rect.height // 2),
                          Rect(0, 0, self.rect.width // 3, self.rect.height // 2))
        self.SetItemsRect()

    def Blitme(self):
        self.Screen.blit(self.image,self.rect)

    def TriggerAction(self):
        self.TryAddToInventory()

    def TryAddToInventory(self):
        collision = pygame.sprite.spritecollideany(self, self.game.itemtilemap.group)

        if collision != None:
            self.AddToInventory(collision)

    def AddToInventory(self, item):
        if len(self.inventory) <= 1:
            self.inventory.append(item)
            self.game.itemtilemap.RemoveItemTile(item)


    def update(self):
        # Необходимо для того, чтобы персонаж падал вниз, когда не касается полаы
        #if not self.IsEndOfFolling() and not self.isFolling:
        #    self.StartFolling()
        #    print('начал падение')
        #print(f'isFolling: {self.isFolling}')
        self.CheckDamage()

        if self.isRight == True:
            self.lastDirection = 1
            #добавляем 1
            self.rect.x += 1
            self.itemsRect[0].x += 1
            self.itemsRect[1].x += 1
            #идем на лево

        if self.isLeft == True:
            self.lastDirection = -1
            #вычитаем 1
            self.rect.x -= 1
            self.itemsRect[0].x -= 1
            self.itemsRect[1].x -= 1

        if self.isJumping == True:
            self.rect.y -= 1
            self.itemsRect[0].y -= 1
            self.itemsRect[1].y -= 1

            if self.IsEndOfJumping(150):
                self.StopJumping()
                self.StartFolling()


        if not self.isJumping and self.isFolling:
            self.rect.y += 1
            self.itemsRect[0].y += 1
            self.itemsRect[1].y += 1
            if self.IsEndOfFolling():
                self.StopFolling()


        if not self.IsEndOfFolling():
            self.isFolling = True
        else:
            self.isFolling = False

        for i in range(len(self.inventory)):
            self.inventory[i].rect.center = self.itemsRect[i].center
            self.inventory[i].Blitme()

        if self.rect.top > self.game.screen.get_rect().height:
            self.Damage(3)


    def StartJumping(self):
        self.isJumping = True
        self.y_StartJumping = self.rect.y

    def StartFolling(self):
        self.isFolling = True


    def IsEndOfJumping(self, maxHeight):
        collision = self.CollideTiles()
        if collision != None or self.y_StartJumping - self.rect.y >= maxHeight:
            return True
        else:
            return False

    def IsEndOfFolling(self):
        collision = self.CollideTiles()
        if collision != None and (collision.rect.top + 3 >= self.rect.bottom and collision.rect.top - 3 <= self.rect.bottom):
            return True
        else:
            return False

    def CollideTiles(self):
        collision = pygame.sprite.spritecollideany(self, self.tilemap.group)
        return collision

    def CheckDamage(self):
        collision = pygame.sprite.spritecollideany(self, self.damagetilemap.group)

        if collision != None and self.health > 0:
           self.Damage(collision.damage)

    def Damage(self, damage):
        if self.health - damage < 0:
            self.health = 0
        else:
            self.health -= damage

        if self.health == 0:
            self.Death()

    def Death(self):
        self.Spawn()

    def StopJumping(self):
        self.isJumping = False

    def StopFolling(self):
        self.isFolling = False

    def Drop(self):
        if not self.TryGiveItemToBat():
            if len(self.inventory) > 0:
                item = self.inventory[-1]

                x_player = self.rect.left
                y_player = self.rect.bottom

                thr1 = threading.Thread(target=item.DropUpdate, args=(self.game.itemtilemap.AddDroppedItemTile, x_player, y_player, self.tilemap))
                thr1.start()

                #self.game.itemtilemap.AddDroppedItemTile(item, self)

                del self.inventory[-1]

    def TryGiveItemToBat(self):
        return False

