# training/create_dataset.py
import cv2, mediapipe as mp, numpy as np, os

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

data = []
labels = []

dataset_path = "asl_images"

for label in os.listdir(dataset_path):
    for img_name in os.listdir(f"{dataset_path}/{label}"):
        img = cv2.imread(f"{dataset_path}/{label}/{img_name}")
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(img_rgb)

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                landmarks = []
                for lm in handLms.landmark:
                    landmarks.extend([lm.x, lm.y, lm.z])
                data.append(landmarks)
                labels.append(ord(label) - 65)

np.save("data/dataset.npy", data)
np.save("data/labels.npy", labels)