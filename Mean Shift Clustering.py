import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import cv2
import random

img = cv2.imread('C:/Users/Ankesh N. Bhoi/Desktop/CVIP/PA-2/butterfly.jpg', 1)  
    

img=img[::3,::3,:]


rgb_data=[np.append(img[i][j],[i,j]) for i in range(img.shape[0]) for j in range(img.shape[1])]
pts = len(rgb_data)
rad = 30
X = np.array(rgb_data)
# =============================================================================
# 
# X =np.array([[1, 0, 0],
#     [0, 1, 0],
#     [0, 0, 0],
#    [0, 1, 4],
#     [1, 0, 4],
#     [0, 0, 4],
#    [5, 0, 6],
#     [0, 5, 6],
#     [3, 5, 6],
#    [7, 0, 8],
#     [0, 7, 8],
#     [7, 3,8]])
# =============================================================================
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X[:pts,0], X[:pts,1], X[:pts,2], c='y', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

class Mean_Shift:
    def __init__(self, radius=rad):
        self.radius = radius

    def fit(self, data):
        centroids = {}

        for i in range(0,len(data),1):
            centroids[i] = data[i]
# =============================================================================
#         random.seed(123)
#         random.shuffle(data)
#         for i in range(len(data)//100):    
#             centroids[i] = data[i]
# =============================================================================
        iteration=0
        while True:
            iteration+=1
            print(iteration,"centroids:",len(centroids))
            new_centroids = []
            #for i in centroids:
                #print(iteration,"centroids:",len(centroids),100*i/len(centroids),'%')
                #in_bandwidth = []
                #centroid = centroids[i]
                #in_bandwidth=[featureset for featureset in data if np.linalg.norm(featureset-centroids[i]) < self.radius]
# =============================================================================
#                 for featureset in data:
#                     if np.linalg.norm(featureset-centroid) < self.radius:
#                         in_bandwidth.append(featureset)
# =============================================================================

                #new_centroid = np.average(in_bandwidth,axis=0)
            new_centroids=[tuple(np.average([featureset for featureset in data if np.linalg.norm(featureset-centroids[i]) < self.radius],axis=0)) for i in centroids]

            uniques = sorted(list(set(new_centroids)))

            prev_centroids = dict(centroids)

            centroids = {}
            for i in range(len(uniques)):
                centroids[i] = np.array(uniques[i])

            optimized = True

            for i in centroids:                
                if not np.array_equal(centroids[i], prev_centroids[i]):
                    optimized = False
                if not optimized:
                    break
                
            if optimized:
                break

        self.centroids = centroids



clf = Mean_Shift()
clf.fit(X[:pts])

centroids = clf.centroids

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X[:pts,0], X[:pts,1], X[:pts,2], c='y', marker='o')
for c in centroids:
    ax.scatter(centroids[c][0], centroids[c][1],centroids[c][2],c='r', marker='*')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

clusters=np.zeros(img.shape)



for pt in X:
    for i in centroids:        
        if(np.linalg.norm(pt-centroids[i])<rad):
            clusters[pt[-2],pt[-1],0]=centroids[i][0]
            clusters[pt[-2],pt[-1],1]=centroids[i][1]
            clusters[pt[-2],pt[-1],2]=centroids[i][2]

cv2.imshow("clusters",clusters.astype('uint8'))       
cv2.waitKey(0)
cv2.destroyAllWindows()      
    
        

