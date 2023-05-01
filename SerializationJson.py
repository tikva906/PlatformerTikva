import json
import pygame
import ItemTile
from Tile import Tile
from damagetile import DamageTile
from TileMap import TileMap
from UI.Button import Button

# сериализация - преобразование класса в текст
# （хранить будем словари - поэтому в словарь)
class SerializationJson:

    @staticmethod
    def GetStartButton(game):
        # {"Font": {"Style": "Arial", "Size": 40}, "Render": {"Text": "start", "Antialias": True, "TextColor": [1, 0, 0], "Background": [1, 187, 255]}}
        with open(f"UI/menu.json", "r") as file:
            data = json.load(file)
            startbtn = data["StartButton"]
            style = startbtn["Font"]["Style"]
            size = startbtn["Font"]["Size"]
            text = startbtn["Render"]["Text"]
            antialias = startbtn["Render"]["Antialias"]
            textColor = startbtn["Render"]["TextColor"]
            txtColorCort = (textColor[0], textColor[1], textColor[2])
            backColor = startbtn["Render"]["Background"]
            backColorCort = (backColor[0], backColor[1], backColor[2])
            #font = pygame.font.SysFont(style, size)
            #btn_text = font.render(text, antialias, txtColorCort, backColorCort)
            btn = Button("StartButton", style, size, text, antialias, txtColorCort, backColorCort,game)

            return btn

    def SerializeTile(self, tile): # указал явно что надо передавать
        return {"texture": tile.texture, "x": tile.rect.left, "y": tile.rect.top}

    def SerializeItemTile(self, itemTile):
        return {"texture": itemTile.texture, "x": itemTile.rect.left, "y": itemTile.rect.top, "name": itemTile.name,
                "id": itemTile.id}

    def SerializeDamageTile(self, damageTile):
        return {"texture": damageTile.texture, "x": damageTile.rect.left, "y": damageTile.rect.top, "damage": damageTile.damage}

    def SerializeItemTileMap(self, itemTileMap):
        itemTileMaplist = []

        for el in itemTileMap.group.sprites():
            ser = self.SerializeItemTile(el)
            ser["x"] = ser["x"] // itemTileMap.width
            ser["y"] = ser["y"] // itemTileMap.height
            itemTileMaplist.append(ser)

        return itemTileMaplist

    def SerializeTileMap(self, tileMap):
        TileMaplist = []

        for el in tileMap.group.sprites():
            ser = self.SerializeTile(el)
            ser["x"] = ser["x"] // tileMap.width
            ser["y"] = ser["y"] // tileMap.height
            TileMaplist.append(ser)
        print(TileMaplist)
        return TileMaplist

    def SerializeDamageTileMap(self, damageTileMap):
        DamageTileMaplist = []

        for el in damageTileMap.group.sprites():
            ser = self.SerializeDamageTile(el)
            ser["x"] = ser["x"] // damageTileMap.width
            ser["y"] = ser["y"] // damageTileMap.height
            DamageTileMaplist.append(ser)

        return DamageTileMaplist

    def Serialize(self, tilemap, itemtilemap, damagetilemap):
        return {"TileMap": self.SerializeTileMap(tilemap), "DamageTileMap": self.SerializeDamageTileMap(damagetilemap),
                "ItemTileMap": self.SerializeItemTileMap(itemtilemap)}