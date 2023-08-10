import pygame
from setting import *

class Overlay:
    def __init__(self, player):

        #general setup
        self.display_surface= pygame.display.get_surface()
        self.player = player

        # imports
        overlay_path = 'C:\code\stardewbelly-main/s1 - setup/graphics/overlay/'
        self.tools_surf = {tool:pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
        self.seeds_surf = {seed:pygame.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in player.seeds}
        print(self.tools_surf)
    def display(self):

        #tool
        tool_surf = self.tools_surf[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(midbotton = OVERLAY_POSITIONS)
        self.display_surface.blit(tool_surf,(0,0))
        #seeds