"""Emotion detection using the IBM Watson NLP service."""

import json
import requests


URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyse):
    """Detect emotions in the supplied text."""
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(
        URL,
        json=payload,
        headers=HEADERS
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    data = json.loads(response.text)
    emotions = data["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(
        emotions,
        key=emotions.get
    )

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
