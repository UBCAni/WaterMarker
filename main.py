import os
from PIL import Image, ImageDraw, ImageFile

def watermark(position):
    directory = "images"
    images = []
    mark = Image.open("mark.png")

    mark = mark.resize((mark.size[0] * 2, mark.size[1] * 2))
    mark_w, mark_h = mark.size
    os.chdir(directory)

    for filename in os.listdir():
        if os.path.isfile(filename):
            im = Image.open(filename).convert(mode="RGBA")
            im_w, im_h = im.size

            overlay = Image.new('RGBA', im.size, (0, 0, 0, 0))
            overlay.paste(mark, (position, im_h - mark_h - position), mark)

            im.paste(overlay, (0, 0), overlay)

            images.append((filename, im))

    os.chdir("marked")

    for i in images:
        i[1].save(i[0])


watermark(100)