import os
from dotenv import load_dotenv
from groq import Groq

class GroqSpeechToText:
  
  def __init__(self):
    load_dotenv()
    self.client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

  def get_text(self):
    filename = os.path.dirname(__file__) + "/sample-0.mp3"
    with open(filename, "rb") as file:
        transcription = self.client.audio.transcriptions.create(
          file=(filename, file.read()),
          model="whisper-large-v3"
        )
    return transcription.text
