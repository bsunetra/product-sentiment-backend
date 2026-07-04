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

if __name__ == "__main__":
    app.run(debug=True, port=5000)