# ASL Sign Language to Speech Recognition AI

Real-time American Sign Language (ASL) recognition system that converts hand gestures into spoken text using computer vision and machine learning.

---

## 📋 Abstract

This project presents an intelligent system for real-time American Sign Language (ASL) to speech conversion. The system leverages MediaPipe for robust hand landmark detection and a deep neural network for accurate letter classification. The application processes live video feeds from a webcam, extracts hand gestures, recognizes individual ASL letters, builds coherent sentences with intelligent debouncing, and converts recognized text to speech through text-to-speech synthesis. The system achieves seamless human-computer interaction, enabling deaf and hard-of-hearing individuals to communicate effectively with voice-enabled systems. The entire pipeline is wrapped in an interactive Streamlit web interface for easy accessibility.

---

## ❓ Problem Statement

Communication barriers exist for deaf and hard-of-hearing individuals when interacting with voice-controlled systems and applications. Current accessibility solutions are limited and often inadequate. There is a critical need for:

1. **Real-time gesture recognition**: Accurate identification of hand gestures without manual annotation or complex setup
2. **Accessible communication**: Enabling sign language users to communicate through spoken text seamlessly
3. **User-friendly interface**: An intuitive system that requires minimal training or technical expertise
4. **Continuous recognition**: Processing live video streams without latency or frame-dropping issues
5. **Intelligent text assembly**: Converting individual letter recognition into meaningful sentences with special commands (space, delete)

Without such a system, sign language users face exclusion from voice-enabled technologies and services.

---

## 🎯 Objectives

The primary objectives of this project are:

1. **Develop a robust hand gesture recognition system** using state-of-the-art MediaPipe hand detection
2. **Build an accurate ASL letter classifier** capable of recognizing all 26 English letters in sign language
3. **Implement real-time processing** with minimal latency for continuous gesture recognition
4. **Create intelligent sentence building mechanism** with debouncing, space insertion, and delete functionality
5. **Integrate text-to-speech conversion** to provide audio feedback for recognized text
6. **Deliver a user-friendly interface** accessible to diverse user groups with minimal technical knowledge
7. **Ensure reliability** through proper error handling and state management
8. **Enable accessibility** for deaf and hard-of-hearing communities in voice-enabled systems

---

## 🔬 Methodology

### Data Collection & Preprocessing

- **Hand Landmark Extraction**: MediaPipe hand detector identifies 21 3D hand landmarks from video frames
- **Feature Representation**: Hand landmarks converted to 63-dimensional feature vectors (21 landmarks × 3 coordinates)
- **Data Normalization**: Landmarks normalized relative to hand bounding box for scale and translation invariance

### Model Architecture

- **Neural Network**: Multi-layer Perceptron (MLP) with the following structure:
  - Input Layer: 63 features (hand landmarks)
  - Hidden Layer 1: 128 neurons with ReLU activation + 30% Dropout
  - Hidden Layer 2: 64 neurons with ReLU activation
  - Output Layer: 26 neurons with Softmax activation (26 ASL letters)
- **Training Configuration**:
  - Optimizer: Adam
  - Loss Function: Categorical Cross-entropy
  - Metrics: Accuracy
  - Epochs: 20
  - Batch Size: Default (auto)

### Real-time Processing Pipeline

1. **Video Capture**: Continuous frame acquisition from webcam at 30 FPS
2. **Hand Detection**: MediaPipe processes each frame to extract hand landmarks
3. **Landmark Extraction**: Convert raw landmarks to normalized 63-D feature vector
4. **Classification**: MLP model predicts ASL letter with highest confidence
5. **Debouncing**: 1-second delay prevents duplicate character registration
6. **Sentence Building**: Characters accumulated with special commands (SPACE/DELETE) support
7. **Text-to-Speech**: Recognized text converted to audio output on user request

### Special Gesture Recognition

- **SPACE Command**: Detected when all 4 finger tips are above their PIP joints (open palm)
- **DELETE Command**: Detected when all 4 finger tips are below their PIP joints (closed fist)

---

## 🛠️ Implementation

### Technology Stack

- **Computer Vision**: OpenCV (video capture & frame processing), MediaPipe (hand detection)
- **Deep Learning**: TensorFlow/Keras (neural network training & inference)
- **Text-to-Speech**: pyttsx3 (offline speech synthesis)
- **Web Framework**: Streamlit (interactive UI)
- **Data Processing**: NumPy (numerical operations)
- **Natural Language**: NLTK (language toolkit utilities)

### Core Components

#### 1. **MediaPipe Hand Detection** (`utils/mediapipe_utils.py`)

- Detects hand landmarks in real-time
- Returns 21 3D coordinates per hand
- Handles multiple hands and occlusions

#### 2. **Neural Network Predictor** (`utils/predictor.py`)

- Loads pre-trained MLP model from `models/asl_mediapipe_mlp_model.h5`
- Predicts ASL letter from landmark features
- Returns character with highest confidence score

#### 3. **Special Gesture Detection** (`utils/hand_tracking.py`)

- Analyzes finger tip positions vs PIP joints
- Identifies SPACE (open palm) and DELETE (closed fist) gestures

#### 4. **Sentence Builder** (`utils/sentence_builder.py`)

- Maintains sentence state across frames
- Implements 1-second debouncing to prevent duplicates
- Handles SPACE (word separation) and DELETE (character removal) commands
- Detects gesture changes to accumulate letters

#### 5. **Text-to-Speech** (`utils/tts.py`)

