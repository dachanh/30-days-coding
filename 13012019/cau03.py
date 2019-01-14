import numpy as  np
import matplotlib.pyplot as  plt

a = np.array([[1,2,3,4],
              [4,5,5,4],
              [9,4,5,3],
              [1,7,6,6],
              [1,7,6,6]],dtype=np.uint8)
b = np.ones((4,4),dtype=np.uint8)
res = np.zeros((5,4),dtype=np.uint8)
for x in range(5):
    for y in range(4):
        res[x,y] = sum(abs(a[x,:] - b[:,y]))
print(res)
for i in range(res.shape[0]):
    print(np.amin(res[i,:]))
