"""
Emotion detection module.

Uses the IBM Watson NLP emotion model when the Watson NLP package/service
is available. The public function returns a normalized dictionary.
"""

try:
    import requests
except ImportError:
    requests = None


def emotion_detector(text_to_analyse):
    """
    Detect emotions in the supplied text.

    Expected Watson NLP response:
      {
        "emotionPredictions": [{
          "emotion": {
             "anger": ...,
             "disgust": ...,
             "fear": ...,
             "joy": ...,
             "sadness": ...
          }
        }]
      }

    Returns a dictionary containing the five emotion scores and the dominant
    emotion. For an empty input or a Watson HTTP 400 response, returns all
    values as None and dominant_emotion as None.
    """
    if not isinstance(text_to_analyse, str) or not text_to_analyse.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    # IBM Watson NLP local service endpoint commonly used by the course.
    url = "http://localhost:8080/v1/analyze"
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        if requests is None:
            raise RuntimeError("The requests package is not installed.")

        response = requests.post(url, json=payload, timeout=30)

        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            }

        response.raise_for_status()
        result = response.json()

        # Support the course's emotionPredictions response shape.
        prediction = result.get("emotionPredictions", [{}])[0]
        emotions = prediction.get("emotion", {})

        # Also support a direct emotion dictionary if returned by a wrapper.
        if not emotions and isinstance(result.get("emotion"), dict):
            emotions = result["emotion"]

        scores = {
            "anger": emotions.get("anger"),
            "disgust": emotions.get("disgust"),
            "fear": emotions.get("fear"),
            "joy": emotions.get("joy"),
            "sadness": emotions.get("sadness"),
        }

        available = {k: v for k, v in scores.items() if isinstance(v, (int, float))}
        dominant = max(available, key=available.get) if available else None
        scores["dominant_emotion"] = dominant
        return scores

    except (requests.RequestException if requests else Exception):
        # Keep the application usable when the local Watson service is not
        # running. The Flask layer can display a friendly error.
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
