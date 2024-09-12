from flask import Flask, render_template, request, redirect, url_for, flash
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
from werkzeug.utils import secure_filename

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages
model = load_model("brain_tumor_detection_model.keras")  # Load your pre-trained model

# Define tumor categories
categories = ["Glioma", "Meningioma", "No Tumor", "Pituitary"]

# Set the folder to save uploaded images
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Preprocess the image for prediction
        img = load_img(file_path, target_size=(150, 150))
        img = img_to_array(img)
        img = np.expand_dims(img, axis=0) / 255.0

        # Perform prediction
        prediction = model.predict(img)
        predicted_class = categories[np.argmax(prediction)]
        confidence = round(np.max(prediction) * 100, 2)

        # Render result page with prediction and image
        return render_template('result.html', 
                               prediction=predicted_class, 
                               confidence=confidence, 
                               image_file=filename)
    else:
        flash('Allowed file types are png, jpg, jpeg, gif')
        return redirect(url_for('index'))

# Route for About page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for Services page
@app.route('/services')
def services():
    return render_template('services.html')

# Route for Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)