import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

class SoundDeviceMicrophone: 
    def __init__(self, duration = 2, sample_rate = 44100):
        self.duration = duration
        self.sample_rate = sample_rate

    def record(self):
        print("Recording...")
        audio_data = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        print("Recording finished")
        wav.write('output.wav', self.sample_rate, audio_data)