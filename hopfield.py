import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

class HopfieldNetwork:
    def __init__(self, master, network):
        self.master = master
        self.network = network

        self.canvas_size = 300
        self.pixel_size = self.canvas_size // 10
        self.canvas = tk.Canvas(self.master, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.button = tk.Button(self.master, text="Recognize", command=self.recognize)
        self.button.pack()

        self.image_array = np.ones((10, 10), dtype=int)

    def on_canvas_click(self, event):
        x = event.x // self.pixel_size
        y = event.y // self.pixel_size
        self.toggle_pixel(x, y)

    def toggle_pixel(self, x, y):
        self.image_array[y, x] = -1 if self.image_array[y, x] == 1 else 1
        color = 'black' if self.image_array[y, x] == -1 else 'white'
        x0 = x * self.pixel_size
        y0 = y * self.pixel_size
        x1 = x0 + self.pixel_size
        y1 = y0 + self.pixel_size
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    def recognize(self):
        pattern = self.image_array.flatten()
        retrieved_pattern = self.network.recall(pattern)
        retrieved_image = retrieved_pattern.reshape((10, 10))

        image = Image.fromarray(np.uint8((retrieved_image + 1) * 255))
        image = image.resize((self.canvas_size, self.canvas_size))
        photo = ImageTk.PhotoImage(image)

        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=photo)
        self.canvas.image = photo

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

# Guardar la red entrenada en un archivo
import pickle

with open("hopfield_network.pkl", "wb") as file:
    pickle.dump(network, file)
