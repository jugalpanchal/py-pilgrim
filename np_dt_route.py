# pip install numpy
import numpy as np

# 1D Array - float64
np_array = np.random.rand(3) # type: float64
# Type
print(type(np_array))
#<class 'numpy.ndarray'>
print(np_array)
#  [0.80467563 0.9156837  0.90132778]


# 2D Array
np_2d_array = np.random.rand(3, 2)
print(type(np_2d_array))
#<class 'numpy.ndarray'>
print(np_2d_array)
# [[0.10347208 0.28300219]
#  [0.39800343 0.44153768]
#  [0.44318117 0.25506049]]
print(np_2d_array[2, 1])
# 0.2550604872076556
