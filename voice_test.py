# Required Modules:
# Install the following packages using pip:
# pip install SpeechRecognition
# pip install PyAudio
# pip install pyttsx3



import speech_recognition as sr
import pyttsx3
import time

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# List available microphone devices and choose the correct one
print("Available microphones:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone with index {index}: {name}")

# Replace with the index of your working microphone (from the list above)
YOUR_MICROPHONE_INDEX = int(input("Enter the microphone index to use: "))

# Function to listen and process speech
def listen_and_process():
    with sr.Microphone(device_index=YOUR_MICROPHONE_INDEX) as source:
        print("Listening....")
        engine.say("Please talk, I'm listening.")
        engine.runAndWait()

        r.adjust_for_ambient_noise(source)
        
        # Start time tracking
        last_speech_time = time.time()
        full_text = ""

        while True:
            try:
                # Listen for speech
                audio_text = r.listen(source, timeout=1, phrase_time_limit=None)
                recognized_text = r.recognize_google(audio_text)
                print("You said: " + recognized_text)
                full_text += recognized_text + " "
                
                # Reset the timer
                last_speech_time = time.time()
                
            except sr.WaitTimeoutError:
                # If there's a pause of 3 seconds, break to process
                if time.time() - last_speech_time > 3:
                    print("Processing your speech...")
                    engine.say("Processing your speech.")
                    engine.runAndWait()
                    print("You said: " + full_text.strip())
                    engine.say("You said: " + full_text.strip())
                    engine.runAndWait()
                    full_text = ""  # Reset for the next round
                    break  # Break to start over listening

            except sr.UnknownValueError:
                print("Sorry, I did not get that")
                engine.say("Sorry, I did not get that")
                engine.runAndWait()
                
            except Exception as e:
                print(f"An error occurred: {e}")
                engine.say(f"An error occurred: {e}")
                engine.runAndWait()
        
        # Check if 15 seconds have passed without any speech
        if time.time() - last_speech_time > 15:
            print("No speech detected for 15 seconds, stopping.")
            engine.say("No speech detected for 15 seconds, stopping.")
            engine.runAndWait()
            return False  # Indicate to stop listening

    return True  # Continue listening

# Main loop to keep the program running
while True:
    if not listen_and_process():
        break  # Exit if the user stops talking for 15 seconds
