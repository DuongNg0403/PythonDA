import numpy as np

data = np.random.randn(2,3)
print(data, end="\n\n")
print(data*10, end="\n\n")
print(data+data, end="\n\n")
print(data.shape)

data1 = [[1,2,3,4],[4,1,2,3]]
arr1 = np.array(data1, dtype=np.float64)
print(arr1)
print(arr1.ndim)

print(np.arange(10))

#indexing
print(arr1[0][2])

#2x2x3
arr2 = np.array([[[1,2,3,4],[4,1,2,3]],arr1**2])
print(arr2)
print(arr2[1])
print(arr2[1][0])
print(arr2[1][0][1:3])

#Boolean Indexing
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)

print(names=="Bob")
print(data[names == "Bob"])
print(data[names == "Bob",1])
print(data[(names == "Bob") | (names == "Joe")])
print(data[data>1])


#Fancy Indexing
arr = np.empty((8, 4))
for i in range(8):
    arr[i]= i*i

print(arr)

#Transposing Arrays and Swapping Axes
arr = np.arange(10).reshape((2,5))
print(arr.transpose())

print(np.dot(arr.transpose(),arr))#produces symmetrical matrix



