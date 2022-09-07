
from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()


        self.image = transfrom.scale(image.load(player.image), (width, heaight))
        self.speed = player_speed


        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def rect(self):
        window.bilt(self.image, (self.rect.x, self.rect.y))