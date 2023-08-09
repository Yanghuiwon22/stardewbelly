import sys, pygame
from setting import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.title = pygame.display.set_caption("stardew belly_ studing")
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            # print("A")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()

if __name__=="__main__":
    game = Game()
    game.run()


#animating the player 넘김