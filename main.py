import argparse
import os
from PIL import Image, ImageDraw, ImageFile

directory = "images/"
scale = 2

def set_mark(position):
    mark = Image.open("mark.png")
    mark = mark.resize((mark.size[0] // scale, mark.size[1] // scale))
    mark_w, mark_h = mark.size

    for filename in os.listdir(directory):
        try:
            path = directory + filename
            if os.path.isfile(path):
                with open(path, 'rb') as pic, open("marked/" + filename, 'w') as out:
                        put_mark(pic, mark, position).save(out)

        except Exception as e:
            print(f"An unexpected error occurred\n{e}")


def put_mark(picture, mark, position):
    im = Image.open(picture).convert(mode="RGBA")
    im = im.resize((im.size[0] // scale, im.size[1] // scale))

    im_w, im_h = im.size
    offset = (position, position)
    im.paste(mark, offset, mark)

    print(f"Processing {picture.name}")

    return im


def change_opacity(img, modifier):
    img_w, img_h = img.size
    pixels = img.load()
    for x in range(img_w):
        for y in range(img_h):
            pixel = pixels[x, y]
            pixels[x, y] = (pixel[0], pixel[1], pixel[2], 0 if pixel[3] + modifier < 0 else pixel[3] + modifier)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Watermark a batch of images')
    parser.add_argument('offset', nargs='?', help="The offset from the corner", default=50)
    args = parser.parse_args()

    set_mark(args.offset)
