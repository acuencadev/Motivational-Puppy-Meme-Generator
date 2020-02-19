import os
from random import randint
from uuid import uuid4

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """ Create a meme with the specified parameters """
    
    def __init__(self, output_dir: str):
        """
        Initializes the MemeEngine
        
        :param output_dir: Location where new memes will be saved.
        :return: None
        """
        self.output_dir = output_dir
        
    def make_meme(self, img_path: str, text: str, author: str,
                  width:int=500) -> str:
        """
        Creates a meme
        
        :param img_path: Path to the original image.
        :param text: Body of the quote.
        :param author: Author of the quote.
        :param width: Width of the image. Defaults to 500.
        :return: Path to the meme.
        """
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
