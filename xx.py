import pyttsx3                                                                  
                                                         
engine = pyttsx3.init('espeak')                                                         
engine.setProperty('rate', 120)                                                 
                                         
engine.say(" Hello, how are you doing?")                                        
engine.runAndWait()                                                             
engine.stop()  