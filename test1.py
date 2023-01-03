import cv2 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import shutil
import imagehash
from PIL import Image

img = cv2.imread('static/data1/a (2).png') 	
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("static/gg.png", gray)

img = cv2.imread('static/gg.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,1.5*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
segment = cv2.subtract(sure_bg,sure_fg)
img = Image.fromarray(img)
segment = Image.fromarray(segment)
path3="static/fg.png"
segment.save(path3)
