import pyautogui
import pyttsx3
import speech_recognition as sr
import pipwin
import pyaudio
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui
import instaloader
import pytube
import PyPDF2
import translate



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=10 ,phrase_time_limit=10)

    try:
       print("Recognize...")
       query = r.recognize_google(audio, language='en-in')
       print(f"user said: {query}")

    except Exception as e:
       speak("Say that again please...")
       return "none"
    return query

def time():
    t_now = datetime.datetime.now().strftime('%H:%M:%S')
    print(time)
    speak("the time is")
    speak(t_now)


#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning")

    elif hour>12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    time()
    speak("I am Jarvis . Please tell me how can I help you")


#to send Email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('[Mailid]','[password]')
    server.sendmail('[Mailid]',to,content)
    server.close()

#for latest news
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=67a243f46e064eaf913e9832c4f9d687'

    main_page = get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day=["first","second","third","fourth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
            #print(f"today's {day[i]} news is: ", {head[i]})
            speak(f"today's {day[i]} news is: {head[i]}")






if __name__=="__main__":
    wish()

    while True:
    #if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "E:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("Seraching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            #print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("Mam,what should I search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("[Number]", "this is testing protocol",12,26)


        elif "play songs on youtube" in query:
            kit.playonyt("[songname]")

        elif "email to me" in query:
            try:
                speak("what should i say")
                content = takecommand().lower()
                to = "[mailid]"
                sendEmail(to,content)
                speak("Email has been sent to xyz ")

            except Exception as e:
                print(e)
                speak("sorry mam,i am not able to send this email")

        elif "no thanks you can sleep" in query:
            speak("thanks for using me,have a good day.")
            sys.exit()
    #to close any application
        elif "close notepad" in query:
            speak("Ok maam, closing notepad")
            os.system("taskkill /f /im notepad.exe")

    #to set alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==20:
                music_dir = 'E:\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

    #to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")

        elif "tell me latest news" in query:
            speak("please wait maam,feteching the latest news")
            news()

        elif "where i am" in query or "where we are" in query:
            speak("Wait maam,let me check")
            try:
                ipAdd = get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_get = get(url)
                geo_data = geo_get.json()
                # print(geo_data)
                city = geo_data['city']
                # state = geo_data['state']
                country = geo_data['country']
                speak(f"maam i am not sure, but i think we are in {city} city of {country} country")

            except  Exception as e:
                speak("sorry maam,due to network issue i am not able to find where we are.")
                pass

    #to check instagram profile
        elif "view instagram profile" in query or "profile on instagram" in query:
            speak("Maam please enter the username correctly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Maam here is the profile of the user {name}")
            speak("Maam would you like to download profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader() #pip install instadownloader
                mod.download_profile(name, profile_pic_only=True)
                speak("I am done maam ,profile picture is saved in our main folder. Now i am ready for next command")
            else:
                pass

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("Maam,please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("Please Maam hold the screen fot few seconds, i am taking screenshot")
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done maam,the screen shot is ready. now i am ready for next command")



        elif "hide all files" in query or "visible for everyone" in query:
            speak("maam please tell me do you want to hide this folder or make it visible for everyone")
            condition = takecommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d") #os module
                speak("maam, all files in this folder are now hidden")
            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("maam, all the files in this folder are now visible to everyone,i wish you are taking decision by your own")

            elif "leave it" in condition or "leave for now" in condition:
                speak("ok sir")

        speak("Maam,do you have any other work")

