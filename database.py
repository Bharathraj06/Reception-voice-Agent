from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

db = client["reception_agent"]

calls_collection = db["calls"]


def save_call(transcript, details):

    call_data = {
        "time": datetime.now(),
        "transcript": transcript,
        "caller_details": details
    }

    calls_collection.insert_one(call_data)


def get_calls():

    return list(
        calls_collection.find().sort(
            "time",
            -1
        )
    )