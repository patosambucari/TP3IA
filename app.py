from flask import Flask, render_template, request, jsonify
import pickle
from hopfield import HopfieldNetwork

app = Flask(__name__)

# Cargar la red de Hopfield entrenada desde el archivo
with open("hopfield_network.pkl", "rb") as file:
    network = pickle.load(file)

# Ruta inicial para cargar la página
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para reconocer el patrón enviado desde el frontend
@app.route("/recognize", methods=["POST"])
def recognize():
    # Obtener los datos de la imagen del cuerpo de la solicitud
    image_data = request.json["image_data"]

    # Reconocer el patrón utilizando la red de Hopfield
    retrieved_pattern = network.recall(image_data)

    # Devolver el patrón reconocido como respuesta JSON
    return jsonify({"retrieved_pattern": retrieved_pattern})

if __name__ == "__main__":
    app.run()
