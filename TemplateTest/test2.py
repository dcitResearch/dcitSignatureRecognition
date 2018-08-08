# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 20:19:36 2018

@author: jimme
"""

import cv2
import numpy as np


'''
#---I DID THESE PROCESSES INCREMENTLY INSTEAD OF PLACING THEM IN DIFFERENT FILES---

#STEP 1
#--READS IN BOTH IMAGES--

image1 = cv2.imread("sig1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("sig2.jpg",  cv2.IMREAD_GRAYSCALE)

#--REMOVE THE NOISE FROM IMAGES--
adapt1 = cv2.adaptiveThreshold(image1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
cv2.imwrite('thresh1.jpg', adapt1)

adapt2 = cv2.adaptiveThreshold(image2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
cv2.imwrite('thresh2.jpg', adapt2)
'''

'''
STEP 2
--TAKES NOISE-FREE IMAGES AND REMOVES THE LINES FROM THEM--

image1 = cv2.imread("thresh3.jpg")
image2 = cv2.imread("thresh4.jpg")
edges = cv2.Canny(image1, 150, 350, apertureSize=3)
minLineLength = 100
maxLineGap= 50   
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)

for x in range(len(lines)):
    for x1, y1, x2, y2 in lines[x]:
        cv2.line(image1, (x1, y1), (x2, y2), (255,255,255), 2)

cv2.imwrite('houghLines3.jpg', image1)

edges2 = cv2.Canny(image2, 50, 150, apertureSize=3)
 
lines2 = cv2.HoughLinesP(edges2, 1, np.pi/180, 100, minLineLength, maxLineGap)

for x in range(len(lines2)):
    for x1, y1, x2, y2 in lines[x]:
        cv2.line(image2, (x1, y1), (x2, y2), (255,255,255), 2)

cv2.imwrite('houghLines4.jpg', image2)
'''


#STEP 3
#--USES ORB TO LOOK FOR COMMON KEYPOINTS BETWEEN THE TWO IMAGES--    
#from matplotlib import pyplot as plt 

img1 = cv2.imread("houghLines1.jpg", 0)
img2 = cv2.imread("houghLines2.jpg", 0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)

matches = sorted(matches, key=lambda x:x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags = 2)

#plt.imshow(img3), plt.show()
cv2.imshow("img3", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(len(matches))






