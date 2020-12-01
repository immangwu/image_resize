from PIL import Image
import os, sys

#path = "C:/Users/ADMIN/Desktop/strict/tamil/"
path = "E:/Photos/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((600,600), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=30)

resize()
