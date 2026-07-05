from flask import Flask, jsonify, request
from flask_cors import CORS
from db import reviews_collection

app = Flask(__name__)
CORS(app)

@app.route("/api/reviews", methods=["GET"])
def get_reviews():
    reviews = list(reviews_collection.find({}, {"_id": 0}))
    return jsonify(reviews)

@app.route("/api/sentiment", methods=["GET"])
def get_sentiment():
    positive = reviews_collection.count_documents({"sentiment": "Positive"})
    negative = reviews_collection.count_documents({"sentiment": "Negative"})
    neutral = reviews_collection.count_documents({"sentiment": "Neutral"})
    return jsonify({
        "Positive": positive,
        "Negative": negative,
        "Neutral": neutral
    })

@app.route("/api/search", methods=["GET"])
def search_reviews():
    keyword = request.args.get("q", "")
    results = list(reviews_collection.find(
        {"review_text": {"$regex": keyword, "$options": "i"}},
        {"_id": 0}
    ))
    return jsonify(results)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
