import numpy as np
ar1=np.array([[1,2],[5,6]])
ar2=np.array([[5,3],[6,9]])
j=np.concatenate((ar1,ar2),axis=1)
print(ar1)
print(ar2)
print(j)