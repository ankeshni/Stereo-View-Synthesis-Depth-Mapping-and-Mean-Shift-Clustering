# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 22:04:23 2018

@author: Ankesh N. Bhoi
"""

import numpy as np
from sklearn.preprocessing import normalize
import cv2
from scipy import signal

imgLeft = cv2.imread('C:/Users/Ankesh N. Bhoi/Desktop/CVIP/PA-2/view5.png', 1)  
imgRight = cv2.imread('C:/Users/Ankesh N. Bhoi/Desktop/CVIP/PA-2/view1.png', 1)

imgLeftGT = cv2.imread('C:/Users/Ankesh N. Bhoi/Desktop/CVIP/PA-2/disp5.png', 0)  
imgRightGT = cv2.imread('C:/Users/Ankesh N. Bhoi/Desktop/CVIP/PA-2/disp1.png', 0) 

cv2.imshow(" ltruth",imgLeftGT)
cv2.imshow(" rtruth",imgRightGT)
cv2.imshow(" l",imgLeft)
cv2.imshow(" r",imgRight)

reconstructed = np.zeros(imgLeft.shape,'int')
l= np.zeros(imgLeft.shape,'uint8')
r= np.zeros(imgLeft.shape,'uint8')

for i in range(imgLeft.shape[0]):
    for j in range(imgLeft.shape[1]):
        try:
            if l[i,j+imgLeftGT[i,j]//2,0]==0:
                l[i,j+imgLeftGT[i,j]//2,0]=imgLeft[i,j,0]
                l[i,j+imgLeftGT[i,j]//2,1]=imgLeft[i,j,1]
                l[i,j+imgLeftGT[i,j]//2,2]=imgLeft[i,j,2]
            if j-imgRightGT[i,j]//2>0:
                r[i,j-imgRightGT[i,j]//2,0]=imgRight[i,j,0]
                r[i,j-imgRightGT[i,j]//2,1]=imgRight[i,j,1]
                r[i,j-imgRightGT[i,j]//2,2]=imgRight[i,j,2]
        except:
            pass

            

for i in range(imgLeft.shape[0]):
    for j in range(imgLeft.shape[1]):
                 
        if (l[i,j,:].sum()==0 and r[i,j,:].sum()==0):
            reconstructed[i,j,0]=reconstructed[i,j,1]=reconstructed[i,j,2]=0
        
        elif (l[i,j].sum()!=0 and r[i,j].sum()==0):            
            reconstructed[i,j,0]=l[i,j,0]
            reconstructed[i,j,1]=l[i,j,1]
            reconstructed[i,j,2]=l[i,j,2]
            
        elif (l[i,j].sum()==0 and r[i,j].sum()!=0):            
            reconstructed[i,j,0]=r[i,j,0]
            reconstructed[i,j,1]=r[i,j,1]
            reconstructed[i,j,2]=r[i,j,2]
            
        else:
                       
            reconstructed[i,j,0]=r[i,j,0]
            reconstructed[i,j,1]=r[i,j,1]
            reconstructed[i,j,2]=r[i,j,2]
            
cv2.imshow("Reconstructed",reconstructed.astype('uint8'))
 
blur=cv2.blur(reconstructed,(11,11))  

for i in range(imgLeft.shape[0]):
    for j in range(imgLeft.shape[1]):       
        if reconstructed[i,j,:].sum()==0:
                reconstructed[i,j,0]=blur[i,j,0]
                reconstructed[i,j,1]=blur[i,j,1]
                reconstructed[i,j,2]=blur[i,j,2]
        
        
cv2.imshow("R",r)
cv2.imshow("L",l)
cv2.imshow("filled Reconstructed",reconstructed.astype('uint8'))
cv2.waitKey(0)
cv2.destroyAllWindows()
