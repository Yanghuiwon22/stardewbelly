import pygame
from setting import *
from support import *
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        print("c")
        super().__init__(group)         # -----> super뒤에 ()를 안붙였더니 아래의 에러가 뜸
                                        #  TypeError: descriptor '__init__' requires a 'super' object but received a 'Group'
        self.import_assets()
        self.status = 'down'
        self.index_frame = 0

        # general setup

        self.image = self.animations[self.status][self.index_frame]# -------> 크기
        self.rect = self.image.get_rect(center = pos)

        # movement attribute
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        self. animations = {"up" : [], "down" : [], 'left' : [], "right" : []}
        for animation in self.animations.keys():
            full_path = "C:\code\STARDEWBELLY_STUDY\graphics\character/" + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        if self.direction != (0,0):
            print(self.direction)
            self.index_frame += 4 * dt
            if self.direction.y == -1:
                self.status = 'up'
            if self.direction.y == +1:
                self.status = 'down'
            if self.direction.x == -1:
                self.status = 'left'
            if self.direction.x == +1:
                self.status = 'right'

            if self.index_frame >= 4:
                self.index_frame /= 4

        self.image = self.animations[self.status][int(self.index_frame)]# -------> 크기

    def input(self):
        keys = pygame.key.get_pressed()
        # print("D")

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = +1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = +1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)