from Tile import Tile
import pygame

class ItemTile(Tile):
    def __init__(self,screen,texture,width,height,x,y,name):
        super(ItemTile, self).__init__(screen,texture,width,height,x,y)
        self.name = name
        self.isFolling = False
        self.tilemap = None

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
        self.tilemap = tilemap
        print("DropUpdate Started")
        while True:
            endOfUpdate = self.Update()
            self.Blitme()

            if endOfUpdate == True:
                break

        #self.tilemap = None
        func(self, x_player, y_player, tilemap)
        print("DropUpdate Ended")
