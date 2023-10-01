import speech_recognition as sr
#to use it instantly type python -m speech_recognition in the terminal


import pyttsx3

engine = pyttsx3.init()
engine.say("hello how are you")
engine.runAndWait()



