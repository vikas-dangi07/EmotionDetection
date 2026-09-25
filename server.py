"""Flask web application for the Emotion Detector."""

from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the emotion of the submitted text."""
    text_to_analyse = request.args.get("textToAnalyze", "")

    if not text_to_analyse or not text_to_analyse.strip():
        return "Invalid input! Please try again!"

    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return "Invalid input! Please try again!"

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy}, "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the main Emotion Detector page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
