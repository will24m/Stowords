import speech_recognition as sr
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Create a file chooser dialog to select the audio file
root = Tk()
root.withdraw()
audio_file = askopenfilename()

# Create a Recognizer object
r = sr.Recognizer()

# Open the audio file and transcribe its audio
with sr.AudioFile(audio_file) as source:
  audio = r.record(source)
  transcribed = r.recognize_google(audio)

# Create a file chooser dialog to select the output file
output_file = asksaveasfilename()

# Write the transcribed text to the output file
with open(output_file, 'w') as file:
  file.write(transcribed)
