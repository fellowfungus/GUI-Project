import pygame
from GameFiles.EngineScripts.GameObject import GameObject

class River(GameObject):

    def __init__(self, game_display):
        self.display = game_display
        self.vector2 = [0, 0]
        self.color = (0, 0, 0)
        self.size =  [800,20]
    def render(self):
        self.display.fill(self.color, rect=[self.vector2[0], self.vector2[1], self.size[0], self.size[1]])
    def update(self):
        self.render()