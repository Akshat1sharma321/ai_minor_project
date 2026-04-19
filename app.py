# app.py

import streamlit as st
import cv2
import mediapipe as mp
import time

from utils.mediapipe_utils import extract_landmarks
from utils.predictor import predict
from utils.sentence_builder import update_sentence
from utils.tts import speak

st.title("🧠 Sign Language to Speech AI")

run = st.checkbox("Start Camera")
FRAME_WINDOW = st.image([])

if "sentence" not in st.session_state:
    st.session_state.sentence = ""

if "cap" not in st.session_state:
    st.session_state.cap = None

if "frame_count" not in st.session_state:
    st.session_state.frame_count = 0

if run:
    if st.session_state.cap is None:
        st.session_state.cap = cv2.VideoCapture(0)
        st.session_state.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Minimize buffer for fresher frames
        st.session_state.cap.set(cv2.CAP_PROP_FPS, 30)  # Set target FPS

    placeholder = st.empty()
    
    for _ in range(10):  # Process 10 frames per rerun
        ret, frame = st.session_state.cap.read()
        if ret:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            landmarks = extract_landmarks(rgb)

            if landmarks:
                char = predict(landmarks)
                st.session_state.sentence = update_sentence(char)

                cv2.putText(frame, f"Text: {st.session_state.sentence}", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            placeholder.image(frame, channels="BGR")
            time.sleep(0.03)
        else:
            st.error("Unable to read from camera.")
            break
    
    st.session_state.frame_count += 1
    st.rerun()
else:
    if st.session_state.cap is not None:
        st.session_state.cap.release()
        st.session_state.cap = None
    FRAME_WINDOW.image([])

if st.button("🔊 Speak"):
    if st.session_state.sentence.strip():
        speak(st.session_state.sentence)
    else:
        st.warning("No text available to speak.")

if st.button("🗑️ Clear"):
    st.session_state.sentence = ""
    st.rerun()