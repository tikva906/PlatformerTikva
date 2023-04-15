import pygame

from pumpkin_heart import *

class DrawMap:
    def __init__(self, level, game, loadLevel=False):
        self.game = game
        self.level = level
        self.tilemap = game.tilemap
        self.damagetilemap = game.damagetilemap
        self.itemtilemap = game.itemtilemap

        if loadLevel == False:
            self.PosTiles()
        else:
            self.LoadLevel(level)

    def PosTiles(self):
        self.tilemap.AddTile('semla.png', 10, 21)
        self.tilemap.AddTile('voda.png', 5, 21)
        self.tilemap.AddTile('semla.png',7,16)

        self.damagetilemap.AddDamageTile('igla.png', 23, 16, 0.5)

        self.itemtilemap.AddItemTile('igla.png', 26, 16, 'Sedge', 1)
        self.itemtilemap.AddItemTile('igla.png', 25, 16, 'Sedge', 1)
        self.itemtilemap.AddItemTile('igla.png', 24, 16, 'Sedge', 1)

    def LoadLevel(self, level):
        self.game.LoadLevel(level)

    def ShowLevel(self):
        self.game.Start()

    def SaveLevel(self):
        ser = SerializationJson.SerializationJson()
        self.game.SaveMap(self.level, ser.Serialize(self.tilemap, self.itemtilemap, self.damagetilemap))


if __name__ == "__main__":
    level = input("ВВедите название уровня: ")

    loadLevel = input("Вы подгружаете уровень (y,n): ")

    if (loadLevel == "y"):
        game = Pumpkin_Heart("draw")
        dm = DrawMap(level, game, True)
        dm.ShowLevel()

    else:
        needToSave = input("Need to save level (y,n): ")

        game = Pumpkin_Heart("draw")
        dm = DrawMap(level, game)

        if (needToSave == "y"):
            dm.SaveLevel()

        dm.ShowLevel()





