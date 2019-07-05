import tensorflow as tf
data1 = tf.constant(2.5)
data2 = tf.Variable(10, name='var')
print(data1)
print(data2)

sess = tf.Session()
print(sess.run(data1))
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(data2))