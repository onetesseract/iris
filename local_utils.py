from playsound import playsound
from gtts import gTTS
import os
def play(noise):
    path = os.getcwd()
    tts = gTTS(text=noise, lang='en')
    tts.save(path + "/sound.mp3")
    playsound(path + "/sound.mp3")
    os.remove(path + "/sound.mp3")