import numpy as np
import tensorflow as tf
from keras.layers.embeddings import Embedding
from keras.models import Sequential

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

model = Sequential()
model.add(Embedding(7, 3, input_length=5))
input_array = np.array([[0, 1, 2, 3, 4], [5, 2, 2, 3, 6]])

print(input_array)
output_array = model.predict(input_array)
print(output_array)
