# utils/mediapipe_utils.py

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(model_asset_path='models/hand_landmarker.task')
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.7,
    min_hand_presence_confidence=0.7,
    min_tracking_confidence=0.7
)
hand_landmarker = vision.HandLandmarker.create_from_options(options)

def extract_landmarks(image):
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
    result = hand_landmarker.detect(mp_image)
    if result.hand_landmarks:
        landmarks = []
        for lm in result.hand_landmarks[0]:  # assuming one hand
            landmarks.extend([lm.x, lm.y, lm.z])
        return landmarks
    return None