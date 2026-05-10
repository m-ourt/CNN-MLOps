import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import json
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.dirname(script_dir)

# =========================
# DATA PREPROCESSING
# =========================
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
    os.path.join(backend_dir, 'dataset/training_set'),
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary'
)

test_set = test_datagen.flow_from_directory(
    os.path.join(backend_dir, 'dataset/test_set'),
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary'
)

# =========================
# CNN MODEL
# =========================
cnn = tf.keras.models.Sequential()

cnn.add(tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=[64, 64, 3]))
cnn.add(tf.keras.layers.MaxPooling2D(2, 2))

cnn.add(tf.keras.layers.Conv2D(32, 3, activation='relu'))
cnn.add(tf.keras.layers.MaxPooling2D(2, 2))

cnn.add(tf.keras.layers.Flatten())
cnn.add(tf.keras.layers.Dense(128, activation='relu'))
cnn.add(tf.keras.layers.Dense(1, activation='sigmoid'))

cnn.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# =========================
# TRAINING
# =========================
history = cnn.fit(
    training_set,
    validation_data=test_set,
    epochs=25
)

# =========================
# SAVE MODEL
# =========================
cnn.save(os.path.join(backend_dir, "model/model.h5"))

# =========================
# SAVE METRICS
# =========================
metrics = history.history

with open(os.path.join(backend_dir, "training/metrics.json"), "w") as f:
    json.dump(metrics, f)

print("Training finished ✔")