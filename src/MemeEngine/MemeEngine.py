import os
from uuid import uuid4

from PIL import Image


class MemeEngine:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        
    def make_meme(self, img_path: str, text: str, author: str,
                  width:int=500) -> str:
        img = Image.open(img_path)
        
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        
        img = img.resize((width, height), Image.NEAREST)
        
        file_name = f"{uuid4()}.jpg"
        path = os.path.join(output_dir, file_name)
        
        img.save(path)
        
        return path
