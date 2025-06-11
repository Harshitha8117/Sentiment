from flask import Flask, request, jsonify, render_template
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier
import nltk

nltk.download('punkt')

app = Flask(__name__)

# Training data
train_reviews = [
    # Positive
    ("I absolutely loved the product", "pos"),
    ("Fantastic service and friendly staff", "pos"),
    ("Really happy with the purchase", "pos"),

    # Negative
    ("The packaging was terrible and item was broken", "neg"),
    ("I want a refund, completely disappointed", "neg"),
    ("Not worth the price", "neg"),
    ("Poor quality and late delivery", "neg"),

    # Neutral
    ("The product is okay, nothing special", "neu"),
    ("It was delivered, but I haven't used it yet", "neu"),
    ("The experience was average", "neu")
]


# Feature extraction
def extract_features(review):
    words = word_tokenize(review.lower())
    return {word: True for word in words}

# Train classifier
training_set = [(extract_features(text), label) for text, label in train_reviews]
classifier = NaiveBayesClassifier.train(training_set)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Predict route with emoji + mood description
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    review = data["review"]
    features = extract_features(review)
    sentiment = classifier.classify(features)

    mood_map = {
    "pos": {"emoji": "😄", "description": "Positive Vibes"},
    "neg": {"emoji": "😠", "description": "Negative Experience"},
    "neu": {"emoji": "😐", "description": "Neutral Mood"}
}

    mood = mood_map.get(sentiment, {"emoji": "😐", "description": "Uncertain Tone"})
    return jsonify({
        "sentiment": sentiment,
        "emoji": mood["emoji"],
        "description": mood["description"]
    })

# Run server
if __name__ == "__main__":
    app.run(debug=True)
