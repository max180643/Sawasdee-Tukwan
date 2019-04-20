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
    print("Input the width or height for 1:1 size here:")
    targetsize = int(input())
    image = cropper(image, targetsize)
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
    low_text = "ตื่นมาเช้านี้ สิ่งไม่ดีจงหมดไป คิดทำอะไร ให้รํ่ารวยทันใจ รวยไปตลอดกาล"
    text = " สวัสดีวันจันทร์ "
    fillcolor = "yellow"
    shadowcolor = "black"
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("‪C:\Windows\Fonts\Kanit-SemiBold.ttf",50)
    w, h = draw.textsize(text, font=font)
    draw.text((((W-w)/2)-1, top_y), text, font=font, fill=shadowcolor)
    draw.text((((W-w)/2)+1, top_y), text, font=font, fill=shadowcolor)
    draw.text((((W-w)/2), top_y-1), text, font=font, fill=shadowcolor)
    draw.text((((W-w)/2), top_y+1), text, font=font, fill=shadowcolor)
    draw.text(((W-w)/2, top_y), text, font=font, fill=fillcolor)

    draw.text((((W-w)/2)-1, low_y), low_text, font=font, fill=shadowcolor)
    draw.text((((W-w)/2)+1, low_y), low_text, font=font, fill=shadowcolor)
    draw.text((((W-w)/2), low_y-1), low_text, font=font, fill=shadowcolor)
    draw.text((((W-w)/2), low_y+1), low_text, font=font, fill=shadowcolor)
    draw.text(((W-w)/2, low_y), low_text, font=font, fill=fillcolor)
    image.convert('RGB').save('output.jpg')


main()
