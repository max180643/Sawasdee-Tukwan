""" Image caption generator"""
import textwrap
import requests
import PIL
import csv
from random import choice
from io import BytesIO
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

class GenerateImage:
    def __init__(self, url, size, day=0):
        self.img = self.generateImage(url, int(size))
        self.size = int(size)
        self.day = day # [Sunday, Monday, ..., Friday, Saturday]
        self.ratio = self.size / 512

    def generateImage(self, url, size):
        """Why do we even need main function in python?"""
        response = requests.get(url)
        image = Image.open(BytesIO(response.content)).convert('RGBA')
        image = self.cropper(image, int(size))
        return image

    def cropper(self, image, targetsize):
        """ Resize and crop image """
        width, height = image.size
        if width >= height:
            ratio = height / width
            image = image.resize((targetsize, int(targetsize * ratio)), PIL.Image.BICUBIC)
            to_crop = int((image.size[0] - targetsize) / 2)
            image = image.crop((to_crop, 0, image.size[0] - to_crop, image.size[1]))
        else:
            ratio = width / height
            image = image.resize((int(targetsize * ratio), targetsize), PIL.Image.BICUBIC)
            to_crop = int((image.size[1] - targetsize) / 2)
            image = image.crop((0, to_crop, image.size[0], image.size[1] - to_crop))        
        return image

    def addText(self, msg=None):
        wanweek = ["อาทิตย์ ", "จันทร์ " , "อังคาร ", "พุธ ", "พฤหัสบดี ", "ศุกร์ ", "เสาร์ ", "วาเลนไทน์ "]
        fillcolor = ["#F00", "#FF0", "#FC0FC0", "#7CFC00", "#FFA500", "#00BFFF", "#8A2BE2", "#FFB6C1"]
        shadowcolor = ["#fff", "#000", "#fff", "#000", "#000", "#000", "#fff", "#F00"]
        W, H = self.size, self.size
        top_y = int(15 * self.ratio)
        low_y = int(400 * self.ratio)
        draw = ImageDraw.Draw(self.img)

        datasetpath = "../csv/" + str(self.day) + ".csv"

        with open(datasetpath, encoding="utf-8") as f:
            reader = csv.reader(f)
            low_text = choice(list(reader)) if not msg else msg

        low_text = ''.join(low_text) + " "
        text = " สวัสดีวัน" + wanweek[self.day]

        headerfont = ImageFont.truetype("‪‪font/Pattaya-Regular.ttf", int(84 * self.ratio))
        w, h = draw.textsize(text, font=headerfont)
        draw.text((((W-w)/2)-1, top_y), text, font=headerfont, fill=shadowcolor[self.day])
        draw.text((((W-w)/2)+1, top_y), text, font=headerfont, fill=shadowcolor[self.day])
        draw.text((((W-w)/2), top_y-1), text, font=headerfont, fill=shadowcolor[self.day])
        draw.text((((W-w)/2), top_y+1), text, font=headerfont, fill=shadowcolor[self.day])
        draw.text(((W-w)/2, top_y), text, font=headerfont, fill=fillcolor[self.day])

        # low_text = "ผู้ชายไม่ได้ต้องการนางฟ้า แต่ ต้องการ คนที่มีเวลาให้กัน ... ผู้หญิงไม่ได้ต้องการเทพบุตร แต่ ต้องการ คนที่หยุดสักที " if not msg else msg
        para = textwrap.wrap(low_text, width=36)
        current_h, pad = int(350 * self.ratio), 10

        font = ImageFont.truetype("‪‪font/Pattaya-Regular.ttf", int(28 * self.ratio))
        for line in para:
            w, h = draw.textsize(line, font=font)
            draw.text((((W - w) / 2)-1, current_h), line, font=font, fill=shadowcolor[self.day])
            draw.text((((W - w) / 2)+1, current_h), line, font=font, fill=shadowcolor[self.day])
            draw.text(((W - w) / 2, current_h-1), line, font=font, fill=shadowcolor[self.day])
            draw.text(((W - w) / 2, current_h+1), line, font=font, fill=shadowcolor[self.day])
            draw.text(((W - w) / 2, current_h), line, font=font, fill=fillcolor[self.day])
            current_h += h + pad
        self.img = self.img.convert('RGB')

if __name__ == '__main__':
    obj = GenerateImage("https://picsum.photos/512/512?random=1", 512)
    obj.img.save('test.jpg')