import numpy as np
data1 = np.array([1, 2, 3, 4, 5])
print(data1)
data2 = np.array([[1,2],
                  [3,4]])
print(data2)
print(data1.shape, data2.shape)


# 基本运算
data3 = np.ones([2, 3])
print(data3*2)
print(data3/3)
print(data3+2)

data4 = np.array([[1,2,3],
                  [4,5,6]])
print(data3+data4)
print(data3*data4)