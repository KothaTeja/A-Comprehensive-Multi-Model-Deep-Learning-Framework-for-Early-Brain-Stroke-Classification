from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.efficientnet import preprocess_input
import numpy as np
import os

app = Flask(__name__)

# Load model
MODEL_PATH = "stroke_classification_model.h5"
model = load_model(MODEL_PATH)

# Class labels (adjust order if needed to match your training generator)
class_labels = ["Bleeding", "Ischemia", "Normal"]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    filename = None
    if request.method == "POST":
        if "file" not in request.files:
            return "No file uploaded"
        
        file = request.files["file"]
        if file.filename == "":
            return "No image selected"
        
        if file:
            filepath = os.path.join("static", file.filename)
            file.save(filepath)
            
            # Preprocess image
            img = load_img(filepath, target_size=(224,224))
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)

            # Prediction
            preds = model.predict(img_array)
            pred_class = np.argmax(preds, axis=1)[0]
            prediction = f"Predicted: {class_labels[pred_class]} (Confidence: {np.max(preds):.2f})"
            filename = file.filename

    return render_template("index.html", prediction=prediction, filename=filename)

if __name__ == "__main__":
    app.run(debug=True)
