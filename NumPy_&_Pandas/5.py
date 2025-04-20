import numpy as np


Marks = np.array([[45,35,64],[34,64,36],[43,65,74],[46,46,74],[37,54,32]])

x = np.mean(Marks,axis=1)

y = np.mean(Marks,axis=0)

print("Average marks of each student: ",x)

print("subject with the highest average: ",np.max(y))