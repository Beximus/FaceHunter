
import os
from PIL import Image

# This script will let you quickly resize the images you have found 

# change the path to make it workable
img_dir = r"/Users/campberebe3/Desktop/faceassignment/trumpfaces"
for filename in os.listdir(img_dir):
    filepath = os.path.join(img_dir, filename)
    with Image.open(filepath) as im:
        x, y = im.size
    totalsize = x*y
    if x < 100 or y < 100:
        os.remove(filepath)

