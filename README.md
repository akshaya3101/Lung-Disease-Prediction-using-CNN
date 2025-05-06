**Lung Disease Prediction Using CNN**

This project implements a Convolutional Neural Network (CNN) model to predict lung health status from chest X-ray images. The web application is built using Flask to provide a simple, interactive interface where users can upload lung X-ray images and get instant predictions.

Key Features
🧠 Deep Learning Model: Trained CNN model classifies lung images into:

Healthy
Type 1 Disease
Type 2 Disease

🌐 Web Application:
Built with Flask.
Upload X-ray images via the browser.
Displays the predicted class along with the uploaded image.

⚙️ Model Input:
Accepts image files (e.g., PNG, JPG).
Images are resized and normalized before prediction.

**Files in This Repository**
CNN - lung disease prediction.ipynb: Jupyter Notebook containing the full code for building, training, and evaluating the CNN model on a custom lung disease dataset.

app.py: Flask web application script that loads the trained CNN model and handles image upload, preprocessing, prediction, and display of results.

templates/index.html & templates/result.html: (Not uploaded here) These should be the HTML templates for the homepage and result display page.
