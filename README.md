# CNN-MLOps
# CNN MLOps – Cat vs Dog Image Classification

## Project Overview

This project is an MLOps-based Deep Learning system for classifying images of cats and dogs using a Convolutional Neural Network (CNN).

The system includes:
- CNN model training with TensorFlow/Keras
- REST API using FastAPI
- Vue.js frontend interface
- Cloud-ready deployment architecture

The goal of this project is to understand the complete Machine Learning lifecycle:
- data processing
- model training
- model deployment
- API integration
- cloud deployment

---

# Technologies Used

## Machine Learning
- Python
- TensorFlow / Keras
- NumPy
- Pillow

## Backend
- FastAPI
- Uvicorn

## Frontend
- Vue.js 3
- Vite
- Axios

## Deployment
- GitHub
- Railway / Render
- Nixpacks

---

# Project Structure

```text
MLOPS/
│
├── backend/
│   ├── dataset/
│   ├── model/
│   │   └── model.h5
│   ├── training/
│   │   ├── train.py
│   │   ├── save_model.py
│   │   └── metrics.json
│   ├── app.py
│   ├── model.py
│   └── utils.py
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
├── requirements.txt
├── runtime.txt
├── Procfile
└── README.md
