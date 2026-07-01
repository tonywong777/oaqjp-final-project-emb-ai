from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the emotion_detector function and store the response 
    response = emotion_detector(text_to_analyze)

    # Extract the joy, anger, disgust, sadness, fear and dominant emotion from the response 
    joy = response['joy']     
    anger = response['anger']
    disgust = response['disgust'] 
    sadness = response['sadness']
    fear = response['fear'] 
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string
    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is <b>{}</b>.".format(anger,disgust,fear,joy,sadness,dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
