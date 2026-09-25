# Emotion Detection Application

## Final Project - Emotion Detector

This project implements an emotion detection web application using a
Watson NLP-compatible emotion analysis service and Flask.

### Features

- Emotion detection for anger, disgust, fear, joy and sadness
- Dominant emotion detection
- Normalized dictionary output
- HTTP 400/error handling
- Blank-input validation
- Unit tests
- Flask web deployment
- Pylint static code analysis

## Project Structure

```text
EmotionDetection/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── test_emotion_detection.py
├── server.py
├── requirements.txt
└── README.md
```

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run Unit Tests

```bash
python -m unittest -v
```

## Run Static Analysis

```bash
pylint server.py EmotionDetection/emotion_detection.py
```

## Run Flask

```bash
python server.py
```

Then open:

http://127.0.0.1:5000/

## Watson NLP Service

The application expects the Watson NLP-compatible analysis endpoint at:

`http://localhost:8080/v1/analyze`

Configure your local Watson NLP service according to the IBM Skills Network
course environment before performing the live emotion-detection demonstration.

## Assignment Evidence

Capture terminal output and screenshots for each graded activity and upload
the requested evidence to the Skills Network assignment.
