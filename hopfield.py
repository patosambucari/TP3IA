import numpy as np

class HopfieldNetwork:
    def __init__(self, pattern_size):
        self.pattern_size = pattern_size
        self.weights = np.zeros((pattern_size, pattern_size))

    def train(self, patterns):
        for pattern in patterns:
            pattern = pattern.reshape(-1, 1)
            self.weights += np.dot(pattern, pattern.T)

    def predict(self, image):
        image = image.reshape(-1, 1)
        output = np.dot(self.weights, image)
        output[output >= 0] = 1
        output[output < 0] = -1
        output = output.reshape(self.pattern_size)
        return output

        