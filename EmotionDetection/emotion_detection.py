import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(url, headers=headers, json=input_json)
        
        if response.status_code == 200:
            response_dict = response.json()

            emotions = response_dict.get('emotionPredictions', [{}])[0].get('emotion', {})

            extracted_emotions = {
                'anger': emotions.get('anger', 0),   
                'disgust': emotions.get('disgust', 0),   
                'fear': emotions.get('fear', 0),   
                'joy': emotions.get('joy', 0),   
                'sadness': emotions.get('sadness', 0),   
            }

            if all(value == 0 for value in extracted_emotions.values()):
                extracted_emotions['dominant_emotion'] = 'neutral'
            else:
                dominant_emotion = max(extracted_emotions, key=extracted_emotions.get)
                extracted_emotions['dominant_emotion'] = dominant_emotion

            return extracted_emotions
        else:
            return {"error": f"API Error {response.status_code}", "details": response.text}
    
    except requests.exceptions.RequestException as e:
        return {"error": "Request failed", "details": str(e)}
