import speech_recognition as sr
AUDIO_FILE=("Recording_hindi.wav")
r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)

try:
    print("audio file contains the following: " + r.recognize_google(audio).capitalize())
except sr.UnknownValueError:
    print("Google cant understand audio")
except sr.RequestError:
    print("Google couldn't get results")
