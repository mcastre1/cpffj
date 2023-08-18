import pygame
import random
from RectColor import RectColor
import time
from selection_sort import *

class MainWindow(object):
    BLACK = (0,0,0)
    GRAY = (60,60,60)
    YELLOW = (227, 227, 9)
    GREEN = (4, 181, 4)
    RED = (176, 5, 5)
    MAX_H = 100
    X_VALUES = random.randint(10,20)

    def __init__(self):
        self.init()

    def init(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((30*(self.X_VALUES + 2), 150))
        self.clock = pygame.time.Clock()
        self.running = True

        #self.arr = [random.randint(1,100) for i in range(10)]
        self.arr = []
        for i in range(1, self.X_VALUES+1):
            h = random.randint(1,self.MAX_H)
            self.arr.append(RectColor(30 * i, (50+abs(h-self.MAX_H)), 30, h))
        
        
        self.main_loop()

        pygame.quit()

    def draw_rects(self):
        for r in self.arr:
            pygame.draw.rect(self.screen, color=r.color, rect = r)


    def find_smallest(self, start, end):
        temp = self.arr[start].h
        index = -1
        
        for i in range(start, end + 1):
            if self.arr[i].h < temp:
                temp = self.arr[i].h
                index = i

        if index == -1:
            return start

        return index
    

    def swap(self, i, j):
        self.arr[i].x, self.arr[j].x = self.arr[j].x, self.arr[i].x
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def main_loop(self):
        isSorted = False
        i = 0
        j = 1

        while self.running:
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("white")

            if not isSorted:
                if i < len(self.arr) - 1:
                    
                    smallest_found = self.find_smallest(i+1, len(self.arr)-1)
                    if self.arr[smallest_found].h < self.arr[i].h:
                        self.swap(i, smallest_found)

                    i += 1


            
            self.draw_rects()

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(10)  # limits FPS to 60


if __name__ == "__main__":
    MainWindow()
