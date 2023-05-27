import pygame
from Tile import Tile
from damagetile import DamageTile
from ItemTile import ItemTile

class TileMap:
    def __init__(self, screen,game, width = 40, height = 40):
        self.width = width
        self.height = height
        self.screen = screen
        self.group = pygame.sprite.Group()
        self.game = game

    def AddTile(self, texture, x, y):
        x = x * self.width
        y = y * self.height
        self.group.add(Tile(self.screen, texture, self.width, self.height, x,y))

    def AddDamageTile(self, texture, x, y, damage):
        x = x * self.width
        y = y * self.height
        self.group.add(DamageTile(self.screen, texture, self.width, self.height, x,y, damage))

    def AddItemTile(self, texture, x, y, name, id):
        x = x * self.width
        y = y * self.height
        self.group.add(ItemTile(self.screen, texture, self.width, self.height, x,y, name, id))

    def AddDroppedItemTile(self, itemTile, x_player, y_player, tilemap):
        new_x = self.Find_x_ByPlayer(x_player)
        new_y = self.Find_y_ByPlayer(tilemap, new_x)

        itemTile.Pos(new_x, new_y)
        self.group.add(itemTile)

    def Find_x_ByPlayer(self, x, lastLeft=0, lastRight=1):
        #print(f"x: {x}, lastleft: {lastLeft}, lastRight: {lastRight}")
        if lastLeft * self.width < x and lastRight * self.width > x:
            return lastRight * self.width
        else:
            return self.Find_x_ByPlayer(x, lastLeft + 1, lastRight + 1)

    def Find_y_ByPlayer(self, hardtilemap, x):
        minY = 1000000000
        for tile in hardtilemap.group.sprites():
            if tile.rect.left == x:
                if tile.rect.top < minY:
                    minY = tile.rect.top
        return minY - 40

    def RemoveItemTile(self, itemTile):
        self.group.remove(itemTile)

    def GetGroup(self):
        return self.group

    def Blitme(self):
        for tile in self.group.sprites():
            tile.Blitme()

    def Update(self):
        self.group.update()