- Converts recognized text to spoken audio
- Uses pyttsx3 for offline synthesis
- Provides audio feedback to user

#### 6. **Streamlit Web Interface** (`app.py`)

- Live webcam feed display
- Real-time text display as gestures are recognized
- "Speak" button to vocalize recognized text
- "Clear" button to reset sentence
- Start/Stop camera checkbox for control

### Key Features Implementation

| Feature              | Implementation                                             |
| -------------------- | ---------------------------------------------------------- |
| Real-time Processing | 10 frames per Streamlit rerun cycle at ~30 FPS             |
| Debouncing           | 1-second timer prevents character duplication              |
| Sentence Building    | Global state maintains sentence across gesture recognition |
| Special Gestures     | Finger tip vs PIP joint comparison                         |
| Buffer Management    | Frame buffer size set to 1 for fresh frame acquisition     |
| Error Handling       | Graceful camera error handling and user warnings           |

---

## 📊 Results

### System Performance

- **Real-time Recognition**: Processes 10 frames per cycle with minimal latency
- **Character Recognition Accuracy**: Model trained on 20 epochs achieving high accuracy on ASL letters
- **Gesture Detection**: Special gestures (SPACE/DELETE) reliably detected
- **UI Responsiveness**: Interactive Streamlit interface with smooth frame updates

### Functional Achievements

✅ Successfully captures and processes live video stream  
✅ Accurately detects hand landmarks in real-time  
✅ Correctly classifies 26 ASL letters  
✅ Intelligently builds sentences with debouncing  
✅ Handles special commands (SPACE for word separation, DELETE for character removal)  
✅ Converts recognized text to speech output  
✅ Provides interactive, user-friendly web interface  
✅ Manages state across multiple rerun cycles

### User Experience

- Clear visual feedback of recognized characters in real-time
- Ability to construct complete sentences through continuous gesture recognition
- Special commands enhance communication fluency
- One-click text-to-speech conversion
- Simple, intuitive interface requiring minimal training

---

## 🚀 Future Scope

### Enhanced Recognition Capabilities

1. **Two-Handed Signs**: Extend system to recognize signs requiring both hands
2. **Continuous Sign Recognition**: Recognize complete words/phrases as single gestures rather than letter-by-letter
3. **Sentence Context**: Implement language model for context-aware sentence completion and correction
4. **Emotion/Expression Detection**: Detect facial expressions accompanying sign language

### Model Improvements

5. **Transformer Architecture**: Replace MLP with transformer-based architecture for better temporal understanding
6. **Transfer Learning**: Leverage pre-trained computer vision models for improved accuracy
7. **Multi-hand Support**: Train model to handle multiple signers simultaneously
8. **Dynamic Thresholding**: Adaptive confidence thresholds based on user proficiency level
9. **Online Learning**: System that improves with each user interaction

### User Experience Enhancements

10. **Multiple Language Support**: Extend beyond English ASL to other sign languages (BSL, ISL, LSF, etc.)
11. **Gesture Customization**: Allow users to define custom gestures for frequent words/phrases
12. **Confidence Visualization**: Display confidence scores for recognized characters
13. **Word Prediction**: Suggest next likely words based on context
14. **Performance Metrics**: Real-time accuracy and FPS display for debugging

### Technical Enhancements

15. **Edge Deployment**: Optimize for mobile devices and embedded systems
16. **GPU Acceleration**: Hardware acceleration for faster inference on edge devices
17. **Privacy**: On-device processing without cloud connectivity
18. **Accessibility Features**: Screen reader support, keyboard navigation
19. **Multi-Camera Support**: Support multiple camera angles simultaneously
20. **Dataset Expansion**: Collect diverse datasets across different age groups, skin tones, and hand sizes

### Commercial & Social Applications

21. **Integration with Virtual Assistants**: Connect with Alexa, Google Assistant for voice command capability
22. **Call Center Integration**: Enable deaf individuals to interact with customer service systems
23. **Educational Platform**: Gamified learning system to teach ASL to hearing individuals
24. **Healthcare Applications**: Medical appointment booking through sign language
25. **Legal/Government Services**: Accessibility compliance for government portals

### Research Directions

26. **Comparative Analysis**: Benchmark against other sign language recognition systems
27. **Cross-Cultural Validation**: Test on signers from different deaf communities
28. **Accessibility Studies**: User studies with actual deaf and hard-of-hearing communities
29. **Performance Optimization**: Research on model compression and quantization
30. **Explainable AI**: Develop interpretable model decisions for trust and debugging

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Usage Guide](#usage-guide)
- [Troubleshooting](#troubleshooting)

## Features

- **Real-time Hand Gesture Recognition**: Live webcam capture with MediaPipe hand landmark detection
- **ASL Letter Classification**: ML model trained to recognize all 26 ASL letters
- **Intelligent Sentence Building**:
  - Accumulates recognized letters into complete sentences
  - SPACE command for word separation
  - DELETE command to remove last character
  - Debouncing to prevent duplicate character registration
- **Text-to-Speech Conversion**: Convert recognized text to audio output
- **Interactive Web Interface**: User-friendly Streamlit application

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Git** (optional, for version control)
- **Webcam** - Required for real-time gesture recognition

## Installation

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

## Setup Instructions

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

## Usage Guide

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

## License

This project is provided as-is for educational and accessibility purposes.

## Acknowledgments

- **MediaPipe** - Hand detection and landmark extraction
- **TensorFlow** - Deep learning framework
- **Streamlit** - Web application framework
