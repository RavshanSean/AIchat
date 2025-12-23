# we have 3 parts on this projec:

# accept voice input and turn to text!!!: FINISH!!!!!!!!!!!!!!

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
    #didnt work find out why and fix the problem later
    
    
 # STEP 1   
#test two this all line is recognize ur voice and print keep in minddd
import speech_recognition as sr
import pyttsx3
import speech_recognition as sr
import os
from dotenv import load_dotenv

from openai import OpenAI

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

#openai.api_key = os.environ.get("OPENAI_API_KEY")
#client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))



def speech_to_text():

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
        
        return text
    except Exception as ex:
        print(ex)
        
        

# STEP 2 my next step is gonna be accepting LLM inputs idk how ill figur it our
# test 11 work
def anime_character_chat(user_speech_text):

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a anime character named Kakashi from Naruto so please talk that way."},
            {
                "role": "user", 
                "content": user_speech_text}
        ]
    )

    ai_response = completion.choices[0].message.content
    return str(ai_response)


#####test 1 working but voice is does not match to what i want 
#def speak_text(text_in): 
    #engine = pyttsx3.init()
    #voices = engine.getProperty('voices') # getting detaile of curent voice 
    #engine.setProperty('voice', voices[1].id) # if changing index, changes voices. 1 for female and 0 male keep in mind 
    #engine.say(text_in) 
    #engine.runAndWait()


# test 2 voice kind a close to what i want but not perfect but better then before ill keep for now
def speak_text(text_in):

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
#test for spacific voice 
    for voice in voices:
        if "Samantha" in voice.name:
            engine.setProperty('voice', voice.id)
            break    
    
    
    engine.say(text_in)
    engine.runAndWait()



# whole process recognize speech
if __name__ == "__main__":
    print('running code')
    
    output_of_speech = speech_to_text()

    print(output_of_speech)

    res = anime_character_chat(output_of_speech)
    print(res)
    speak_text(res)

# STEP 3 text to speech TTS
# For Mac, if there any error try to run this command on terminal (pip install "pyobjc>=9.0.1") should be fine

