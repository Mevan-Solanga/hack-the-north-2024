from SpeechToText import GroqSpeechToText
from TextToBraille import to_braille

speechToText = GroqSpeechToText()

text = speechToText.get_text() 
print(text)

print(to_braille(text))
