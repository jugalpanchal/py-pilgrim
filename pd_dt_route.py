# pip install numpy
# pip install pandas

import numpy as np
import pandas as pd

# 1D Array
np_array = np.random.rand(3) # type: float64
print(type(np_array))
# <class 'numpy.ndarray'>
print(np_array)
# [0.07438286 0.64987328 0.32785387]


# Pandas Series - contains labels
first_series = pd.Series(np_array) # class: Series class
print(type(first_series))
# <class 'pandas.core.series.Series'>
print(first_series)
# 0    0.074383
# 1    0.649873
# 2    0.327854


# Pandas Series - custom labels
second_series = pd.Series(np_array, index = ["First", "Second", "Third"])
print(type(second_series))
# <class 'pandas.core.series.Series'>
print(second_series)
# First     0.816091
# Second    0.622287
# Third     0.154517
print(second_series[1]) # apply index
# 0.622287
print(second_series["Second"]) # apply custom index
# 0.622287
print(second_series.index)
# Index(['First', 'Second', 'Third'], dtype='object')



# 2D Array
np_2d_array = np.random.rand(3, 2)
print(type(np_2d_array))
#<class 'numpy.ndarray'>
print(np_2d_array)
# [[0.4291743  0.41552642]
#  [0.24572321 0.04125593]
#  [0.34186999 0.25560191]]
print(np_2d_array[2, 1])
# 0.2556019147619174


# Pandas DataFrame - along with row and col index/label
first_df = pd.DataFrame(np_2d_array) # class: DataFrame
print(type(first_df))
# <class 'pandas.core.frame.DataFrame'>
print(first_df) # prints values with index
#           0         1
# 0  0.429174  0.415526
# 1  0.245723  0.041256
# 2  0.341870  0.255602
# print(first_df[2,1]) # it fails :) - KeyError: (2, 1)
print(first_df.columns)
# RangeIndex(start=0, stop=2, step=1)
first_df.columns = ["First", "Second"]
print(first_df)
#       First    Second
# 0  0.429174  0.415526
# 1  0.245723  0.041256
# 2  0.341870  0.255602
print(first_df["Second"]) # It returns a series now.
# 0    0.415526
# 1    0.041256
# 2    0.255602
# print(first_df[1, "second"]) # it fails :) - KeyError: (1, 'second')
print(first_df['Second'].values[1]) # the values gives a numpy array.
# 0.0412559339792629

# iat, at, iloc, loc
print(first_df.iat[1, 1])
# 0.04125593397926297
print(first_df.at[1, "Second"])
# 0.04125593397926297
print(first_df.iloc[1])
# First     0.245723
# Second    0.041256
print(first_df.iloc[1, 1])
# 0.04125593397926297
print(first_df.iloc[1]["Second"])
# 0.04125593397926297
