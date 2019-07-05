import tensorflow as tf
mat0 = tf.constant([[0,0,0],[0,0,0]])
mat1 = tf.zeros([2,3])
mat2 = tf.ones([2,3])
with tf.Session() as sess:
    print(sess.run(mat1))
    print(sess.run(mat2))
