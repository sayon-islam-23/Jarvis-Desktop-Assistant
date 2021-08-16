import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning sir !!! ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir !!! ")
    else:
        speak("Good Evening sir !!! ")

    speak("I am your assistant ! tell me how can i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')    
        print(f"User said :{query}\n")
    
    except Exception as e:
        #print(e)
        print("say that again please......")
        speak("Say that again please")
        return "None"
    return query




if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia.....give me a moment")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak ("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube'  in query:
            speak("opening Youtube")
            #speak("what can i search for you in youtube ?")
            cm = takeCommand().lower()
            webbrowser.open("https://www.youtube.com/")
            #webbrowser.open(f"{cm}")
        
        elif 'open google'  in query:
            speak("opening google")
            speak("what can i search for you in google ?")
            cm = takeCommand().lower()
            #webbrowser.open("https://www.google.co.in/")
            results = webbrowser.open(f"{cm}")
            speak(results)
            print(results)
        elif 'open whatsapp'  in query:
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")    
        elif 'open facebook'  in query:
            speak("opening facebook")
            webbrowser.open("https://www.facebook.com/campaign/landing.php?&campaign_id=973072061&extra_1=s%7Cc%7C256741341323%7Ce%7Cfacebook%7C&placement=&creative=256741341323&keyword=facebook&partner_id=googlesem&extra_2=campaignid%3D973072061%26adgroupid%3D54006406691%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-297690534863%26loc_physical_ms%3D9061812%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=CjwKCAjwu5CDBhB9EiwA0w6sLSurgekl-usnJagBl4I4nvCjvmjjWCYvmTM3TXnvpKF9m9xmYTgkOxoCvTEQAvD_BwE")

        elif 'play music' in query:
            music_dir = "C:\\Users\CAPITAL\Desktop\music"
            songs = os.listdir(music_dir)
            print(songs)
            speak("playing songs...wait for a moment")
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H: %M: %S: %p")
            speak(f"sir, the time is {strTime}")
            print(f"sir, the time is {strTime}")

        

        elif 'thank you' in query:
            speak("thank you sir. I hope you are enjoying. bye bye...")
            quit()

        elif 'moodle' in query:
            speak("opening moodle")
            webbrowser.open("http://moodlebppimt.ddns.net/login/index.php")  
        
        elif 'wish me' in query:
            wishMe()
        elif 'i love you' in query:
            speak("awwwwwwwwww. I love you more.... ")

        elif 'tell me a joke' in query:
            speak("ok, get ready for laughing...")
            speak("Why did the Clydesdale give the pony a glass of water? Because he was a little horse............ hahahaha.")
        elif 'tell me another joke' in query:
            speak ("There are two muffins baking in the oven. One muffin says to the other, “Phew, is it getting hot in here or is it just me?” The other muffin says, AAAAHHH!! A TALKING MUFFIN!")
            speak("HA ha ha ha. i know i'm funny")
        
        elif "play video on youtube" in query:
            speak("which video sir ??")
            cn= takeCommand().lower()
            kit.playonyt(f"{cn}")
            speak(f"your video {cn} is on your way")
