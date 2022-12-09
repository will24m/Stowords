Stowords
Stowords is a program for transcribing audio from .mp3 and .mp4 files into text. It uses the SpeechRecognition library to convert the audio to text, and allows the user to select the audio file and output file using file chooser dialogs.

Requirements
To use Stowords, you will need the following:

Python 3.6 or later
The SpeechRecognition library (version 3.8.1 or later)
The google-auth and google-api-python-client libraries (if using the Google Cloud API)
Installation
To install the required libraries, run the following command:

Copy code
pip install SpeechRecognition google-auth google-api-python-client
Usage
To use Stowords, run the transcribe.py script and follow the instructions on the screen. The program will prompt you to select the audio file and output file using file chooser dialogs.

To use the Google Cloud API for transcription, you will need to provide your API key. This can be done by creating a config.py file with the following contents:

Copy code
# config.py

# Replace this with your Google Cloud API key
API_KEY = 'YOUR_API_KEY'
Replace YOUR_API_KEY with your actual API key, and make sure the config.py file is in the same directory as the transcribe.py script. The program will automatically use the API key from the config.py file when transcribing audio.

License
Stowords is licensed under the MIT License. See the LICENSE file for more information.
