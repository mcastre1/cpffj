import pygame

class RectColor(pygame.Rect):
    def __init__(self, x, y, w, h, color=(0,0,0)):
        super().__init__(x, y, w, h)
        self.color = color