from gtts import gTTS

from playsound import playsound

audio = 'speech.mp3'

language = 'en'
f = open("text.txt", "r")
content = f.read()

sp = gTTS(text=content,
          lang=language, slow=False)

sp.save(audio)
playsound(audio)
f.close()
