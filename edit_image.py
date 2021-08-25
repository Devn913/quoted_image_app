from PIL import Image, ImageDraw, ImageFont, ImageFilter
from image_grab import ImageGrab
from fetch_quote import Quote
import textwrap
import random
import base64
import requests
import os

class ImageEdit:

    def genPhoto(self):
        save_image = ImageGrab()
        name = save_image.unsplash()
        return name
    
    def blurImage(self, name):
        image_to_blur = Image.open(name)
        blurred_image = image_to_blur.filter(ImageFilter.GaussianBlur(radius=5))   
        blurred_image.save(name)
    
    def drawSquare(self, name):
        image = Image.open(name)
        draw = ImageDraw.Draw(image)
        color = "white"
        draw.rectangle([(50,50),(950,950)], fill=None, outline=color, width=15)
        image.save(name)
    
    def drawQuote(self, name):
        image = Image.open(name)
        draw = ImageDraw.Draw(image)      
        quote = Quote().getQuote()
        para = textwrap.wrap(quote, width=25)
        MAX_W, MAX_H = 1000,1000
        current_h, pad = 300, 15
        last_font = 3                               # if you want to add a font change its name to a number following old fonts and change the variable here
        r = random.randint(1,last_font)
        fonts = ImageFont.truetype("fonts/"+ str(r) + ".ttf", 50)
        for line in para:
            w,h = draw.textsize(line,font = fonts)
            draw.text(((MAX_W - w) / 2 , current_h),line,font = fonts)
            current_h += h + pad     
        image.save(name)
    
    def upload(self, name):
        api_key = "apiKey"
        url = "https://api.imgbb.com/1/upload"
        with open(name,'rb') as file:
            payload = {"key": api_key, "image": base64.b64encode(file.read())}
            while True:
                try: 
                    result = requests.post(url,payload)
                    if result.status_code == 200: break
                except:
                    return "Something is wrong....!"
        os.remove(name)
        return result.json()['data']['url']

    def run(self):
        name = self.genPhoto()
        self.blurImage(name)
        self.drawSquare(name)
        self.drawQuote(name)
        url = self.upload(name)
        return url

