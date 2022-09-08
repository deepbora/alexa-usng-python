import speech_recognition as sr
import pyttsx3
# import pywhatkit
# import datetime
# import wikipedia
# import pyjokes

listener = sr.Recognizer()

engine = pyttsx3.init('dummy')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('hi ai am alexa how can i help you')

engine.runAndWait()
# try:
#     with sr.Microphone() as source:  
#         print('listinging...')
#         voice =listener.listen(source)
#         command = listener.recognize_google(voice)
#         command = command.lower()
#         if 'alexa' in command:
          
#             print(command)
        
# except:
#             pass
             