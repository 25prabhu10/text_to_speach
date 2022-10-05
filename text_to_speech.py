from gtts import gTTS

import os

with open("text.txt") as f:
    TEXT_DATA = f.read()

lang = 'en'

audio = gTTS(text=TEXT_DATA, lang=lang, slow=False)

audio.save("text.wav")

print("Audio file saved :)")