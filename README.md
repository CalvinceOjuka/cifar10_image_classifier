Image Classifier Model
This project is an image classification model using TensorFlow and Flask. It loads a pre-trained model (cifar10_model.h5) and provides a web interface for users to upload images and receive predictions.

📂 Folder Structure

Image Classifier Model/
│── myenv/              # Virtual environment (dependencies installed here)
│── notebooks/          # Jupyter notebooks for model training/testing
│── templates/          # HTML templates for the Flask web interface
│── reports/            # Images for the outputs and graphs
│── app.py              # Flask application script
│── cifar10_model.h5    # Pre-trained Keras model
│── README.md           # Project documentation (this file)
│── requirement.txt     # Text file for required libraries

🔧 Setup Instructions
1️⃣ Install Python & Virtual Environment
Ensure you have Python installed (recommend Python 3.9+). Then, create and activate a virtual environment:

# Navigate to the project folder
cd "C:\Users\calvi\Desktop\Image Classifier Model"

# Create a virtual environment (if not created)
python -m venv myenv

# Activate virtual environment
myenv\Scripts\activate   # For Windows

2️⃣ Install Dependencies
Run the following command to install required packages:

pip install -r requirements.txt
If requirements.txt is missing, manually install the dependencies:

pip install tensorflow keras flask numpy pillow

3️⃣ Run Flask App
Once dependencies are installed, start the Flask web app:

python app.py
The application should start, and you can access it in your browser at:
http://127.0.0.1:5000/

🖼️ Model Details
The pre-trained model (cifar10_model.h5) is based on the CIFAR-10 dataset.
It classifies images into 10 categories (airplane, car, bird, cat, deer, dog, frog, horse, ship, truck).
The model is loaded using tf.keras.models.load_model("cifar10_model.h5").
Download the Model from https://1drv.ms/f/c/53479518717C5183/EhzcDxhZTZpHj7vBGBQVZjsBgml6dlupXdTTkVm-S7L-Zg?e=CwVmnV

📌 Troubleshooting
1️⃣ Flask Says "Template Not Found"
Ensure your templates folder contains the correct HTML files and is inside the main project folder.

2️⃣ Model File Not Found (FileNotFoundError)
Confirm that cifar10_model.h5 is inside the main project folder (as shown in your screenshot).

If the model is in another directory, update app.py to load it correctly:

import os
model_path = os.path.join(os.getcwd(), "cifar10_model.h5")
model = tf.keras.models.load_model(model_path)

3️⃣ Virtual Environment Not Activated
If python app.py fails, ensure your virtual environment is activated:

myenv\Scripts\activate   # Windows

📜 License
This project is for educational purposes. Feel free to modify and expand it.