from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, UnidentifiedImageError
import io
import time
import numpy as np

from model import model
from utils import preprocess

# ==================================================
# FastAPI Application
# ==================================================
app = FastAPI(
    title="MLOps CNN Prediction API",
    description="Professional FastAPI API for Cat vs Dog Image Classification",
    version="1.0.0"
)

# ==================================================
# CORS Configuration
# ==================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For production: replace with frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================================================
# Root Endpoint
# ==================================================
@app.get("/")
def home():
    return {
        "message": "API Running",
        "project": "CNN Cat vs Dog Classifier",
        "status": "success"
    }

# ==================================================
# Health Check Endpoint
# ==================================================
@app.get("/health")
def health():
    return {
        "api_status": "running",
        "model_loaded": True,
        "version": "1.0.0"
    }

# ==================================================
# Metrics Endpoint
# ==================================================
@app.get("/metrics")
def metrics():
    return {
        "train_accuracy": 0.8544,
        "validation_accuracy": 0.7960,
        "train_loss": 0.3241,
        "validation_loss": 0.5310,
        "epochs": 25
    }

# ==================================================
# Prediction Endpoint
# ==================================================
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    start_time = time.time()

    try:
        # Validate file type
        if not file.content_type.startswith("image/"):
            raise HTTPException(
                status_code=400,
                detail="Uploaded file must be an image."
            )

        # Read uploaded file
        contents = await file.read()

        if not contents:
            raise HTTPException(
                status_code=400,
                detail="Empty file uploaded."
            )

        # Open image
        try:
            image = Image.open(io.BytesIO(contents)).convert("RGB")
        except UnidentifiedImageError:
            raise HTTPException(
                status_code=400,
                detail="Invalid image file."
            )

        # Save image info
        width, height = image.size

        # Preprocess
        img = preprocess(image)

        # Predict
        raw_prediction = float(model.predict(img, verbose=0)[0][0])

        # Binary sigmoid interpretation
        if raw_prediction > 0.5:
            predicted_class = "dog"
            confidence = raw_prediction
        else:
            predicted_class = "cat"
            confidence = 1 - raw_prediction

        end_time = time.time()
        prediction_time = round(end_time - start_time, 4)

        return {
            "filename": file.filename,
            "image_size": {
                "width": width,
                "height": height
            },
            "prediction": {
                "class": predicted_class,
                "confidence": round(confidence, 4),
                "confidence_percent": round(confidence * 100, 2)
            },
            "raw_model_output": round(raw_prediction, 6),
            "processing_time_seconds": prediction_time,
            "status": "success"
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )