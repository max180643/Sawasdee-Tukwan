"""Testing image caption generator"""
import textwrap
import numpy as np
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def main():
    """Why do we even need main function in python?"""
    imagefile = "test.jpg"
    image = Image.open(imagefile).convert('RGBA')
    image = cropper(image, 512)
    text(image)

def cropper(image, targetsize):
    """oofio"""
    width, height = image.size
    if width <= height:
        re_width, re_height = 512, (width/height) / 512
        image = image.resize((int(re_width), int(re_width)), Image.ANTIALIAS)
    elif height < width:
        re_width, re_height = (width/height) * 512, 512
        image = image.resize((int(re_width), int(re_height)), Image.ANTIALIAS)
    width, height = image.size
    print(width, height)
    new_width, new_height = targetsize, targetsize

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    print(left, top, right, bottom)
    image = image.crop((left, top, right, bottom))
    return image

def text(image):
    W, H = 512, 512
    top_y = 30
    low_y = 400
    fillcolor = "yellow"
    shadowcolor = "black"
    draw = ImageDraw.Draw(image)

    text = " วันพฤหัสบดี "

    headerfont = ImageFont.truetype("‪‪C:\Windows\Fonts\DB Helvethaica X Blk v3.2.ttf",90)
    w, h = draw.textsize(text, font=headerfont)
    draw.text((((W-w)/2)-1, top_y), text, font=headerfont, fill=shadowcolor)
    draw.text((((W-w)/2)+1, top_y), text, font=headerfont, fill=shadowcolor)
    draw.text((((W-w)/2), top_y-1), text, font=headerfont, fill=shadowcolor)
    draw.text((((W-w)/2), top_y+1), text, font=headerfont, fill=shadowcolor)
    draw.text(((W-w)/2, top_y), text, font=headerfont, fill=fillcolor)

    low_text = "ผู้ชายไม่ได้ต้องการนางฟ้า แต่ ต้องการ คนที่มีเวลาให้กัน ... ผู้หญิงไม่ได้ต้องการเทพบุตร แต่ ต้องการ คนที่หยุดสักที "
    para = textwrap.wrap(low_text, width=50)
    current_h, pad = 350, 10

    font = ImageFont.truetype("‪‪C:\Windows\Fonts\DB Helvethaica X Med v3.2.ttf",35)
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text((((W - w) / 2)-1, current_h), line, font=font, fill=shadowcolor)
        draw.text((((W - w) / 2)+1, current_h), line, font=font, fill=shadowcolor)
        draw.text(((W - w) / 2, current_h-1), line, font=font, fill=shadowcolor)
        draw.text(((W - w) / 2, current_h+1), line, font=font, fill=shadowcolor)
        draw.text(((W - w) / 2, current_h), line, font=font, fill=fillcolor)
        current_h += h + pad
    # draw.text((((W-w)/2)-1, low_y), low_text, font=font, fill=shadowcolor)
    # draw.text((((W-w)/2)+1, low_y), low_text, font=font, fill=shadowcolor)
    # draw.text((((W-w)/2), low_y-1), low_text, font=font, fill=shadowcolor)
    # draw.text((((W-w)/2), low_y+1), low_text, font=font, fill=shadowcolor)
    # draw.text(((W-w)/2, low_y), low_text, font=font, fill=fillcolor)
    image.convert('RGB').save('output.jpg')


main()
