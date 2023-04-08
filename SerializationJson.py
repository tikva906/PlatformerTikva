import ItemTile
from Tile import Tile
from damagetile import DamageTile
from TileMap import TileMap

# сериализация - преобразование класса в текст
# （хранить будем словари - поэтому в словарь)
class SerializationJson:
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
            itemTileMaplist.append(self.SerializeItemTile(el))

        return itemTileMaplist

    def SerializeTileMap(self, tileMap):
        TileMaplist = []

        for el in tileMap.group.sprites():
            print(el)
            TileMaplist.append(self.SerializeTile(el))
        print(TileMaplist)
        return TileMaplist

    def SerializeDamageTileMap(self, damageTileMap):
        DamageTileMaplist = []

        for el in damageTileMap.group.sprites():
            DamageTileMaplist.append(self.SerializeDamageTile(el))

        return DamageTileMaplist

    def Serialize(self, tilemap, itemtilemap, damagetilemap):
        return {"TileMap": self.SerializeTileMap(tilemap), "DamageTileMap": self.SerializeDamageTileMap(damagetilemap),
                "ItemTileMap": self.SerializeItemTileMap(itemtilemap)}