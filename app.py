from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image

# Load trained model
model = tf.keras.models.load_model("cifar10_model.h5")

# CIFAR-10 class names
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")  # HTML file for UI

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    image = Image.open(file).resize((32, 32))  # Resize image to 32x32
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension

    # Make prediction
    predictions = model.predict(image)
    predicted_class = class_names[np.argmax(predictions)]

    return jsonify({"prediction": predicted_class})

if __name__ == '__main__':
    app.run(debug=True)
