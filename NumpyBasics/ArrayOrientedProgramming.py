import numpy as np 
import matplotlib.pyplot as plt
points = np.arange(-3,3,.01)

xs,ys = np.meshgrid(points,points)#meshgrid produces 2D matrices corresponding to all pair of (x,y) in the 2 arrays

print(xs)
print()
print(len(ys))
print()
z= np.sqrt(xs**2+ys**2)
print(z)

#plt.imshow(z, cmap= plt.cm.gray)
#plt.colorbar()
#plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
#plt.show()

#Expressing Conditional Logic as Array Operations
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

#take a value from xarr if cond at index == True and value from yarr otherwise
result = [(x if c else y) for x,y,c in zip(xarr,yarr,cond)]
print(result)

#better way to do the previous task
result = np.where(cond, xarr, yarr)
print(result)


###############STATISTICS#####################
arr = np.random.randn(5,4)

print(np.mean(arr))
print(arr.sum())

#Methods for Boolean Array
print((arr>1).any())
print((arr<2).all())
print(arr)
print(arr.sort(1))

#unique
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))



