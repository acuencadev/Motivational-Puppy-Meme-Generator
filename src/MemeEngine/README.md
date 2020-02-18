# Meme Engine Module

The Meme Engine Module is responsible for manipulating and drawing text onto images. The module has the following responsibilities:

- Loading of a file from disk
- Transform image by resizing to a maximum width of 500px while maintaining the input aspect ratio
- Add a caption to an image (string input) with a body and author to a random location on the image.

## Usage

```
from MemeEngine import MemeEngine


meme = MemeEngine('./tmp')
path = meme.make_meme(img, quote.body, quote.author)
```

## Requirements

This package requires Pillow to process the image. It is listed on the project's requirements.txt. Pillow can be installed using
the following command:

```
pip install pillow
```