import os
import eel
import threading
import pyaudio

from engine.features import *
from engine.command import *

eel.init("www")

def start():

# Define a global variable to keep track of the last recognized query
    last_query = ""

# Function to start the Eel application
def start_eel():
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', block=True)

# Function to perform voice recognition and respond to commands
def start_voice_recognition():
    global last_query
    while True:
        query = allCommands()
        if query and query != last_query:  # Check if the query is not empty and different from the last one
            last_query = query
            print("Recognized query:", query)
            speak(query)
            

            # Perform actions based on the recognized query

# Start Eel in a separate thread
eel_thread = threading.Thread(target=start_eel)
eel_thread.start()

# Start voice recognition in the main thread
start_voice_recognition()
