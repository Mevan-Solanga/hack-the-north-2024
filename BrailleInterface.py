import time

class BrailleGenerator:
    
    def __init__(self):
        # pin number to Servo
        # @Mev fill in
        self.pins = []

    def create_character(self, character):
        assert(len(character) == 6)
        # for i in range(len(character)):
        #     self.pins[i].change_state(True if character[i] == "1" else False)
        print(character)

    def process_sentence(self, sentence):
        for character in sentence:
            self.create_character(character) 
            time.sleep(0.5)