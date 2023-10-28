from PIL import Image
import glob

def split_image(tile_size, path):
    image = Image.open(path, 'r')
    width, height = image.size

    im1 = image.crop((0, 0, 32, 32))

    for col in range(int(width/tile_size)):
        left = col * tile_size
        top = 0
        right = left + (tile_size)
        bottom = tile_size

        crop_img = image.crop((left, top, right, bottom))

        crop_img.save(f'./pygame_tools/out_tiles/{col}_image.png')
    im1.save('./new_image.png')

def make_gif(path):
    tiles = [Image.open(image) for image in glob.glob(f"./pygame_tools/out_files/*.PNG")]
    print(len(tiles))

    first_tile = tiles[0]
    first_tile.save('gif_test.gif', format="GIF", append_images = tiles, save_all=True, duration=100, loop=1)

if __name__ == "__main__":
    split_image(32, './pygame_tools/tile_folder/walking_v4.png')
    make_gif("./")