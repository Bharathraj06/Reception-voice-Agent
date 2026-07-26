from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



def extract_details(transcript):


    prompt = f"""

You are an AI receptionist.

Analyze this phone conversation:

{transcript}


Extract:

1. Caller Name
2. Phone Number
3. Reason for Calling
4. Appointment Details
5. Customer Priority
6. Summary


Give the answer in a structured format.

"""


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]

    )


    return response.choices[0].message.content