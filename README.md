# NeuraScan - Brain Tumor Detection App

![Brain Tumor Detection](https://media.istockphoto.com/id/1250205787/photo/brain-tumor.jpg?s=612x612&w=0&k=20&c=iu9lulr9RpYsFA2r8NqdEAzxxewm4jNNaH4hV3IAY-0=)

## Overview

**NeuraScan** is a machine learning-based web application designed to detect and classify brain tumors from MRI scans. This project utilizes a deep learning model that predicts the type of tumor, such as **Glioma**, **Meningioma**, **Pituitary Tumor**, or **No Tumor**, with a high degree of accuracy. The application provides valuable recommendations based on the analysis, making it an essential tool for early detection and medical consultation.

## Features

- **User-Friendly Interface**: A sleek, modern UI with an easy-to-use file upload mechanism.
- **Accurate Predictions**: The app leverages a trained machine learning model to classify brain tumors.
- **Recommendations**: Provides tailored next steps and recommendations based on the prediction result.
- **Tumor Information**: Offers detailed information about different types of brain tumors.

![image](https://github.com/user-attachments/assets/bef721ee-eb24-4cd2-8825-573b7c1cd0aa)
![image](https://github.com/user-attachments/assets/b172230b-55a5-4b6f-9ab5-06295567ad7b)



## Technologies Used

- **Frontend**: HTML, CSS (Bootstrap), JavaScript (for file handling and UI)
- **Backend**: Python (Flask)
- **Machine Learning**: Trained deep learning model (TensorFlow/Keras)
- **File Handling**: Uploads MRI scans in various formats (JPEG, PNG)
- **Deployment**: Works locally or can be deployed to any cloud provider (Heroku, AWS, etc.)

## Installation and Setup

To set up the project locally, follow these steps:

### Prerequisites

- Python 3.x
- Flask
- TensorFlow/Keras
- Jupyter (Optional, for model testing)
- Git (for cloning the repository)

### Steps

1. **Clone the Repository**

   First, clone the project repository from GitHub:
   ```bash
   git clone https://github.com/your-username/brain-tumor-detection.git
   cd brain-tumor-detection
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**
   
   It's a good practice to use a virtual environment to isolate dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install all necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Trained Model**

   You need to place the trained deep learning model in the `root` directory. If you haven't trained a model yet, you can use a pre-trained one (optional). For this project, make sure the model file is named `brain_tumor_detection_model.keras` and placed in the `root` directory.

5. **Set Up Flask Environment Variables**

   Create a `.env` file in the root directory and define your Flask environment variables:
   ```bash
   FLASK_APP=app.py
   FLASK_ENV=development
   ```

6. **Run the Application**

   Use Flask to start the server:
   ```bash
   flask run
   ```

7. **Access the Application**

   Once the server is running, open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

   From there, you can upload an MRI image and get predictions.

## Project Directory Structure

```plaintext
brain-tumor-detection/
├── app.py               # Main Flask application file
├── model/               # Directory containing the trained model
│   └── brain_tumor_detection_model.keras    # Pre-trained model for prediction
├── static/              # Static files (CSS, JS, Images)
├── templates/           # HTML templates for Flask views
│   ├── index.html        # Homepage for file upload
│   └── result.html       # Analysis result page
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation (this file)
```

## Running the Model

The app uses a trained machine learning model to predict the type of tumor from an MRI image. If you have your own model, ensure it's compatible and place it in the `root` directory.

## Prediction Types

The app classifies brain MRI scans into four categories:

- **Glioma**: Aggressive tumors originating from glial cells.
- **Meningioma**: Typically benign tumors arising from the meninges.
- **Pituitary Tumor**: Benign tumors near the pituitary gland.
- **No Tumor**: Indicates no detectable brain tumor in the MRI scan.

## Model Performance Metrics

### Accuracy Graph

![Model Accuracy](![image](https://github.com/user-attachments/assets/8b574e70-43df-4f39-ba32-bea32ebd5a15)
)

### Loss Graph

![Loss Graph](![image](https://github.com/user-attachments/assets/3198ff1e-7fee-48f5-91d6-5c8bda6940bd)
)

### Confusion Matrix

![Confusion Matrix](![image](https://github.com/user-attachments/assets/e873a0ce-a922-4b72-9667-3f605eedec44)
)

## Future Improvements

Some ideas for improving this project include:
- Implementing a more detailed analysis report.
- Allowing multiple file uploads for batch processing.
- Improving the model's accuracy with a larger dataset.
- Deploying the application on a cloud platform.

**NeuraScan** - Enhancing brain tumor diagnosis through machine learning.
