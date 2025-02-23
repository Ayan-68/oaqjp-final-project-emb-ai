import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self): 
        expected_output = {
            'anger': 0.014019422, 'disgust': 0.007684813, 'fear': 0.018253794, 'joy': 0.8379833, 'sadness': 0.16916132, 'dominant_emotion': 'joy'
        }
        actual_output = emotion_detector("I am glad this happened.")

        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()