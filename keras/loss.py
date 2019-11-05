import numpy as np
from keras import backend as K

a = np.array([1, 2, 3])
b = K.sum(a, axis=-1)
print(b)
print(K.eval(b))

c = K.mean(K.constant(a), axis=-1)
print(K.eval(c))
