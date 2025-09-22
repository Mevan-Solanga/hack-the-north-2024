
# Hack the North 2024: Braille Audio Interface

## Overview

This project is a Python-based assistive technology solution developed for Hack the North 2024. It enables visually impaired users to convert spoken language into Braille output and vice versa, using a combination of speech recognition, audio processing, and hardware control (servo motors for Braille display). The system is designed to run on a microcontroller platform (such as Arduino) interfaced with a computer, providing real-time translation between speech and Braille.

## Features

- **Speech to Braille:** Converts spoken words into Braille patterns using speech recognition and controls a Braille display via servo motors.
- **Braille to Speech:** (Planned/Optional) Reads Braille input and converts it back to speech.
- **Audio Recording:** Captures audio input from a microphone and processes it for speech recognition.
- **Modular Design:** Code is organized into modules for easy maintenance and extension.

## File Structure

```
hack-the-north-2024/
├── BrailleInterface.py      # Main interface for Braille hardware control
├── main.py                 # Entry point for running the application
├── Microphone.py           # Handles audio recording and microphone input
├── output.wav              # Sample/output audio file
├── requirements.txt        # Python dependencies
├── sample-0.mp3            # Sample audio file
├── servo.py                # Servo motor control logic for Braille display
├── SpeechToText.py         # Speech recognition and audio-to-text conversion
├── test.py                 # Test script for components
├── TextToBraille.py        # Text to Braille conversion logic
├── README.md               # Project documentation
├── .gitignore              # Git ignore file
└── __pycache__/            # Python bytecode cache
```

## Getting Started

### Prerequisites

- Python 3.8+
- Microphone (for audio input)
- Arduino or compatible microcontroller (for Braille display)
- Servo motors (for Braille pins)

### Installation

1. **Clone the repository:**
	```sh
	git clone https://github.com/Mevan-Solanga/hack-the-north-2024.git
	cd hack-the-north-2024
	```

2. **Install dependencies:**
	```sh
	pip install -r requirements.txt
	```

3. **Connect hardware:**
	- Connect the servo motors to your Arduino/microcontroller as per your hardware setup.
	- Ensure the Arduino is connected to your computer via USB.

### Running the Application

Run the main application:

```sh
python main.py
```

Follow the on-screen prompts to record audio and see the Braille output.

## Module Descriptions

- **main.py**: Orchestrates the workflow. Handles user input, calls speech-to-text, and sends Braille commands.
- **BrailleInterface.py**: Contains the logic to interface with the Braille hardware (servo control, pin mapping).
- **Microphone.py**: Handles audio recording and saving to `output.wav`.
- **SpeechToText.py**: Converts recorded audio to text using speech recognition libraries.
- **TextToBraille.py**: Converts text to Braille patterns (dot matrix representation).
- **servo.py**: Contains low-level servo control functions for actuating Braille pins.
- **test.py**: Script for testing individual modules.

## Example Usage

1. Run `main.py`.
2. Speak into the microphone when prompted.
3. The system will process your speech, convert it to text, then to Braille, and actuate the Braille display.

## Hardware Setup

- **Braille Display:**
  - Uses servo motors to raise/lower pins for Braille characters.
  - Connect servos to Arduino digital pins as specified in your hardware configuration.
- **Microphone:**
  - Any standard USB or built-in microphone can be used.

## Dependencies

See `requirements.txt` for a full list. Key packages include:
- `speechrecognition`
- `pyaudio`
- `pyserial` (for Arduino communication)
- `numpy`

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Hack the North 2024 organizers
- Open source Python libraries

## Contact

For questions or collaboration, contact [Mevan Solanga](https://github.com/Mevan-Solanga) or [Aung K Min](https://github.com/AungKMin).
