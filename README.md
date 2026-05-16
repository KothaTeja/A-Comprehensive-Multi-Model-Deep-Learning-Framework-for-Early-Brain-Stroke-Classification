# A Comprehensive Multi-Model Deep Learning Framework for Early Brain Stroke Classification

This project presents a deep learning-based system for automated brain stroke classification using CT scan images. The proposed framework aims to assist in early and accurate stroke detection by classifying brain CT images into multiple categories using advanced convolutional neural network architectures. The system helps reduce diagnostic time and supports healthcare professionals in clinical decision-making. :contentReference[oaicite:0]{index=0}

## 🧠 Overview

Brain stroke is a critical neurological condition caused by interrupted blood supply to the brain, potentially leading to severe brain damage, disability, or death. Accurate and timely diagnosis is essential for effective treatment and improved patient outcomes. This project focuses on:

- Automated classification of brain stroke using CT scan images
- Detecting multiple stroke categories using deep learning models
- Applying advanced preprocessing and image enhancement techniques
- Using multi-model CNN architectures for improved classification accuracy
- Building a Flask-based web application for real-time prediction

The proposed framework utilizes deep learning models including ResNet50, EfficientNetB0, and Xception for efficient feature extraction and classification. :contentReference[oaicite:1]{index=1}

## 📁 Dataset

Dataset Link: https://www.kaggle.com/datasets/ozguraslank/brain-stroke-ct-dataset

The dataset contains brain CT scan images categorized into multiple stroke-related classes.

### Classes Include:
- No Stroke
- Ischemic Stroke
- Bleeding Stroke

The dataset contains thousands of CT scan images used for training and testing the deep learning models. :contentReference[oaicite:2]{index=2}

## 🛠️ Tools & Libraries

- Python
- Flask
- TensorFlow / Keras
- PyTorch
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- ResNet50
- EfficientNetB0
- Xception

## 🔍 Image Preprocessing

The project performs several preprocessing operations to improve model performance:

- CT image resizing
- Image normalization
- Data augmentation
- Grayscale conversion
- Tensor conversion
- Dataset splitting for training and testing

Images are resized to 224×224 dimensions for model compatibility and computational efficiency. :contentReference[oaicite:3]{index=3}

## 🧪 Model Training

### Deep Learning Models Used:
- ResNet50
- EfficientNetB0
- Xception

### Training Techniques:
- Transfer Learning
- Multi-model Ensemble Learning
- Data Augmentation
- Hyperparameter Optimization

### Performance Metrics:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Sensitivity
- Specificity

The dataset was divided into training and testing sets using an 80:20 ratio. :contentReference[oaicite:4]{index=4}

## 📈 Results

The proposed framework achieved strong classification performance across all models.

### Overall Model Performance:

| Model | Accuracy |
|-------|-----------|
| ResNet50 | 96% |
| EfficientNetB0 | 92% |
| Xception | 89.32% |

ResNet50 achieved the highest overall accuracy and balanced evaluation metrics, making it the best-performing model for brain stroke classification. 
## 🌐 Web Interface (Flask App)

The Flask web application allows users to:

- Upload brain CT scan images
- Perform real-time stroke prediction
- Display classification results instantly
- Show prediction confidence scores
- Provide a simple and user-friendly interface

The system predicts whether the uploaded CT scan corresponds to:
- Normal (No Stroke)
- Ischemia
- Bleeding

The interface is designed for efficient clinical usage and easy accessibility. :contentReference[oaicite:6]{index=6}

## 🚀 Future Enhancements

- Integration with cloud deployment
- Mobile application support
- Real-time hospital integration
- Vision Transformer-based architectures
- Advanced lesion segmentation
- Multi-center dataset expansion
- 3D visualization support

Future improvements aim to enhance scalability, accessibility, and classification accuracy for real-world medical applications. :contentReference[oaicite:7]{index=7}

## 📂 Project Structure

```text
project/
│
├── app.py
├── requirements.txt
├── static/
├── templates/
└── README.md
```

## ▶️ How to Run the Project

### Clone Repository

```bash
git clone https://github.com/KothaTeja/A-Comprehensive-Multi-Model-Deep-Learning-Framework-for-Early-Brain-Stroke-Classification.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Flask Application

```bash
python app.py
```
