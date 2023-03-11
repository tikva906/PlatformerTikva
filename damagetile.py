from Tile import Tile

class DamageTile(Tile):
    def __init__(self,screen,texture,width,height,x,y,damage):
        super(DamageTile, self).__init__(screen,texture,width,height,x,y)
        self.damage = damage