# training/train_model.py
import numpy as np
import tensorflow as tf

X = np.load("data/dataset.npy")
y = np.load("data/labels.npy")

y = tf.keras.utils.to_categorical(y, num_classes=26)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(63,)),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(26, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X, y, epochs=20)

model.save("model/model.h5")