import pygame
from setting import *
from support import *
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
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

        #tools
        self.selected_tool = "_axe"

    def import_assets(self):
        self. animations = {"up" : [], "down" : [], 'left' : [], "right" : [],
                            "up_idle" : [], "down_idle" : [], 'left_idle' : [], "right_idle" : [],
                            "up_hoe": [], "down_hoe": [], 'left_hoe': [], "right_hoe": [],
                            "up_axe": [], "down_axe": [], 'left_axe': [], "right_axe": [],
                            "up_water": [], "down_water": [], 'left_water': [], "right_water": []}

        for animation in self.animations.keys():
            full_path = "C:\code\stardewbelly-main\s1 - setup\graphics\character/" + animation
            self.animations[animation] = import_folder(full_path)
    def animate(self, dt):
        self.index_frame += 4 * dt
        if self.index_frame >= len(self.animations[self.status]):
            self.index_frame = 0

            print(self.status)

        self.image = self.animations[self.status][int(self.index_frame)]# -------> 크기
    def input(self):
        keys = pygame.key.get_pressed()

        # directions
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = +1
            self.status = 'down'
        else:
            self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = +1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

    #     tool use
        if keys[pygame.K_SPACE]:
            self.selected_tool = "_hoe"
        else:
            
            self.status = self.status.split("_")[0]
            print(self.status)

    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split("_")[0] + "_idle"

    def use_tool(self):
        self.status = self.status.split('_')[0] + self.selected_tool
    def move(self, dt):
        # normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.use_tool()

        self.get_status()
        self.move(dt)
        self.animate(dt)

