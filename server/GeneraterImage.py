""" Image caption generator"""
import textwrap
import requests
import PIL
from io import BytesIO
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

class GenerateImage:
    def __init__(self, url, size):
        self.img = self.generateImage(url, int(size))
        self.size = int(size)
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
        W, H = self.size, self.size
        top_y = int(15 * self.ratio)
        low_y = int(400 * self.ratio)
        fillcolor = "yellow"
        shadowcolor = "black"
        draw = ImageDraw.Draw(self.img)

        text = " วันพฤหัสบดี "

        headerfont = ImageFont.truetype("‪‪font/Pattaya-Regular.ttf", int(84 * self.ratio))
        w, h = draw.textsize(text, font=headerfont)
        draw.text((((W-w)/2)-1, top_y), text, font=headerfont, fill=shadowcolor)
        draw.text((((W-w)/2)+1, top_y), text, font=headerfont, fill=shadowcolor)
        draw.text((((W-w)/2), top_y-1), text, font=headerfont, fill=shadowcolor)
        draw.text((((W-w)/2), top_y+1), text, font=headerfont, fill=shadowcolor)
        draw.text(((W-w)/2, top_y), text, font=headerfont, fill=fillcolor)

        low_text = "ผู้ชายไม่ได้ต้องการนางฟ้า แต่ ต้องการ คนที่มีเวลาให้กัน ... ผู้หญิงไม่ได้ต้องการเทพบุตร แต่ ต้องการ คนที่หยุดสักที " if not msg else msg
        para = textwrap.wrap(low_text, width=36)
        current_h, pad = int(350 * self.ratio), 10

        font = ImageFont.truetype("‪‪font/Pattaya-Regular.ttf", int(28 * self.ratio))
        for line in para:
            w, h = draw.textsize(line, font=font)
            draw.text((((W - w) / 2)-1, current_h), line, font=font, fill=shadowcolor)
            draw.text((((W - w) / 2)+1, current_h), line, font=font, fill=shadowcolor)
            draw.text(((W - w) / 2, current_h-1), line, font=font, fill=shadowcolor)
            draw.text(((W - w) / 2, current_h+1), line, font=font, fill=shadowcolor)
            draw.text(((W - w) / 2, current_h), line, font=font, fill=fillcolor)
            current_h += h + pad
        self.img = self.img.convert('RGB')

if __name__ == '__main__':
    obj = GenerateImage("https://picsum.photos/512/512?random=1", 512)
    obj.img.save('test.jpg')