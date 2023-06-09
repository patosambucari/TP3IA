import numpy as np

class HopfieldNetwork:
    def __init__(self, pattern_size):
        self.pattern_size = pattern_size
        self.weights = np.zeros((pattern_size, pattern_size))

    def train(self, patterns):
        for pattern in patterns:
            pattern = np.array(pattern)
            pattern = pattern.reshape(-1, 1)
            self.weights += np.dot(pattern, pattern.T)
            np.fill_diagonal(self.weights, 0)

    def recall(self, pattern):
        pattern = np.array(pattern)
        pattern = pattern.reshape(-1, 1)
        old_pattern = np.zeros(pattern.shape)
        while not np.array_equal(old_pattern, pattern):
            old_pattern = pattern.copy()
            pattern = np.sign(np.dot(self.weights, pattern))
        return pattern.flatten()

    def predict(self, image):
        image = image.reshape(-1, 1)
        output = np.dot(self.weights, image)
        output[output >= 0] = 1
        output[output < 0] = -1
        output = output.reshape(self.pattern_size)
        return output

# Patrones de entrenamiento (imágenes de 10x10 píxeles)
patterns = [
    [-1, 1, 1, 1, 1, 1, 1, 1, 1, -1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     -1, 1, 1, 1, 1, 1, 1, 1, 1, -1],

    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],

    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

    [1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     -1, 1, -1, -1, -1, -1, -1, -1, 1, -1,
     -1, -1, 1, -1, -1, -1, -1, 1, -1, -1,
     -1, -1, -1, 1, -1, -1, 1, -1, -1, -1,
     -1, -1, -1, -1, 1, 1, -1, -1, -1, -1,
     -1, -1, -1, -1, 1, 1, -1, -1, -1, -1,
     -1, -1, -1, 1, -1, -1, 1, -1, -1, -1,
     -1, -1, 1, -1, -1, -1, -1, 1, -1, -1,
     -1, 1, -1, -1, -1, -1, -1, -1, 1, -1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1],

    [1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
     -1, 1, -1, -1, -1, -1, -1, -1, 1, -1,
     -1, -1, 1, -1, -1, -1, -1, 1, -1, -1,
     -1, -1, -1, 1, -1, -1, 1, -1, -1, -1,
     -1, -1, -1, -1, 1, 1, -1, -1, -1, -1,
     -1, -1, -1, -1, 1, 1, -1, -1, -1, -1,
     -1, -1, -1, 1, -1, -1, 1, -1, -1, -1,
     -1, -1, 1, -1, -1, -1, -1, 1, -1, -1,
     -1, 1, -1, -1, -1, -1, -1, -1, 1, -1,
     1, -1, -1, -1, -1, -1, -1, -1, -1, 1]
]

# Crear una instancia de la red de Hopfield
network = HopfieldNetwork(pattern_size=100)

# Entrenar la red con los patrones de entrenamiento
network.train(patterns)

# Imagen de prueba
test_image = np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                       -1, -1, -1, -1,  1,  1, -1, -1, -1, -1,
                       -1, -1, -1,  1, -1, -1,  1, -1, -1, -1,
                       -1, -1,  1, -1, -1, -1, -1,  1, -1, -1,
                       -1,  1, -1, -1, -1, -1, -1, -1,  1, -1,
                       -1,  1, -1, -1, -1, -1, -1, -1,  1, -1,
                       -1, -1,  1, -1, -1, -1, -1,  1, -1, -1,
                       -1, -1, -1,  1, -1, -1,  1, -1, -1, -1,
                       -1, -1, -1, -1,  1,  1, -1, -1, -1, -1,
                       -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,])

# Realizar la predicción utilizando la red de Hopfield
predicted_image = network.predict(test_image)

# Imprimir los resultados
print("Imagen original:")
print(test_image.reshape(10, 10))
print("\nImagen reconstruida:")
print(predicted_image.reshape(10, 10))