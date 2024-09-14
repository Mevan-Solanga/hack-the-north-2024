from SpeechToText import GroqSpeechToText
from TextToBraille import to_braille
from Microphone import SoundDeviceMicrophone

speechToText = GroqSpeechToText()
microphone = SoundDeviceMicrophone()

while (True):
    microphone.record()
    text = speechToText.get_text()
    print(text)
    print(to_braille(text))
