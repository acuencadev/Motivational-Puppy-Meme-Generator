import os
from random import randint
from uuid import uuid4

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        
    def make_meme(self, img_path: str, text: str, author: str,
                  width:int=500) -> str:
        img = Image.open(img_path)
        
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        
        image_position = (randint(0, 150), randint(0, 250))
        
        img = img.resize((width, height), Image.NEAREST)
        font = ImageFont.truetype(os.path.abspath('./fonts/android.ttf'), 20)
        draw = ImageDraw.Draw(img)
        
        draw.text(image_position, f"{text} - {author}", color=(0, 0, 0), font=font)
        
        file_name = f"{uuid4()}.png"
        path = os.path.join(self.output_dir, file_name)
        
        img.save(path)
        
        return path
