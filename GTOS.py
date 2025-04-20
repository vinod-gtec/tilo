# Use gTTS (Google Text-to-Speech)


from gtts import gTTS
tts = gTTS("வணக்கம்! soil testing செய்ய 1 ஐ அழுத்தவும்.", lang='ta')
tts.save("welcome.mp3")
