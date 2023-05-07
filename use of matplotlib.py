
"""
use of matplotlib
 
"""

from matplotlib import pyplot as plt
x = [1,2,3,4,5]
y = [1,4,9,16,25]
import numpy as np
a = np.array(x)
b= np.array(y)
#plt.plot(x,y)

plt.figure(figsize=(12,6))
plt.subplot(221)
plt.bar(a,b)
plt.yscale('linear')
plt.title('linear scale')
plt.grid(True)
plt.subplot(222)
plt.plot(a,b)
plt.yscale('log')
plt.title('log scale')
plt.grid(True)

#import cv2
#gray_img = cv2.imread('om.jpg', 0)
#plt.imshow(gray_img, cmap = 'gray')

#plt.hist(gray_img, bins=100, range=(0,255))
