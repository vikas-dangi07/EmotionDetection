from flask import Flask, request, render_template_string
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
    <title>Emotion Detector</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 60px auto; }
        textarea { width: 100%; padding: 12px; font-size: 16px; }
        button { margin-top: 12px; padding: 10px 20px; }
        .result { margin-top: 25px; padding: 18px; background: #f2f2f2; }
        .error { color: #b00020; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Emotion Detector</h1>
    <form method="post">
        <textarea name="text" rows="6"
                  placeholder="Enter text to analyze...">{{ text }}</textarea>
        <br>
        <button type="submit">Analyze</button>
    </form>

    {% if error %}
        <p class="error">{{ error }}</p>
    {% endif %}

    {% if result %}
        <div class="result">
            <h2>Emotion Result</h2>
            <p><b>Anger:</b> {{ result.anger }}</p>
            <p><b>Disgust:</b> {{ result.disgust }}</p>
            <p><b>Fear:</b> {{ result.fear }}</p>
            <p><b>Joy:</b> {{ result.joy }}</p>
            <p><b>Sadness:</b> {{ result.sadness }}</p>
            <p><b>Dominant Emotion:</b> {{ result.dominant_emotion }}</p>
        </div>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    text = ""
    result = None
    error = None

    if request.method == "POST":
        text = request.form.get("text", "").strip()

        if not text:
            error = "Please enter text before clicking Analyze."
        else:
            result = emotion_detector(text)
            if result.get("dominant_emotion") is None:
                error = (
                    "Unable to analyze the text. "
                    "Make sure the Watson NLP service is running."
                )

    return render_template_string(
        HTML,
        text=text,
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
