import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
#engine.say("Hello Sir! This is Jarvis")
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    print(Time)  
    speak(f"The current time is {Time}") 

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(f"Today's date {date}")
    speak(f"Month{month}")
    speak(f"year{year}")
 
def wish():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good morning sir...")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir...")    
    elif hour >=18 and hour<24:
        speak("Good evening sir...")
    else:
        speak("Good night sir...")   
    speak('This is Jarvis always at your service, How can I help you?')
    #time()
    #date()
  
def wiki():
    query = "iPhone"
    results = wikipedia.summary(query, sentences=2)
    speak("According to wikipedia")
    print(results)
    speak(results)

def takecmd():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)    

    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def wiki():
    results = wikipedia.summary(query, sentences=2)
    speak("According to wikipedia")
    print(results)
    speak(results) 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com','1234')
    server.sendmail('senderemail@gmail.com', to, content)
    server.close()

def  screenshot():
    img=pyautogui.screenshot()
    img.save("C:/Users/ankit/Downloads/ss.png")   
                     
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())    

if __name__ == "__main__":
    wish()
    while True:
        query = takecmd().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query: 
            speak("searching...") 
            query = query.replace("wikipedia","")
            wiki()  
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takecmd()
                to = 'xyz@gmail.com'
                sendEmail(to, content) 
                speak(content)
                speak("Email has been sent")
            
            except Exception as e:
                print(e)
                speak("Unable to send email")

        elif 'search in internet' in query:
            speak("what should I search?")  
            chromepath = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
            search = takecmd().lower()
            wb.get(chromepath).open_new_tab(search+'.com') 

        elif 'logout' in query:
            os.system("shutdown -1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")   
        elif 'restart' in query:
            os.system("shutdown /r /t") 

        elif 'play songs' in query:
            music_dir = 'C:/Users/ankit/Downloads/Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'remember that' in query:
            speak("What should I remember?")
            data = takecmd()
            speak("You said me to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close() 

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said me to remember that"+remember.read())       

        elif 'screenshot' in query:
               screenshot()
               speak('done')

        elif 'cpu' in query:
            cpu()  

        elif 'joke' in query:
            jokes()      

        elif 'offline' in query: 
            quit()       