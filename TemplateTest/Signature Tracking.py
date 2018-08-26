# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 19:44:51 2018

@author: jimme
"""
import cv2
import numpy as np

class SignatureTracking:
    def studentAttended(self, ID, date, courseCode):
        return True
    
    def addStudentData(studentData):
        return True
    
    def addCourseData(self, courseData):
        return True
    
    def convertToImage(self, fileName):
        return True
    
    def uploadAttendanceFile(self, fileName):
        image = cv2.imread(fileName)
        height, width = image.shape[:2]
        
        i = 1
        name = "name"
        r1 = .10
        r2 = .20
        
        while (r2 < 0.7):
            
            start_row, start_col = int(height * r1), int(width * .51)
            
            end_row, end_col = int(height * r2), int (width * .80)
            
            #start_row, start_col = int(height * .10), int(width * .51)
            
            #end_row, end_col = int(height * .20), int (width * .80)
            
            cropped = image[start_row:end_row, start_col:end_col]
            
            #cv2.imshow("img", cropped)
            name +=str(i)+".jpg"
            cv2.imwrite(name, cropped)
            name = "name"
            i+=1
            r1 += 0.1
            r2 += 0.1

    def cleanImages(self, sig1, sig2):
        image1 = cv2.imread(sig1, cv2.IMREAD_GRAYSCALE)
        image2 = cv2.imread(sig2,  cv2.IMREAD_GRAYSCALE)
        
        #--REMOVE THE NOISE FROM IMAGES--
        adapt1 = cv2.adaptiveThreshold(image1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
        cv2.imwrite('thresh10.jpg', adapt1)
        
        adapt2 = cv2.adaptiveThreshold(image2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
        cv2.imwrite('thresh11.jpg', adapt2)
        
    def removeLines(self, sig1, sig2):
        image1 = cv2.imread(sig1)
        image2 = cv2.imread(sig2)
        edges = cv2.Canny(image1, 10, 50, apertureSize=3)
        minLineLength = 10
        maxLineGap= 5   
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
        
        for x in range(len(lines)):
            for x1, y1, x2, y2 in lines[x]:
                cv2.line(image1, (x1, y1), (x2, y2), (255,255,255), 2)
        
        cv2.imwrite('houghLines10.jpg', image1)
        
        edges2 = cv2.Canny(image2, 50, 150, apertureSize=3)
         
        lines2 = cv2.HoughLinesP(edges2, 1, np.pi/180, 100, minLineLength, maxLineGap)
        
        for x in range(len(lines2)):
            for x1, y1, x2, y2 in lines[x]:
                cv2.line(image2, (x1, y1), (x2, y2), (255,255,255), 2)
        
        cv2.imwrite('houghLines11.jpg', image2)
        
    def compareSignatures(self, sig1, sig2):
        img1 = cv2.imread(sig1, 0)
        img2 = cv2.imread(sig2, 0)
        
        orb = cv2.ORB_create()
        
        kp1, des1 = orb.detectAndCompute(img1,None)
        kp2, des2 = orb.detectAndCompute(img2,None)
        
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        
        matches = bf.match(des1, des2)
        
        matches = sorted(matches, key=lambda x:x.distance)
        
        #img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags = 2)
        
        #plt.imshow(img3), plt.show()
        #cv2.imshow("img3", img3)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        
        return len(matches)
        #print(len(matches))
        
        
    def takeAttendance():
        return True
    
    def getAttendanceLog(self, date, courseCode):
        return True
    
    def displayAttendanceLog(self, date, courseCode):
        print("Date: " + date, "CourseCode: " + courseCode)
        
#convert pdf to jpg function

        
    
        
    
