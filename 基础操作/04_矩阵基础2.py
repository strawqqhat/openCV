import tensorflow as tf
data1 = tf.constant([[6, 6]])
data2 = tf.constant([[2],
                     [2]])
data3 = tf.constant([[3, 3]])
data4 = tf.constant([[1,2],
                     [3,4],
                     [5,6]])
matMul = tf.matmul(data1, data2)
matAdd = tf.add(data1, data3)
with tf.Session() as sess:
    print(sess.run(matMul))
    print(sess.run(matAdd))
    print(sess.run([matMul, matAdd]))