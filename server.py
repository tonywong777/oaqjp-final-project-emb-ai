"""
This module provides a Flask web application for detecting emotions in text.

It includes routes to render the main interface and process text analysis requests.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the requested text and return scores for different emotions.

    Returns:
        str: A formatted string containing emotion scores or an error message.
    """
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

    # Check if the dominant_emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return " Invalid text! Please try again!"

    # Return a formatted string
    return f"For the given statement, the system response is \
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. \
    The dominant emotion is <b>{dominant_emotion}</b>."

@app.route("/")
def render_index_page():
    """
    Render the main index page of the application.

    Returns:
        str: The rendered HTML content of index.html.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
