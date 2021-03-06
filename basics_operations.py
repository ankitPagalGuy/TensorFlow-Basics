import tensorflow as tf

a = tf.constant(5)
b = tf.constant(6)

with tf.Session() as sess:
	print('a=5, b=6')
	print('Addition with constants: %i' % sess.run(a+b))
	print('Multipications with constants: %i' % sess.run(a*b))



a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

add = tf.add(a , b)
mul = tf.multiply(a , b)

with tf.Session() as sess:
	print("Addition with variables: %i" % sess.run(add , feed_dict={a: 2, b: 3}))
	print("Multipications with variables: %i" % sess.run(mul, feed_dict={a: 2, b: 3}))


# 1 cross 2 matrix -> 1 row , 2 columna
matrix1 = tf.constant([[3., 3.]])

# 2 cross 1 matrix -> 2 row , 1 column
matrix2 = tf.constant([[2.],[2.]])

product = tf.matmul(matrix1, matrix2)

with tf.Session() as sess:
	result = sess.run(product)
	print(result)

