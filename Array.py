
#install package for array "pip install numpy"

#import numpy

"""import numpy as np  # allis name as np for numpy


#a=numpy.array([1,2,3,4,5])

a=np.array([1,2,3,4,5])
print(a)
print(type(a))

#to check numpy version

print(np.__version__)"""




#matplotlib install=====pip install matplotlib
#Matplotlib is low level graph plotting library

import matplotlib.pyplot as mp

import numpy as np

#check version
#print(mp.__version__)

x1=input("Enter x1 : ")
x2=input("Enter x2 : ")
y1=input("Enter y1 : ")
y2=input("Enter y2 : ")

x=np.array([x1,x2])
y=np.array([y1,y2])

mp.plot(x,y)
mp.show()



