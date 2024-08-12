# Understanding audioSums.py
-----

### imports:
+ speech_recognition - to recognize speech. a recognizer r object is created. The library uses google voice recognition to idetify the voices

+ pyttsx3 - a test to speech converted library. an engine is initialised. a function SpeakText(cmd) is written to give the statemnt to be spoke.

+ random - used to randomly generating sums for the questions


### Process:
+ sr.Microphone() is called for source input

+ adjustments are made to tolerate/expect ambient noise

+ r.listen() i called to listen to voice which is recognized by r.recognize_google()

+ random sums are generated using random.randint()

+ conditional statement are written to check for correct answer

+ appropriate exception handling cases are written  
