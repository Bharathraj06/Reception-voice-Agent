from datetime import datetime


def call_model(transcript, details):

    return {
        "time": datetime.now(),
        "transcript": transcript,
        "caller_details": details
    }