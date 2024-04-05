from textblob import TextBlob

def detect_emotion(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0.2:
        return 'Positive'
    elif sentiment_score < -0.2:
        return 'Negative'
    else:
        return 'Neutral'

text = "I hate spending time with my family."
emotion = detect_emotion(text)
print("Emotion:", emotion)