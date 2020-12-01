from PIL import Image
import glob2
image_list = []
for filename in glob.glob('"C:/Users/ADMIN/Desktop/strict/*.jpg'):
    im=Image.open(filename)
    #image_list.append(im)
    #foo = Image.open("C:\\Users\\ADMIN\\Desktop\\strict\\1.jpg")
    #foo.size
    foo = im.resize((600,600),Image.ANTIALIAS)
    foo.save("C:\\Users\\ADMIN\\Desktop\\strict\\resized1.jpg",quality=20)
    foo.save("C:\\Users\\ADMIN\\Desktop\\strict\\resized2.jpg",optimize=True,quality=95)
