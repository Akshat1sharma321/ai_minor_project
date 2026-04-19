
# utils/predictor.py

import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("models/asl_mediapipe_mlp_model.h5")

# load labels
with open("data/labels.txt") as f:
    labels = f.read().splitlines()

def predict(landmarks):
    data = np.array(landmarks).reshape(1, -1)
    pred = model.predict(data, verbose=0)
    return labels[np.argmax(pred)]