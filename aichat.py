# we have 3 parts on this projec:

# accept voice input and turn to text!!!:

# accept tex and plug into GPT:

# speech in to text:

# what you want after:


# test code
#import speech_recognition as sr
#import pyttsx3

#def SpeakText(command):
    #engine = pyttsx3.init()
    #engine.say(command) 
    #engine.runAndWait()
    #didnt work find out why and fix the problem
    
#test two
import speech_recognition as sr

recognizer = sr.Recognizer()

''' recording the sound '''

with sr.Microphone() as source:
    print("Adjusting noise ")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Recording for 4 seconds")
    recorded_audio = recognizer.listen(source, timeout=4)
    print("Done recording")

''' Recorgnizing the Audio '''
try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="en-US"
        )
    print("Decoded Text : {}".format(text))

except Exception as ex:
    print(ex)