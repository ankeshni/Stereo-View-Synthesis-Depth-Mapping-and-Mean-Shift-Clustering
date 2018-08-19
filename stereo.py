# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 23:08:45 2018

@author: Ankesh N. Bhoi
"""

import numpy as np
from sklearn.preprocessing import normalize
import cv2
from scipy import signal
imgLeft = cv2.imread('C:/Users/Ankesh N. Bhoi/Desktop/CVIP/PA-2/view5.png', 0)  
imgRight = cv2.imread('C:/Users/Ankesh N. Bhoi/Desktop/CVIP/PA-2/view1.png', 0)

lmap=np.zeros(imgLeft.shape,'uint8')
rmap=np.zeros(imgRight.shape,'uint8')

block=3

for i in range(0,imgLeft.shape[0]-block,1):
    print((i+1)*100/imgLeft.shape[0],'%')
    for j in range(0,imgLeft.shape[1]-block,1):
        bl=imgLeft[i:i+block,j:j+block]
        ssd=1000000       
        for k in range(j,imgRight.shape[1]-block,1):
            calc=((bl-imgRight[i:i+block,k:k+block])**2).sum()           
            if(calc<ssd):
                #print(bl,imgRight[i:i+block,k:k+block])
                ssd=calc
                #print(ssd)
                lmap[i:i+block,j:j+block].fill(k-j)

cv2.imshow("l disparityeq",cv2.equalizeHist(lmap.astype('uint8')))
cv2.imshow("l disparity",lmap.astype('uint8'))
cv2.imshow("l ",imgLeft)
cv2.imshow("r ",imgRight)
#cv2.waitKey(0)

for i in range(imgLeft.shape[0]-1,block,-1):
    print((imgLeft.shape[0]-i-1)*100/imgLeft.shape[0],'%')
    for j in range(imgLeft.shape[1]-1,block,-1):
        bl=imgRight[i:i-block:-1,j:j-block:-1]
        #print(bl,i,j)
        ssd=1000000       
        for k in range(j,block,-1):
            calc=((bl-imgLeft[i:i-block:-1,k:k-block:-1])**2).sum()
            if(calc<ssd):
                #print(bl,imgRight[i:i+block,k:k+block])
                ssd=calc
                #print(ssd)
                rmap[i:i-block:-1,j:j-block:-1].fill(j-k)
cv2.imshow("r disparityeq",cv2.equalizeHist(rmap.astype('uint8')))
cv2.imshow(" rdisparity",rmap.astype('uint8'))
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# =============================================================================
# Consistency check
# =============================================================================
imgLeftGT = cv2.imread('C:/Users/Ankesh N. Bhoi/Desktop/CVIP/PA-2/disp5.png', 0)  
imgRightGT = cv2.imread('C:/Users/Ankesh N. Bhoi/Desktop/CVIP/PA-2/disp1.png', 0) 

l=np.array(lmap[:,:])
r=np.array(rmap[:,:])

for i in range(imgLeft.shape[0]):
    for j in range(imgLeft.shape[1]):
        if lmap[i][j]!=rmap[i][j+lmap[i][j]]:
           l[i][j]=0 

for i in range(imgLeft.shape[0]):
    for j in range(imgLeft.shape[1]):
        if rmap[i][j]!=lmap[i][j-rmap[i][j]]:
           r[i][j]=0            

l_mse=((imgLeftGT.astype('int')-lmap.astype('int'))**2).mean()
r_mse=((imgRightGT.astype('int')-rmap.astype('int'))**2).mean()

l_mse_consistent=np.zeros_like(l)
for i in range(l.shape[0]):
    for j in range(l.shape[1]):
        if l[i,j].astype('int')!=0:
            l_mse_consistent[i,j]=(imgLeftGT[i,j]-l[i,j])**2
            
r_mse_consistent=np.zeros_like(r)
for i in range(r.shape[0]):
    for j in range(r.shape[1]):
        if r[i,j]!=0:
            r_mse_consistent[i,j]=(imgRightGT[i,j]-r[i,j])**2
            

l_mse_consistent=l_mse_consistent.mean()
r_mse_consistent=r_mse_consistent.mean()

cv2.imshow("l consistent",l.astype('uint8'))   
cv2.imshow("r consistent",r.astype('uint8'))        

       
cv2.waitKey(0)
cv2.destroyAllWindows()      
    
