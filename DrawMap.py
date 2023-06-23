import pygame

from pumpkin_heart import *

class DrawMap:
    def __init__(self, level, game, loadLevel=False):
        self.game = game
        self.game.level = level
        self.level = level
        self.tilemap = game.tilemap
        self.damagetilemap = game.damagetilemap
        self.itemtilemap = game.itemtilemap

        if loadLevel == False:
            self.PosTiles()
        else:
            self.LoadLevel(level)

    def PosTiles(self):
        self.tilemap.AddTile('semla_trova_kamen.png',6,17)
        self.tilemap.AddTile('semla.png', 6, 18)
        self.tilemap.AddTile('semla.png', 6, 19)
        self.tilemap.AddTile('semla.png', 6, 20)
        self.tilemap.AddTile('semla.png', 6, 21)
        self.tilemap.AddTile('semla_trova_kamen.png', 7, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 8, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 9, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 10, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 11, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 12, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 13, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 14, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 15, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 16, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 17, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 18, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 19, 17)
        self.tilemap.AddTile('semla_trova_kamen.png', 20, 17)
        self.tilemap.AddTile('semla.png', 7, 18)
        self.tilemap.AddTile('semla.png', 7, 19)
        self.tilemap.AddTile('semla.png', 7, 20)
        self.tilemap.AddTile('semla.png', 7, 21)
        self.tilemap.AddTile('semla.png', 8, 18)
        self.tilemap.AddTile('semla.png', 8, 19)
        self.tilemap.AddTile('semla.png', 8, 20)
        self.tilemap.AddTile('semla.png', 8, 21)
        self.tilemap.AddTile('semla.png', 9, 18)
        self.tilemap.AddTile('semla.png', 9, 19)
        self.tilemap.AddTile('semla.png', 9, 20)
        self.tilemap.AddTile('semla.png', 9, 21)
        self.tilemap.AddTile('semla.png', 10, 18)
        self.tilemap.AddTile('semla.png', 10, 19)
        self.tilemap.AddTile('semla.png', 10, 20)
        self.tilemap.AddTile('semla.png', 10, 21)
        self.tilemap.AddTile('semla.png', 11, 18)
        self.tilemap.AddTile('semla.png', 11, 19)
        self.tilemap.AddTile('semla.png', 11, 20)
        self.tilemap.AddTile('semla.png', 11, 21)
        self.tilemap.AddTile('semla.png', 12, 18)
        self.tilemap.AddTile('semla.png', 12, 19)
        self.tilemap.AddTile('semla.png', 12, 20)
        self.tilemap.AddTile('semla.png', 12, 21)
        self.tilemap.AddTile('semla.png', 13, 18)
        self.tilemap.AddTile('semla.png', 13, 19)
        self.tilemap.AddTile('semla.png', 13, 20)
        self.tilemap.AddTile('semla.png', 13, 21)
        self.tilemap.AddTile('semla.png', 14, 18)
        self.tilemap.AddTile('semla.png', 14, 19)
        self.tilemap.AddTile('semla.png', 14, 20)
        self.tilemap.AddTile('semla.png', 14, 21)
        self.tilemap.AddTile('semla.png', 15, 18)
        self.tilemap.AddTile('semla.png', 15, 19)
        self.tilemap.AddTile('semla.png', 15, 20)
        self.tilemap.AddTile('semla.png', 15, 21)
        self.tilemap.AddTile('semla.png', 16, 18)
        self.tilemap.AddTile('semla.png', 16, 19)
        self.tilemap.AddTile('semla.png', 16, 20)
        self.tilemap.AddTile('semla.png', 16, 21)
        self.tilemap.AddTile('semla.png', 17, 18)
        self.tilemap.AddTile('semla.png', 17, 19)
        self.tilemap.AddTile('semla.png', 17, 20)
        self.tilemap.AddTile('semla.png', 17, 21)
        self.tilemap.AddTile('semla.png', 18, 18)
        self.tilemap.AddTile('semla.png', 18, 19)
        self.tilemap.AddTile('semla.png', 18, 20)
        self.tilemap.AddTile('semla.png', 18, 21)
        self.tilemap.AddTile('semla.png', 19, 18)
        self.tilemap.AddTile('semla.png', 19, 19)
        self.tilemap.AddTile('semla.png', 19, 20)
        self.tilemap.AddTile('semla.png', 19, 21)
        self.tilemap.AddTile('semla.png', 20, 18)
        self.tilemap.AddTile('semla.png', 20, 19)
        self.tilemap.AddTile('semla.png', 20, 20)
        self.tilemap.AddTile('semla.png', 20, 21)
        self.tilemap.AddTile('semla.png', 15, 15)
        self.tilemap.AddTile('semla.png', 18, 12)
        self.tilemap.AddTile('semla.png', 12, 9)





    def LoadLevel(self, level):
        self.game.LoadLevel(level)

    def ShowLevel(self):
        self.game.isStart = True
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





