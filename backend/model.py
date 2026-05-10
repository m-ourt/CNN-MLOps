from tensorflow.keras.models import load_model
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "model/model.h5")

model = load_model(model_path)

classes = ["cat", "dog"]