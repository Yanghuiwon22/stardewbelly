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
        # 화면에 변화를 주는 함수를 작성하려고 한다면, self.display_surface를 초기화 시켜주어야 한다 ( 무조건 )
        self.offset = pygame.math.Vector2()
        # 카메라 초기화: 주로 게임 개발에서 사용되는 카메라 시스템을 초기화하는 역할을 할 수 있습니다.
        # 카메라 시스템은 화면에 보이는 부분을 제어하고 플레이어나 객체의 움직임을 따라가는 역할을 합니다.
        # self.offset을 초기화함으로써 카메라의 시작 위치나 초기화 조건을 설정할 수 있습니다.

        #------> 만약 카메라 시스템을 이용하고 싶다면 self.offset을 초기화하고 시작하자 .
        #------> 초기화한다는 것은 초기값으로 설정한다는 것을 의미한다.

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH/2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT/2

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)


