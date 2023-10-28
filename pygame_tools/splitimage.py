from PIL import Image
import os

# Split given image into x amount of images of size tile_size
# These splitted images will be squares
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

# Turn all images in path into a gif
def make_gif(path):
    tiles = []
    for file in os.listdir(path):
        if file.endswith('.png'):
            tiles.append(untransparent(Image.open(f'{path}/{file}', 'r')))

    first_tile = tiles[0]
    first_tile.save('gif_test.gif', format="GIF", append_images = tiles, save_all=True, duration=85, loop=100)

# Turn all transparent, alpha value of 1, pixels into a color with alpha value of 100
# Making the background not transparent
def untransparent(img):
    img = img.convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        if item[3] == 0:
            new_data.append((82,82,82,100))
        else:
            new_data.append(item)

    img.putdata(new_data)
    return img

if __name__ == "__main__":
    split_image(32, './pygame_tools/tile_folder/walking_v4.png')
    make_gif("./pygame_tools/out_tiles")