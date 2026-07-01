import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)

    print(response.status_code)

    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)

        anger_score = float(formatted_response["emotionPredictions"][0]["emotion"]["anger"])
        disgust_score = float(formatted_response["emotionPredictions"][0]["emotion"]["disgust"])
        fear_score = float(formatted_response["emotionPredictions"][0]["emotion"]["fear"])
        joy_score = float(formatted_response["emotionPredictions"][0]["emotion"]["joy"])
        sadness_score = float(formatted_response["emotionPredictions"][0]["emotion"]["sadness"])

        emotions = {'anger':anger_score,'disgust':disgust_score,\
        'fear':fear_score,'joy':joy_score,\
        'sadness':sadness_score}

        dominant_emotion = max(emotions, key=emotions.get)

    # If the response status code is 500, set all emotion to None		
    elif response.status_code == 400:        
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    # For any other unexpected status codes, set all emotion to None		
    else:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    return {'anger':anger_score,'disgust':disgust_score,\
    'fear':fear_score,'joy':joy_score,\
    'sadness':sadness_score,'dominant_emotion':dominant_emotion}
    ##return formatted_response["emotionPredictions"][0]["emotion"]["anger"]