'''
import tensorflow as tf
data1 = tf.placeholder(tf.float32)
data2 = tf.placeholder(tf.float32)
dataAdd = tf.add(data1,  data2)
with tf.Session() as sess:
    print(sess.run(dataAdd, feed_dict={data1:6, data2:2}))
print('end')
'''

import tensorflow as tf
data1 = tf.constant([[6, 6]])
data2 = tf.constant([[2],
                     [2]])
data3 = tf.constant([[3, 3]])
data4 = tf.constant([[1, 2],
                    [3, 4],
                    [5, 6]])
print(data4.shape)
with tf.Session() as sess:
    print(sess.run(data4))
    print(sess.run(data4[0]))
    print(sess.run(data4[:, 0]))
    print(sess.run(data4[0][0]))