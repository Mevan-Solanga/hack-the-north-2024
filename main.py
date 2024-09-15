import time

from SpeechToText import GroqSpeechToText
from TextToBraille import to_braille
from Microphone import SoundDeviceMicrophone
from BrailleInterface import BrailleGenerator

from threading import Thread, Lock

speechToText = GroqSpeechToText()
microphone = SoundDeviceMicrophone()
brailleGenerator = BrailleGenerator()

braille_character_queue = []
mutex = Lock()

def main_func():
    global braille_character_queue
    while (True):
        microphone.record()
        text = speechToText.get_text()
        # print(text)
        # print(to_braille(text))
        mutex.acquire()
        braille_character_queue.extend(to_braille(text))
        mutex.release()

def process_braille():
    global braille_character_queue
    while (True):
        temp_q = None
        mutex.acquire()
        temp_q = braille_character_queue.copy()
        braille_character_queue = []
        mutex.release()
        if temp_q:
            brailleGenerator.process_sentence(temp_q)

main_thread = Thread(target = main_func)
braille_thread = Thread(target = process_braille)
main_thread.start()
braille_thread.start()