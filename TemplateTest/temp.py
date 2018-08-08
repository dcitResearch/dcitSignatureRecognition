# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
"""
#img = cv2.imread("sample.jpg")
#gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
"""

image1 = cv2.imread("list.jpg", cv2.IMREAD_GRAYSCALE)
#image2 = cv2.imread("try.jpg", cv2.IMREAD_GRAYSCALE)


#_, threshold = cv2.threshold(template, 155, 255, cv2.THRESH_BINARY)

adapt_t = cv2.adaptiveThreshold(image1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)

'''
w, h = template.shape[::-1]

result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
loc = np.where(result >= 0.9)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 255, 0), 3)
    
'''
cv2.imshow("img", image1)

#cv2.imshow("result", result)
#cv2.waitKey(0)
#cv2.destroyAllWindows()




"""
img1 = cv2.imread("list.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("try.jpg", cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
matches = bf.match(des1, des2)

matching_results = cv2.drawMatches(img1, kp1, img2, kp2, matches, None)

print (len(matches))

#cv2.imshow("matchingResults", matching_results)
"""