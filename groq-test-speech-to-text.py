import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get('GROQ_API_KEY') 
)
filename = os.path.dirname(__file__) + "/sample-0.mp3"

with open(filename, "rb") as file:
    transcription = client.audio.transcriptions.create(
      file=(filename, file.read()),
      model="whisper-large-v3"
    )
    print(transcription.text)






















KEY='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'