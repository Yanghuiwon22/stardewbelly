import sys, pygame
from setting import *
from player import Player
from overlay import Overlay
from sprite import Generic
class Level:
    def __init__(self):
        # def the display surface
        self.display_surface = pygame.display.get_surface()

        # sprout groups
        self.all_sprites = CameraGroup()
        #  sprite는 Sprite 클래스는 게임에서 다양한 유형의 객체에 대한 기본 클래스로 사용하기 위한 것입니다.
        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        self.player = Player((640,360), self.all_sprites)

        Generic(
            pos = (0,0),
            surf = pygame.image.load('C:\code\stardewbelly-main\s1 - setup/graphics/world/ground.png').convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['ground'])


    def run(self, dt):
        # print("b")
        self.display_surface.fill("black")
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)

        self.overlay.display()

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH/2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT/2

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, sprite.rect)


