# Speech Recognition and Text-to-Speech Assistant

This project implements a speech recognition and text-to-speech assistant using Python. It listens for spoken words through the microphone, processes the input, and provides verbal feedback to the user. 

## Features

- Listens for user speech and recognizes it using Google Speech Recognition.
- Provides text-to-speech feedback using the `pyttsx3` library.
- Handles pauses in speech to process input effectively.
- Stops listening after 15 seconds of inactivity.

## Requirements

To run this project, you need to have Python installed on your machine. Additionally, you will need to install the following libraries:

- `SpeechRecognition`: For recognizing speech from the microphone.
- `PyAudio`: Required for capturing audio input.
- `pyttsx3`: For text-to-speech functionality.

### Installation

You can install the required libraries using pip. Open your terminal or command prompt and run the following command:

```bash
pip install SpeechRecognition PyAudio pyttsx3
