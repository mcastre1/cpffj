import pygame
import sys

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, tile_size):
        super().__init__()
        self.images = self.split_image(image_path)
        self.tile_size = tile_size

        print(self.images)


    def split_image(self, path):
        images = []

        image = pygame.image.load(path).convert_alpha()
        x_tiles = image.get_width()/self.tile_size
        y_tiles = image.get_height()/self.tile_size

        for row in range(y_tiles):
            for col in range(x_tiles):
                x = col * self.tile_size
                y = row * self.tile_size

                new_surface = pygame.Surface((self.tile_size, self.tile_size), flags=pygame.SRCALPHA)
                new_surface.blit(image, (0,0), pygame.Rect(x, y, self.tile_size, self.tile_size))
                images.append(new_surface)

        return images




class Sprite_animator():
    def __init__(self, path, tile_size):
        pygame.init()
        self.display_surface = pygame.display.set_mode((500,500))
        self.clock = pygame.time.Clock()

        sprite_group = pygame.sprite.GroupSingle()
        sprite = Sprite(path, tile_size)
        sprite_group.add(sprite)

        pygame.display.set_caption('Sprite animations')
        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.display_surface.fill('black')



            pygame.display.update()
            self.clock.tick(60)

            



if __name__ == '__main__':
    animator = Sprite_animator('./tile_folder', 32)