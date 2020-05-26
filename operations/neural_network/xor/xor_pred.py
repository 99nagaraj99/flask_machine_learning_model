import numpy as np
import pickle
import os


def predict_xor_output(num1, num2):
    """
    Predict xor
    :param num1:
    :param num2:
    :return:
    """
    path = os.path.split(os.path.abspath(__file__))[0]
    output = {'output_prediction_of_xor': 0}
    x_input = np.array([num1, num2]).reshape(1, 2)
    file_name = 'xor_model.pkl'
    abs_path = path + '/' + file_name
    m1 = pickle.load(open(abs_path, 'rb'))
    output['output_prediction_of_xor'] = int(m1.predict(x_input)[0])
    # print(output)
    return output
