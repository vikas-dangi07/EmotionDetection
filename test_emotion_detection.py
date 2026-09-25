"""Unit tests for the emotion detection application."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


def create_mock_response(emotions):
    """Create a mock Watson response."""
    response = Mock()
    response.status_code = 200
    response.text = (
        '{"emotionPredictions":[{"emotion":'
        f'{emotions}'
        '}]}' 
    )
    return response


class TestEmotionDetector(unittest.TestCase):
    """Test the emotion_detector function."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, mock_post):
        """Test that joy is detected."""
        mock_post.return_value = create_mock_response(
            '{"anger":0.01,"disgust":0.01,"fear":0.01,'
            '"joy":0.95,"sadness":0.02}'
        )

        result = emotion_detector("I am very happy")

        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, mock_post):
        """Test that anger is detected."""
        mock_post.return_value = create_mock_response(
            '{"anger":0.95,"disgust":0.01,"fear":0.01,'
            '"joy":0.01,"sadness":0.02}'
        )

        result = emotion_detector("I am angry")

        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, mock_post):
        """Test that sadness is detected."""
        mock_post.return_value = create_mock_response(
            '{"anger":0.01,"disgust":0.01,"fear":0.01,'
            '"joy":0.02,"sadness":0.95}'
        )

        result = emotion_detector("I am sad")

        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear(self, mock_post):
        """Test that fear is detected."""
        mock_post.return_value = create_mock_response(
            '{"anger":0.01,"disgust":0.01,"fear":0.95,'
            '"joy":0.01,"sadness":0.02}'
        )

        result = emotion_detector("I am afraid")

        self.assertEqual(result["dominant_emotion"], "fear")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust(self, mock_post):
        """Test that disgust is detected."""
        mock_post.return_value = create_mock_response(
            '{"anger":0.01,"disgust":0.95,"fear":0.01,'
            '"joy":0.01,"sadness":0.02}'
        )

        result = emotion_detector("This is disgusting")

        self.assertEqual(result["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_empty_input(self, mock_post):
        """Test blank input."""
        result = emotion_detector("")

        self.assertIsNone(result["dominant_emotion"])
        mock_post.assert_called_once()


if __name__ == "__main__":
    unittest.main()
