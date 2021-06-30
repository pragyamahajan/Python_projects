import pyttsx3

engine=pyttsx3.init()
engine.say("Htext here")
engine.save_to_file("text outpout here , 'tj.mp3')
engine.runAndWait()
