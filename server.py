from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    
    if not text_to_analyze:
        return "Error: No text provided for analysis."
    
    result = emotion_detector(text_to_analyze)
    
    if 'error' in result:
        return f"Error: {result.get('error', 'Unknown error')}. Details: {result.get('details', 'No details')}"
    
    emotions_order = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    emotion_parts = []
    
    for emotion in emotions_order:
        value = result.get(emotion, 0)
        emotion_parts.append(f"'{emotion}': {value}")
    
    # Format the emotions into the required string format
    emotions_str = ', '.join(emotion_parts[:-1]) + ' and ' + emotion_parts[-1]
    dominant_emotion = result.get('dominant_emotion', 'neutral')
    
    return f"For the given statement, the system response is {emotions_str}. The dominant emotion is {dominant_emotion}."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)