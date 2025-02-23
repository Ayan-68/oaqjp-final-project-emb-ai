import unittest  
from EmotionDetection import emotion_detector  
from math import isclose  

class TestEmotionDetector(unittest.TestCase):  
      
    def assertDictAlmostEqual(self, d1, d2, rel_tol=5e-2):  
        self.assertEqual(set(d1.keys()), set(d2.keys()), "Keys mismatch between expected and actual output.")
        
        for key in d1:  
            if key == 'dominant_emotion':  
                self.assertEqual(d1[key], d2[key], f"Mismatch in dominant emotion: {d1[key]} != {d2[key]}")  
            else:    
                self.assertTrue(  
                    isclose(d1[key], d2[key], rel_tol=rel_tol),  
                    msg=f"Mismatch in {key}: {d1[key]} != {d2[key]}"  
                )  

    def test_joy(self):   
        expected_output = {  
            'anger': 0.014019, 'disgust': 0.007685, 'fear': 0.018254,   
            'joy': 0.837983, 'sadness': 0.169161, 'dominant_emotion': 'joy'  
        }  
        actual_output = emotion_detector("I am glad this happened.")  
        self.assertDictAlmostEqual(actual_output, expected_output)  
    
    def test_anger(self):  
        expected_output = {
            'anger': 0.667473, 'disgust': 0.020267, 'fear': 0.097490,   
            'joy': 0.011864, 'sadness': 0.195306, 'dominant_emotion': 'anger'    
        }  
        actual_output = emotion_detector("I am really mad about this.")  
        self.assertDictAlmostEqual(actual_output, expected_output)


    def test_disgust(self):  
        expected_output = {  
            'anger': 0.115978, 'disgust': 0.920103, 'fear': 0.055259,   
            'joy': 0.002479, 'sadness': 0.068364, 'dominant_emotion': 'disgust'  
        }  
        actual_output = emotion_detector("I feel disgusted just hearing about this.")  
        self.assertDictAlmostEqual(actual_output, expected_output)  

    def test_sadness(self):  
        expected_output = {  
            'anger': 0.006353, 'disgust': 0.005103, 'fear': 0.070198,   
            'joy': 0.004687, 'sadness': 0.981956, 'dominant_emotion': 'sadness'  
        }  
        actual_output = emotion_detector("I am so sad about this.")  
        self.assertDictAlmostEqual(actual_output, expected_output)  

    def test_fear(self):  
        expected_output = {  
            'anger': 0.006871, 'disgust': 0.003523, 'fear': 0.990468,   
            'joy': 0.005993, 'sadness': 0.073742, 'dominant_emotion': 'fear'  
        }  
        actual_output = emotion_detector("I am really afraid that this will happen.")  
        self.assertDictAlmostEqual(actual_output, expected_output)  

if __name__ == '__main__':  
    unittest.main(verbosity=2, exit=False)  
