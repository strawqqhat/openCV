import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
data = np.linspace(1, 15, 15)
endPrice = np.array([2511.90,2538.26,2510.68,2591.66,2732.98,2701.69,2600,2233,2424,2242,2324,2324,2545,2645,2435])
beginPrice = np.array([2501.90,2438.26,2610.68,2791.66,2932.98,2901.69,2400,2533,2024,2142,2224,2024,2045,2945,2635])
print(data)
plt.figure()
for i in range(0, 15):
    dataOne = np.zeros([2])
    dataOne[0] = i
    dataOne[1] = i
    priceOne = np.zeros([2])
    priceOne[0] = beginPrice[i]
    priceOne[1] = endPrice[i]
    if endPrice[i] > beginPrice[i]:
        plt.plot(dataOne, priceOne, 'r', lw=10)
    else:
        plt.plot(dataOne, priceOne, 'g', lw=10)

dataNormal = np.zeros([15, 1])
priceNormal = np.zeros([15, 1])
for i in range(0, 15):
    dataNormal[i, 0] = i/14.0
    priceNormal[i, 0] = endPrice[i]/3000.0
x = tf.placeholder(tf.float32, [None, 1])
y = tf.placeholder(tf.float32, [None, 1])

w1 = tf.Variable(tf.random_uniform([1, 10], 0.1))
b1 = tf.Variable(tf.zeros([1, 10]))
wb1 = tf.matmul(x, w1)+b1

# 加一个激励函数
layer1 = tf.nn.relu(wb1)

w2 = tf.Variable(tf.random_uniform([10, 1],0,1))
b2 = tf.Variable(tf.zeros([15,1]))
wb2 = tf.matmul(layer1,w2)+b2
layer2 = tf.nn.relu(wb2)
loss = tf.reduce_mean(tf.square(y-layer2))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(0, 10000):
        sess.run(train_step,feed_dict={x:dataNormal, y:priceNormal})
    pred = sess.run(layer2,feed_dict={x:dataNormal})
    predPrice = np.zeros([15, 1])
    for i in range(0, 15):
        predPrice[i, 0] = (pred*3000)[i, 0]
    plt.plot(data, predPrice, 'b', lw=1)
plt.show()

