result.html file

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prediction Result</title>
</head>
<body>
    <h1>Prediction Result</h1>
    <p>Predicted Class: {{ prediction }}</p>
    <img src="data:image/png;base64,{{ image_data }}" alt="Uploaded Image">
    <br><a href="{{ url_for('index') }}">Go Back</a>
</body>
</html>