import pygame
import random
import time

class MainWindow(object):
    def __init__(self):
        self.init()

    def init(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((360, 150))
        self.clock = pygame.time.Clock()
        self.running = True

        self.arr = [random.randint(1,100) for i in range(10)]
        

        self.main_loop()

        pygame.quit()

    def draw_rects(self, arr):
        # Initializing Color
        color = (255,0,0)

        column = 1
        for h in arr:
            pygame.draw.rect(self.screen, color, pygame.Rect(30 * column, (50+abs(h-100)), 30, h))
            column += 1

    def main_loop(self):
        self.clock.tick(5) # Limit fps to 5, for better visualization of graph movement.
        isSorted = False
        i = 0
        j = 1

        print(self.arr)

        while self.running:

            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("purple")

            if not isSorted:
                if i < len(self.arr):
                    if j < len(self.arr):
                        if self.arr[j] < self.arr[i]:
                            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                        j += 1
                    
                    if j == len(self.arr):
                        i += 1
                        j = i + 1
                    
                    if i == len(self.arr) - 1:
                        print("Done sorting!")

            
            self.draw_rects(self.arr)

            # flip() the display to put your work on screen
            pygame.display.flip()

    def simple_sort(self, arr, n):
        for i in range(n):
            j = i+1
            while j <= n - 1:
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
                    continue
                j += 1






if __name__ == "__main__":
    MainWindow()
