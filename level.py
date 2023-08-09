import sys, pygame
from setting import *
from player import Player

class Level:
    def __init__(self):
        # def the display surface
        self.display_surface = pygame.display.get_surface()

        # sprout groups
        self.all_sprites = pygame.sprite.Group()
        #  sprite는 Sprite 클래스는 게임에서 다양한 유형의 객체에 대한 기본 클래스로 사용하기 위한 것입니다.

        self.setup()

    def setup(self):
        self.player = Player((640,360), self.all_sprites)

    def run(self, dt):
        # print("b")
        self.display_surface.fill("black")
        self.player.import_assets()
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
