# -*- coding: utf-8 -*-
from imageio import imread
from matplotlib.pyplot import imshow

from PIL import Image
import numpy as np
import sys
import matplotlib.pyplot as plt
import cv2
from uitl import PalletteToPNG, ColorToPNG

from palette import ColorThief


#fd = urlopen('http://lokeshdhakar.com/projects/color-thief/img/photo1.jpg')
#f = io.BytesIO(fd.read())
im = ('db/upload/1.jpg')
color_thief = ColorThief(im)

print(color_thief.get_color(quality=1))
print(color_thief.get_palette(quality=1))
#c_array = np.asarray(color_thief.get_palette(quality=1))
#print(c_array)

img1 = PalletteToPNG(color_thief.get_palette(quality=1))
img2 = ColorToPNG(color_thief.get_color(quality=1))



'''
img = Image.fromarray(c_array,'RGB')
img.save('testrgb.png')
#img.show()
array = np.zeros([100, len(c_array)*100, 3], dtype=np.uint8)
for x in range(len(c_array)):
    y = x*10
    array[:,x*100:] = c_array[x] #Orange left side

#array = np.zeros([100, 200, 3], dtype=np.uint8)
#array[:,:100] = c_array[0] #Orange left side
#array[:,400:] = [0, 0, 255]   #Blue right side

img = Image.fromarray(array)
img.save('testrgb.png')
'''


