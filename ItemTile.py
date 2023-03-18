from Tile import Tile
import pygame
import time

class ItemTile(Tile):
    def __init__(self,screen,texture,width,height,x,y,name,id):
        super(ItemTile, self).__init__(screen,texture,width,height,x,y)
        self.name = name
        self.isFolling = False
        self.tilemap = None
        self.id = id

    def Update(self):
        if not self.IsEndOfFolling():
            self.isFolling = True
        else:
            self.isFolling = False

        if self.isFolling:
            self.rect.y += 1
            print(f"y: {self.rect.y}")
            if self.IsEndOfFolling():
                self.StopFolling()
                return True

        return False

    def IsEndOfFolling(self):
        collision = self.CollideTiles()
        if collision != None and (collision.rect.top + 3 >= self.rect.bottom and collision.rect.top - 3 <= self.rect.bottom):
            print("End of folling")
            return True
        else:
            return False

    def StopFolling(self):
        self.isFolling = False

    def CollideTiles(self):
        collision = pygame.sprite.spritecollideany(self, self.tilemap.group)
        return collision

    def DropUpdate(self, func, x_player, y_player, tilemap):
        #tilemap.game.needToFlip = False
        self.tilemap = tilemap
        print("DropUpdate Started")
        while True:
            time.sleep(0.01)
            endOfUpdate = self.Update()

            self.Blitme()

            #pygame.display.flip()


            if endOfUpdate == True:
                #tilemap.game.needToFlip = True
                break

        #self.tilemap = None
        func(self, x_player, y_player, tilemap)
        print("DropUpdate Ended")
