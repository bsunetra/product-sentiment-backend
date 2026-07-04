from pymongo import MongoClient

MONGO_URI = "mongodb+srv://user:pass@cluster.mongodb.net/sentiment_db"

client = MongoClient(MONGO_URI)
db = client["sentiment_db"]
reviews_collection = db["reviews"]