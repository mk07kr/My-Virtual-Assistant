

import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# Audio voice checked



def speak(audio): 
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning! Mayank ")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon! Mayank ")
        
    else:
        speak("Good Evening! Mayank ")
    
    speak("I am your Virtual Assistant . Hope you are good , tell me what i can help with")
    
def takeCommand(): 
    
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold =1 #----> this is the pause time of the user speaking value
        audio =r.listen(source) #--> comming from speechRecognition module
    
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        
        print(f"User said:{query}\n")
    
    except Exception as e:
        # print(e)
        
        print("Sorry ! , Can't recognize at this moment . Can you Speak Again please!......")
        return "None"
    
    return query


    
       
if __name__ == "__main__": 
   
    wishMe()
    while(True):
   
        query=takeCommand().lower()
    
   
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia", "") 
            results =wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results) 
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open github' in query:
            webbrowser.open("github.com")
             
        elif 'open google' in query :
            webbrowser.open("google.com")
        
        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
        
        elif 'open amazon' in query :
            webbrowser.open("amazon.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\mk\\Music'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query :
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
                
                
        elif 'close' or 'exit' or 'quit' or 'stop' in query:
            exit(0)
            
        
        
             
        
        
            
            
