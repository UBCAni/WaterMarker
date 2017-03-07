import os
from PIL import Image, ImageDraw, ImageFile

def watermark(position):
    directory = "images"
    mark = Image.open("mark.png")

    mark = mark.resize((mark.size[0] * 2, mark.size[1] * 2))
    mark_w, mark_h = mark.size
    os.chdir(directory)
    for filename in os.listdir():
        im = Image.open(filename).convert(mode="RGBA")
        im_w, im_h = im.size

        overlay = Image.new('RGBA', im.size, (0, 0, 0, 0))
        overlay.paste(mark, (position, im_h - mark_h - position), mark)

        im.paste(overlay, (0, 0), overlay)
        im.save(os.path.basename(filename) + "_mark.jpg")

watermark(100)