import os
from dotenv import load_dotenv
from groq import Groq

class GroqSpeechToText:
  
  def __init__(self):
    load_dotenv()
    self.client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

  def get_text(self, filename="output.wav"):
    filepath = os.path.dirname(__file__) + "/" + filename
    with open(filepath, "rb") as file:
        transcription = self.client.audio.transcriptions.create(
          file=(filepath, file.read()),
          model="whisper-large-v3"
        )
    return transcription.text
