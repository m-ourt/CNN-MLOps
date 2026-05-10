from tensorflow.keras.models import load_model

model = load_model("model/model.h5")

model.save("model/model.h5")

print("Model saved ✔")