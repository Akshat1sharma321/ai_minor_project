#  ASL Sign Language to Speech Recognition AI

Real-time American Sign Language (ASL) recognition system that converts hand gestures into spoken text using computer vision and machine learning.

##  Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Usage Guide](#usage-guide)
- [Troubleshooting](#troubleshooting)

##  Features

- **Real-time Hand Gesture Recognition**: Live webcam capture with MediaPipe hand landmark detection
- **ASL Letter Classification**: ML model trained to recognize all 26 ASL letters
- **Intelligent Sentence Building**:
  - Accumulates recognized letters into complete sentences
  - SPACE command for word separation
  - DELETE command to remove last character
  - Debouncing to prevent duplicate character registration
- **Text-to-Speech Conversion**: Convert recognized text to audio output
- **Interactive Web Interface**: User-friendly Streamlit application

##  Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Git** (optional, for version control)
- **Webcam** - Required for real-time gesture recognition

##  Installation

### Step 1: Clone or Navigate to the Project Directory

```bash

```

### Step 2: Create a Virtual Environment (Recommended)

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**

- opencv-python - Computer vision library
- mediapipe==0.8.11 - Hand detection and landmark extraction
- numpy - Numerical computations
- tensorflow - Deep learning framework
- streamlit - Web application framework
- pyttsx3 - Text-to-speech synthesis
- nltk - Natural language toolkit

### Step 4: Download Pre-trained Models

The following models are already included in the `models/` directory:

- `asl_mediapipe_mlp_model.h5` - ASL letter classification model
- `hand_landmarker.task` - MediaPipe hand landmark detector

If models are missing, contact the project maintainer.

##  Setup Instructions

### 1. Verify Project Structure

Ensure your project directory has the following structure:

```
aiproj/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Project dependencies
├── data/
│   └── labels.txt                  # ASL letter labels (A-Z)
├── models/
│   ├── asl_mediapipe_mlp_model.h5  # Trained classification model
│   └── hand_landmarker.task        # MediaPipe hand detection model
├── training/
│   ├── create_dataset.py           # Dataset creation script
│   └── train_model.py              # Model training script
└── utils/
    ├── hand_tracking.py            # Hand tracking utilities
    ├── mediapipe_utils.py          # MediaPipe helper functions
    ├── predictor.py                # Model prediction logic
    ├── sentence_builder.py         # Sentence accumulation logic
    └── tts.py                       # Text-to-speech functionality
```

### 2. Check Labels File

Verify `data/labels.txt` contains all 26 ASL letters:

```
A
B
C
...
Z
SPACE
DELETE
```

### 3: Configure Webcam

Ensure your webcam is working and not in use by other applications before running the app.

## 🎮 Running the Application

### Start the Streamlit Application

```bash
streamlit run app.py
```

The application will automatically open in your default browser at:

```
http://localhost:8501
```

##  Usage Guide

### Step 1: Start the Camera

- Check the **"Start Camera"** checkbox to enable real-time hand detection

### Step 2: Perform ASL Gestures

- Position your hand in front of the camera
- Make clear ASL letter gestures (A-Z)
- The application will display the recognized letters in real-time

### Step 3: Build Your Sentence

- **Each recognized gesture** adds a letter to your sentence
- **SPACE gesture**: Adds a space between words
- **DELETE gesture**: Removes the last character
- The current text appears both on-screen and in the sidebar

### Step 4: Convert to Speech

- Click the **" Speak"** button to convert your sentence to audio
- The application will use text-to-speech to read the sentence aloud

### Step 5: Clear Text

- Click the **" Clear"** button to reset the sentence and start over

### Stop the Camera

- Uncheck the **"Start Camera"** checkbox to stop real-time processing

## Training Your Own Model (Optional)

If you want to retrain the model with new data:

### 1. Create Dataset

```bash
python training/create_dataset.py
```

This will generate:

- `data/dataset.npy` - Hand landmark features
- `data/labels.npy` - Corresponding letter labels

### 2. Train the Model

```bash
python training/train_model.py
```

This will:

- Load the dataset
- Train an MLP neural network
- Save the new model to `models/asl_mediapipe_mlp_model.h5`

## Troubleshooting

### Issue: "Unable to read from camera"

**Solution:**

- Ensure your webcam is connected and functioning
- Check that no other application is using the camera
- Try granting permissions to the Streamlit application

### Issue: Poor gesture recognition accuracy

**Solution:**

- Ensure good lighting conditions
- Keep your hand clearly visible in the camera frame
- Make deliberate, clear ASL gestures
- Avoid shadows on your hand

### Issue: Module not found errors

**Solution:**

```bash
# Reinstall dependencies
pip install -r requirements.txt

# Or manually install missing packages
pip install streamlit tensorflow mediapipe
```

### Issue: Text-to-speech not working

**Solution:**

- Verify pyttsx3 is installed: `pip install pyttsx3`
- Check that your system audio output is working
- Try a different text-to-speech engine

### Issue: Slow frame rate or lag

**Solution:**

- Close unnecessary applications to free up resources
- Reduce webcam resolution in camera settings
- Check your system CPU/RAM usage
- Move closer to the camera for better detection


##  License

This project is provided as-is for educational and accessibility purposes.

##  Acknowledgments

- **MediaPipe** - Hand detection and landmark extraction
- **TensorFlow** - Deep learning framework
- **Streamlit** - Web application framework
