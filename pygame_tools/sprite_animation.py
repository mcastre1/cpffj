import pygame
import sys

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, tile_size):
        super().__init__()
        self.tile_size = tile_size
        self.images = self.split_image(image_path)

        self.sprite_index = 0
        self.sprite_speed = 0.1

        self.image = pygame.Surface((tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.image.fill('white')


    def split_image(self, path):
        images = []

        image = pygame.image.load(path).convert_alpha()
        x_tiles = int(image.get_width()/self.tile_size)
        y_tiles = int(image.get_height()/self.tile_size)

        for row in range(y_tiles):
            for col in range(x_tiles):
                x = col * self.tile_size
                y = row * self.tile_size

                new_surface = pygame.Surface((self.tile_size, self.tile_size), flags=pygame.SRCALPHA)
                new_surface.blit(image, (0,0), pygame.Rect(x, y, self.tile_size, self.tile_size))
                images.append(new_surface)

        return images
    
    def animate(self):
        self.sprite_index += self.sprite_speed

        if self.sprite_index >= len(self.images):
            self.sprite_index = 0

        self.image = self.images[int(self.sprite_index)]
        self.rect = self.image.get_rect()

    def update(self):
        self.animate()




class Sprite_animator():
    def __init__(self, path, tile_size):
        pygame.init()
        self.display_surface = pygame.display.set_mode((500,500))
        self.clock = pygame.time.Clock()

        self.sprite_group = pygame.sprite.GroupSingle()
        sprite = Sprite(path, tile_size)
        self.sprite_group.add(sprite)

        pygame.display.set_caption('Sprite animations')
        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.display_surface.fill('grey')

            self.sprite_group.update()
            self.sprite_group.draw(self.display_surface)
            

            pygame.display.update()
            self.clock.tick(60)



if __name__ == '__main__':
    animator = Sprite_animator('./tile_folder/idle.png', 32)