# Python program to translate
# speech to text and text to speech
import speech_recognition as sr
import pyttsx3 
import random


r = sr.Recognizer() # Initialize the recognizer  

# Function to convert text to speech
def SpeakText(command):
    
    # Initialize the engine
    engine = pyttsx3.init("sapi5", bool)
    engine.say(command) 
    engine.runAndWait()

# Loop infinitely for user to speak
while(1):    
    
    # Exception handling to handle
    try:
        
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            
            a= random.randint(10,20)
            b= random.randint(10,20)
            intSum=a+b
        
            # wait for a second to let the recognizer; adjust the energy threshold based on; the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            stupidAns=False
            voiceInt=0
            while(stupidAns or (intSum!=voiceInt)):
                print(f'{a} + {b} = ?')   
                
                print("listening...")
                audio2 = r.listen(source2)
                # Using google to recognize audio
                print("recognizing...")
                MyText = r.recognize_google(audio2)                 
                MyText = MyText.lower()
                print("Did you say ",MyText)

                try:
                    voiceInt= int(MyText)
                    stupidAns=False
                
                except ValueError:
                    # voiceInt=0
                    stupidAns=True
                    
                if(intSum==voiceInt):
                    print("yes, correct")
                    SpeakText("yes, correct")
                    break
                else:
                    if(stupidAns):
                        print("stupid answer, try again")
                        SpeakText("stupid answer, try again")
                        
                    else:
                        print("no, wrong try again")
                        SpeakText("no, wrong try again")  
    
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("unknown error occurred")
