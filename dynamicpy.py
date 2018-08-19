# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:31:57 2018

@author: Ankesh N. Bhoi
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

left_img = cv2.imread('C:/Users/Ankesh N. Bhoi/Desktop/CVIP/PA-2/view5.png', 0)  
right_img = cv2.imread('C:/Users/Ankesh N. Bhoi/Desktop/CVIP/PA-2/view1.png', 0)

displ=np.zeros(left_img.shape,'int64')
dispr=np.zeros(left_img.shape,'int64')
#Disparity Computation for Left Image
for x in range(left_img.shape[0]):
    OcclusionCost = 20 #(You can adjust this, depending on how much threshold you want to give for noise)
    
    #For Dynamic Programming you have build a cost matrix. Its dimension will be numcols x numcols
    
    CostMatrix = np.zeros((left_img.shape[1],left_img.shape[1]),'int64')
    DirectionMatrix = np.zeros((left_img.shape[1],left_img.shape[1]),'int')  #(This is important in Dynamic Programming. You need to know which direction you need traverse)
    
    #We first populate the first row and column values of Cost Matrix
    
    for i in range(CostMatrix.shape[1]):
         CostMatrix[i,0] = i*OcclusionCost
         CostMatrix[0,i] = i*OcclusionCost
         
    for i in range(1,CostMatrix.shape[1]):
        for j in range(1,CostMatrix.shape[1]):
            min1=CostMatrix[i-1,j-1]+abs(right_img[x,j]-left_img[x,i])
            min2=CostMatrix[i-1,j]+OcclusionCost
            min3=CostMatrix[i,j-1]+OcclusionCost
            CostMatrix[i,j]=cmin=min([min1,min2,min3])
            if(min1==cmin):
                DirectionMatrix[i,j]=1
            if(min2==cmin):
                DirectionMatrix[i,j]=2
            if(min3==cmin):
                DirectionMatrix[i,j]=3
    
    ctr=p=q=CostMatrix.shape[1]-1
    
    while(p!=0 and q!=0):
        if DirectionMatrix[p,q]==1:
            displ[x,p]=abs(p-q)            
            p-=1
            q-=1
            ctr-=1
        elif DirectionMatrix[p,q]==2:
            p-=1
        elif DirectionMatrix[p,q]==3:
            q-=1
    # Now, its time to populate the whole Cost Matrix and DirectionMatrix
    
    # Use the pseudocode from "A Maximum likelihood Stereo Algorithm" paper given as reference
cv2.imshow(" dynamic disparity left",displ.astype('uint8'))

for x in range(left_img.shape[0]):
    OcclusionCost = 20 #(You can adjust this, depending on how much threshold you want to give for noise)
    
    #For Dynamic Programming you have build a cost matrix. Its dimension will be numcols x numcols
    
    CostMatrix = np.zeros((left_img.shape[1],left_img.shape[1]),'int64')
    DirectionMatrix = np.zeros((left_img.shape[1],left_img.shape[1]),'int')  #(This is important in Dynamic Programming. You need to know which direction you need traverse)
    
    #We first populate the first row and column values of Cost Matrix
    
    for i in range(CostMatrix.shape[1]):
         CostMatrix[i,0] = i*OcclusionCost
         CostMatrix[0,i] = i*OcclusionCost
         
    for i in range(1,CostMatrix.shape[1]):
        for j in range(1,CostMatrix.shape[1]):
            min1=CostMatrix[i-1,j-1]+abs(right_img[x,i]-left_img[x,j])
            min2=CostMatrix[i-1,j]+OcclusionCost
            min3=CostMatrix[i,j-1]+OcclusionCost
            CostMatrix[i,j]=cmin=min([min1,min2,min3])
            if(min1==cmin):
                DirectionMatrix[i,j]=1
            if(min2==cmin):
                DirectionMatrix[i,j]=2
            if(min3==cmin):
                DirectionMatrix[i,j]=3 
    
    ctr=p=q=CostMatrix.shape[1]-1
    
    while(p!=0 and q!=0):
        if DirectionMatrix[p,q]==1:
            dispr[x,p]=abs(p-q)            
            p-=1
            q-=1
            ctr-=1
        elif DirectionMatrix[p,q]==2:
            p-=1
        elif DirectionMatrix[p,q]==3:
            q-=1
    # Now, its time to populate the whole Cost Matrix and DirectionMatrix
    
    # Use the pseudocode from "A Maximum likelihood Stereo Algorithm" paper given as reference
cv2.imshow(" dynamic disparity right",dispr.astype('uint8'))

cv2.waitKey(0)
cv2.destroyAllWindows()    