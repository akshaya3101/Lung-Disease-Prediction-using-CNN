from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import io
import os
from PIL import Image
import base64

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('cnn_custom_dataset_model.h5')

# Map class indices to labels
class_labels = {0: "Healthy", 1: "Type 1 Disease", 2: "Type 2 Disease"}

# Function to preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0  # Scale pixels to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to display prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    # Save the uploaded file to process
    img_path = os.path.join('uploads', file.filename)
    os.makedirs('uploads', exist_ok=True)  # Ensure the uploads folder exists
    file.save(img_path)
    
    # Preprocess the image and make prediction
    img = preprocess_image(img_path)
    predictions = model.predict(img)
    predicted_class = np.argmax(predictions, axis=-1)[0]
    predicted_label = class_labels.get(predicted_class, "Unknown")

    # Prepare the image to show on the front end
    img = Image.open(img_path)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return render_template('result.html', prediction=predicted_label, image_data=img_str)


if __name__ == '__main__':
    app.run(debug=False, port=700)
