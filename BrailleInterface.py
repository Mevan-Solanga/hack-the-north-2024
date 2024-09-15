import time
from Servo import GPIOServo

PINS = [27, 23, 17, 25, 24, 22]

class BrailleGenerator:
    
    def __init__(self):
        # pin number to Servo
        # @Mev fill in
        # 27, 23, 17, 25, 24, 22
        self.pins = []
        for i in PINS:
            self.pins.append(GPIOServo(i))

    def create_character(self, character):
        assert(len(character) == 6)
        for i in range(len(character)):
            self.pins[i].change_state(True if character[i] == "1" else False)
        print(character)

    def process_sentence(self, sentence):
        for character in sentence:
            self.create_character(character) 
            time.sleep(2)