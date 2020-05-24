import numpy as np

arr = np.arange(10)

np.save("some_array.npy", arr)
z = np.load("some_array.npy")

np.savez("some_array.npz",arr =arr, z=z)
loaded = np.load("some_array.npz")
print(loaded["z"])

