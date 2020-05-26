import numpy as np
import pickle
from sklearn.neural_network import MLPClassifier

xs = np.array([0, 0, 0, 1, 1, 0, 1, 1]).reshape(4, 2)
ys = np.array([0, 1, 1, 0]).reshape(4,)

model = MLPClassifier(activation='relu', max_iter=10000, hidden_layer_sizes=(4, 2))
model.fit(xs, ys)
file_name = 'xor_model.pkl'
pickle.dump(model, open(file_name, 'wb'))