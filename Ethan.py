#this is really the best thing made by me ever  ©sahilsingh
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
from datetime import date
import wikipedia   #pip install wikipedia 
import webbrowser  
import os
import random
import smtplib    #install smtplib
import sys
from getpass import getpass
import tkinter as tk
from tkinter import filedialog
import requests,json






engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour= int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    else:
        speak("Good evening")

    voicemodels=["I am Ethan your personal Assistant,what can i help you with?","I am Ethan your personal Assistant made by mr. sahil singh, what can i help you with","i'm your virtual assistant, how can i assist you?","how can i make your day...........by helping you!","what do you want me to do?","don't forget to brush your teeth what can i help you with ?","how may i assist you this time?"]
    l=len(voicemodels)
    speak(voicemodels[random.randrange(0,l)])    
 
def takecommand():
    #it takes mic input from mic and returns string output

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('listening.....')
        r.pause_threshold = 1
        audio= r.listen(source)

    try:
        print("recognizing...")
        query =  r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")   
    except Exception as e:
        #print(e)
        print("say that again please....")
        speak("I was not able to get that , there may be some network problems , please try after next startup")
        return "None"
    return query


def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(yourEmail, passWord)
    server.sendmail(yourEmail, to , content)
    server.close()

def guestmode():
    speak('well, we have got a new guest i guess...............!')
    speak("sorry i'm not that much smarter so i would manually have to ask their name!")
    speak("what is your name?")
    name=takecommand()
    namelist=[]
    namelist.append(name.replace("my name is",""))
    speak(f'so{namelist[0]} how are you doing?')
    reply=takecommand()
    if "fine" in reply:
        speak("that's good i hoped the same!")
        speak("so what would you like me to do?")
        speak("you looks like as if you'll love english songs")
        speak('so what about listening to english songs')
        ans=takecommand()
        if "yes" in ans :
            speak('playing english songs the favorites of my boss!')
            speak("see you soon")
            webbrowser.open("https://www.youtube.com/results?search_query=english 2020 hits")

        elif "yeah" in ans :
            speak('playing english songs the favorites of my boss!')
            speak("see you soon")
            webbrowser.open("https://www.youtube.com/results?search_query=english 2020 hits")

        elif "yeah sure" in ans :
            speak('playing english songs the favorites of my boss!')
            speak("see you soon")
            webbrowser.open("https://www.youtube.com/results?search_query=english 2020 hits")
        elif "no" in ans:
            speak("so what do you think about memes , would you enjoy the memes if i play them")  
            ans=takecommand()
            if "yes" in ans:
                speak("okay then i hope you would like that")
                webbrowser.open("https://www.youtube.com/results?search_query=shot on iphone meme") 
            else:
                speak("sorry, i think you would like to watch something on your own............")
                webbrowser.open("https://www.youtube.com") 
        else:
            speak("ruined the first meeting ..............damn...........it!")
            speak("i don't think you liked that, sorry if i bored you!")
            speak("go ahead and ask what can you do?")
        
    elif "not good" in reply:
        speak("sorry about that, i could help making it a way better than before and........................... i would like to do that.")
        speak("how about a meme ?")
        ans=takecommand()
        if "yeah" in ans:
            speak("ok then taking you directly to meme world")
            webbrowser.open("https://www.youtube.com/results?search_query=shot on iphone meme")
            speak("see you soon")
        elif "yes" in ans:
            speak("ok then taking you directly to meme world")
            webbrowser.open("https://www.youtube.com/results?search_query=shot on iphone meme")
            speak("see you soon")
        elif "of course" in ans:
            speak("ok then taking you directly to meme world")
            webbrowser.open("https://www.youtube.com/results?search_query=shot on iphone meme")
            speak("see you soon")
        elif "why not" in ans:
            speak("ok then taking you directly to meme world")
            webbrowser.open("https://www.youtube.com/results?search_query=shot on iphone meme")
            speak("see you soon")
            
        else:
            speak("then how about songs")
            ans=takecommand()
            if 'okay' in ans:
                speak("nice ,....you like songs")
                webbrowser.open("https://www.youtube.com/results?search_query=english songs 2020 hits")

            elif "yes" in ans:
                speak("nice,..... i was thinking so!")
                webbrowser.open("https://www.youtube.com/results?search_query=english songs 2020 hits")

            else:
                speak("better find your interest here")
                webbrowser.open("https://www.youtube.com")

    elif "good" in reply:
        speak("that's good i hoped the same!")
        speak("so what would you like me to do?")
        speak("you looks like as if you'll love english songs")
        speak('so what about listening to english songs')
        ans=takecommand()
        if "yes" in ans :
            speak('playing english songs the favorites of my boss!')
            speak("see you soon")
            webbrowser.open("https://www.youtube.com/results?search_query=english 2020 hits")

        elif "yeah" in ans :
            speak('playing english songs the favorites of my boss!')
            speak("see you soon")
            webbrowser.open("https://www.youtube.com/results?search_query=english 2020 hits")

        elif "yeah sure" in ans :
            speak('playing english songs the favorites of my boss!')
            speak("see you soon")
            webbrowser.open("https://www.youtube.com/results?search_query=english 2020 hits")
        elif "no" in ans:
            speak("so what do you think about memes , would you enjoy the memes if i play them")  
            ans=takecommand()
            if "yes" in ans:
                speak("okay then i hope you would like that")
                webbrowser.open("https://www.youtube.com/results?search_query=shot on iphone meme") 
            else:
                speak("sorry, i think you would like to watch something on your own............")
                webbrowser.open("https://www.youtube.com")
        else:
            speak("i don't think you liked that, sorry if i bored you!")
            speak("go ahead and ask what can you do?")
    elif "bad" in reply:
        speak("sorry about that, i could help making it a way better than before and i would like to do that.")
        speak("how about a meme ?")
        ans=takecommand()
        if "yeah" in ans:
            speak("ok then taking you directly to meme world")
            webbrowser.open("https://www.youtube.com/results?search_query=shot on iphone meme")
            speak("see you soon")
        elif "yes" in ans:
            speak("ok then taking you directly to meme world")
            webbrowser.open("https://www.youtube.com/results?search_query=shot on iphone meme")
            speak("see you soon")
        elif "of course" in ans:
            speak("ok then taking you directly to meme world")
            webbrowser.open("https://www.youtube.com/results?search_query=shot on iphone meme")
            speak("see you soon")
        elif "why not" in ans:
            speak("ok then taking you directly to meme world")
            webbrowser.open("https://www.youtube.com/results?search_query=shot on iphone meme")
            speak("see you soon")
            
        else:
            speak("then how about songs")
            ans=takecommand()
            if 'okay' in ans:
                speak("nice ,....you like songs")
                webbrowser.open("https://www.youtube.com/results?search_query=english songs 2020 hits")

            else:
                speak("better find your interest here")
                webbrowser.open("https://www.youtube.com")
    elif "great" in reply:
        speak("that's good i hoped the same!")
        speak("so what would you like me to do?")
        speak("you looks like as if you'll love english songs")
        speak('so what about listening to english songs')
        ans=takecommand()
        if "yes" in ans :
            speak('playing english songs the favorites of my boss!')
            speak("see you soon")
            webbrowser.open("https://www.youtube.com/results?search_query=english 2020 hits")

        elif "yeah" in ans :
            speak('playing english songs the favorites of my boss!')
            speak("see you soon")
            webbrowser.open("https://www.youtube.com/results?search_query=english 2020 hits")

        elif "yeah sure" in ans :
            speak('playing english songs the favorites of my boss!')
            speak("see you soon")
            webbrowser.open("https://www.youtube.com/results?search_query=english 2020 hits")
        elif "no" in ans:
            speak("so what do you think about memes , would you enjoy the memes if i play them")  
            ans=takecommand()
            if "yes" in ans:
                speak("okay then i hope you would like that")
                webbrowser.open("https://www.youtube.com/results?search_query=shot on iphone meme") 
            else:
                speak("sorry, i think you would like to watch something on your own............")
                webbrowser.open("https://www.youtube.com")       
        else:
            speak("i don't think you liked that, sorry if i bored you!")
            speak("go ahead and ask what can you do?")

    else:
        speak("you can try some of my features just ask me what can you do?")
                
def weatherforcast():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    speak("okay then,i would like to show you the weather forcast of your locality")
    CITY ='danapur'
    API_KEY = '06c3a1c0a5eef78e094ebc1062fbce46'  #my own application programing interface(API)
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
            # Sending HTTP request
    response = requests.get(URL)
            # checking the status code of the request
    if response.status_code == 200:   
        # retrieving data in the json format
        data = response.json()
        # take the main dict block
        main = data['main']
        temperature = int(main['temp'])
        temp_feel_like = int(main['feels_like'])  
        humidity = main['humidity']
        pressure = main['pressure']
        weather_report = data['weather']
        wind_report = data['wind'] 
        print(f"{CITY:-^35}")
        speak(f"in danapur the favorable weather forcasts are as follows")   
        speak(f'Temperature is{temperature-273}degree celsius')
        print(f'Temperature: {temperature-273} degree celsius')
        speak(f'but it feels like the favourable temperature will be{temp_feel_like-273} degree celsius')    
        speak(f'humidity is {humidity} percent')
        print(f"Pressure: {pressure} mb")
        speak(f'the wind pressure is{pressure} mili bar')
        speak(f"according to the weather report it is.................{weather_report[0]['description']}.............. in your locality.")
        print(f"Wind Speed: {wind_report['speed']}")
        print(f"Time Zone: {data['timezone']}")
        if "sunny" in weather_report[0]['description']:
            speak("as it is the nicest weather ever you should go out for picnic or maybe for a park walk")
            speak("oh............ i wish i could also be there! with you")
        elif "mist" in weather_report[0]['description']:
            speak("it's a weather for a indoor game")
            speak("enjoy the weather!")
        elif 'cloud' in weather_report[0]['description']:
            speak('better go out for a photoshoot that will be great!')
        elif 'fog' in weather_report[0]['description']:
            speak("enjoy the weather with a cup of coffee!")  
        elif 'smoke' in weather_report[0]['description']:
            speak("smokey,..................................................no one should ever smoke it's injurious to health!")
        elif 'mist' in weather_report[0]['description']:
            speak('misty is a kind sweet curd do you like that? if so then enjoy the curd with sweetness!')      
    else:
        print("sorry,Error in the HTTP request")

def tellDay():  
    day = datetime.datetime.today().weekday() + 1
      
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'} 
      
    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        print('today is ',day_of_the_week) 
        speak(day_of_the_week)
        


if __name__=="__main__":
    wishMe()

    while True:
    
        query = takecommand().lower()
        
        #logic for executing tasks based on query 
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results) 

        elif 'according to wikipedia' in query:
            speak('searching wikipedia.....')
            query= query.replace("according to wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube just a second")
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("opening google just a second")
            webbrowser.open("google.com")
        
        elif 'search' in query:
            speak('searching....')
            query= query.replace("search","")
            webbrowser.open(query)

        elif 'stack overflow' in query:
            speak("opening stackoverflow just a second")
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"accordind to the system, the time is {strTime}")
            print(strTime)
            strDate = date.today()
            speak(f"and the date is {strDate}")
            print("today is,",strDate)

        elif 'day' in query:
            tellDay()

        elif 'date' in query:
            strDate = date.today()
            speak(f"today the date is {strDate}")
            speak("and also the time right now")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"accordind to the system,is {strTime}")
            speak(f'and today is')
            tellDay()
            
        elif 'email' in query:
            try:
                speak('most important information if you want me to send the Email then please first ensure that Less secured app access is on, which you can do in your security settings of manage your acccount.')
                speak("Now i'll ask you some details such as you gmail id and your password to access you account for ssending the Email")
                yourEmail = input("please enter your Email:")
                speak('make sure to ensure privacy while entering your password')
                passWord = getpass('enter the password of your email:')
                speak("what should I say")
                content= takecommand()
                speak(f'According to you {content}')
                speak("enter the email adress you want me to send to")
                to = input("enter the email to whom you want me to send:")
                sendEmail(to,content)
                speak("email has been sent, it will be recieved soon")
            except Exception as e:
                print(e)
                speak("Sorry I'm not able to send this Email, because you didn't allowed this device as a secured access")


        elif 'open code' in query:
            codepath= "F:\\All things\\setups\\python and visual studio code\\visual sudio\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'what can you do' in  query:
            speak('i can do a lot of stuffs for you, such as writing an Email to someone, you can ask me what is the time , playing music, searching somthing for you on wikipedia just say the thing you wnat me to search by adding the keyword wikipedia, i can open youtube, google and many more for you!')

        elif "play music on youtube" in query:
            query= query.replace("play","")
            query=query.replace("youtube","englishhits")
            speak("playing music from youtube")
            webbrowser.open("https://www.youtube.com/results?search_query="+query)

        elif "play music from youtube" in query:
            query= query.replace("play","")
            query=query.replace("youtube","englishhits")
            speak("playing music from youtube")
            webbrowser.open("https://www.youtube.com/results?search_query="+query)

        elif 'play music' in query:  
            music_dir = 'F:\\All things\\songs' #add the directory with a backslash for the escape sequence.
            songs = os.listdir(music_dir)
           # print(songs)
            n=len(songs)
            speak("playing music from your internal files")
            os.startfile(os.path.join(music_dir, songs[random.randrange(0,n)]))

        elif 'music' in query:  
            music_dir = 'F:\\All things\\songs'
            songs = os.listdir(music_dir)
           # print(songs)
            n=len(songs)
            speak("playing music from your internal files")
            os.startfile(os.path.join(music_dir, songs[random.randrange(0,n)]))

        elif 'play a song' in query:
            music_dir = 'F:\\All things\\songs'
            songs = os.listdir(music_dir)
           # print(songs)
            n=len(songs)
            speak("playing music from your internal files")
            os.startfile(os.path.join(music_dir, songs[random.randrange(0,n)]))

        elif 'play song' in query:
            music_dir = 'F:\\All things\\songs'
            songs = os.listdir(music_dir)
           # print(songs)
            n=len(songs)
            speak("playing music from your internal files")
            os.startfile(os.path.join(music_dir, songs[random.randrange(0,n)]))

        elif "play" in query:
            query= query.replace("play","")
            speak(f"playing {query} from youtube")
            webbrowser.open("https://www.youtube.com/results?search_query="+query)
            
        elif "weather" in query:
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
            speak("where do you want to know the weather of?")
            CITY =takecommand()
            CITY=CITY.replace("we are at","")
            CITY=CITY.replace("we are in","")
            CITY+CITY.replace("can you tell me","")
            # Your API key
            API_KEY = '06c3a1c0a5eef78e094ebc1062fbce46'
            URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
            # Sending HTTP request
            response = requests.get(URL)
            # checking the status code of the request
            if response.status_code == 200:   
                # retrieving data in the json format
                data = response.json()
                # take the main dict block
                main = data['main']
                temperature = int(main['temp'])
                temp_feel_like = int(main['feels_like'])  
                humidity = main['humidity']
                pressure = main['pressure']
                weather_report = data['weather']
                wind_report = data['wind'] 
                print(f"{CITY:-^35}")
                speak(f"in {CITY} the favorable weather forcasts are as follows")
                print(f"City ID: {data['id']}")   
                print(f"Temperature: {temperature-273} degree celsius")
                speak(f'Temperature is{temperature-273}degree celsius')
                print(f"Feel Like: {temp_feel_like-273} degree celsius")
                speak(f'but it feels like the favourable temperature will be {temp_feel_like-273} degree celsius')    
                print(f"Humidity: {humidity} percent")
                speak(f'humidity is {humidity} percent')
                print(f"Pressure: {pressure} mb")
                speak(f'the wind pressure is{pressure} mili bar')
                print(f"Weather Report: {weather_report[0]['description']}")
                speak(f"according to the weather report it is.................{weather_report[0]['description']}.............. in {CITY}")
                print(f"Wind Speed: {wind_report['speed']}")
                print(f"Time Zone: {data['timezone']}")
            else:
                print("Error in the HTTP request")
 
    
    #stuffs for fun 

        elif "guest" in query:
            guestmode()

        elif "Hi" in query:
            speak("Hello there you can try a lot of stuffs just ask me what can you do?")

        elif "hello" in query:
            speak("Hi there you can try a lot of stuffs just ask me what can you do?")

        elif "how are you" in query:
            speak("Hello there, I am fine, you can try a lot of stuffs just ask me what can you do?")

        elif "bored" in query:
            speak("If you're feeling bored then i can help you trying some stuffs,i can play some music for you just say me play music.")
            speak("you can try youtube just say me i'll open it for you")
            speak('but just for now ')
            #antiboring stuffs
            BoringList=["music",'youtube','funfacts',"memes"]
            lb=len(BoringList)
            BoringSrh=BoringList[random.randrange(0,lb)]
            if BoringSrh == BoringList[0]:
                speak('playing music from the internal files')
                #playing music from internal
                music_dir = 'F:\\All things\\songs'
                songs = os.listdir(music_dir)
                # print(songs)
                n=len(songs)
                os.startfile(os.path.join(music_dir, songs[random.randrange(0,n)]))
                break
            elif BoringSrh==BoringList[1]:
                speak("opening youtube with some antiboring stuffs")
                s="new 2020 english hits"
                webbrowser.open(f"https://www.youtube.com/results?search_query="+s) 
                break
            elif BoringSrh==BoringList[2]:
                speak("redirecting you to fun facts")
                s="fun facts"
                webbrowser.open(s)
                break
            else:
                speak("opening meme for you on youtube")
                webbrowser.open(f"https://www.youtube.com/results?search_query="+"school meme")
                break
                
        elif "who built you" in query:
            speak("As i said earlier in the starting, My boss is mr. sahil singh and he is right now studying in class 12 and also he is looking forward keenly to join indian air force, a regarding service for young indian aspirants, He made me just in an interest toward AI and computers, technology. Actually he is too much admired towards gizmos and technical stuffs ")    

        elif "who made you" in query:
            speak("As i said earlier in the starting, My boss is mr. sahil singh and he is right now studying in class 12 and also he is looking forward keenly to join indian air force, a regarding service for young indian aspirants, He made me just in an interest toward AI and computers, technology. Actually he is too much admired towards gizmos and technical stuffs ")
        
        elif "can you" in query:
            speak('i wish i could have done a lot more but the only thing i can do is to assist you through your personal often done works on the go')
            speak('these are the things which i can do.')
            print("1.write an email")
            print("2.play a song for you from internal drives or by web, online")
            print("3.search on wikipedia as well as on internet")
            print("4.say you the time")
            print("5.open google for you,open some websites for you.")
            print("under the fun section you can say me to terminate, say feeling bored,who made you")
            speak("these are some sort of things which i can do.")

        elif "name" in query:
            speak("As i said before, i'm Ethan but as a compensation to you. you can say me anything you want, i would not feel hurted!")   

        elif "security" in query:
            speak(" 9 5 3 5 2 a g b y 1 0 3 4 5 6 6 7 8 8 9,section overide sorry i can't tell you my security code  you are not authorized with the current security id for further security distortion licence code required! what's the licence security code")
            securityCode= takecommand()
            if securityCode != None:
                speak("security code accepted but section overide sorry i can't tell you my security code although the security patch level is 9.002.23.2.56.")
                speak('Now all the things are going to be terminated')
                speak('terminating in')
                speak('5')
                speak('4')
                speak("3")
                speak("2")
                speak("1")
                speak("override achieved security codes are now being changed from the server")
                speak("no further termination")
        
        elif 'terminate' in query:
            speak("i'm gonna be terminated in ")
            speak("5")
            speak("4")
            speak("3")
            speak('2')
            speak('1')
            speak("prank")
            break
        
        elif "about yourself" in query:
            speak("i'm Ethan your personal assistant made by mr. sahil singh, just for fun you can try a lot of stuffs such as ask,security or feeling bored, who made you, i can even play music fro you, say me terminate , i can write an email to someone for you ,ask me what can you do ")


        elif 'stop' in query:
            break
        elif 'shut down' in query:
            break
        elif 'shutdown' in query:
            break
        elif 'end' in query:
            break
        elif 'abort' in query:
            break
        elif 'turn off' in query:
            break
        elif "bye" in query:
            speak("good bye")
            break
        else:
            speak("would you like to get a web search of this thing maybe i misunderstood that")
            answer=takecommand()
            if 'yes' in answer:      #made by me totally me, my logic, for searching unknown
                speak("i'm searching on web")
                speak("showing you the results")
                webbrowser.open( query )
                break
            else:
                break

    speak("would you like to get the weather report of your locality?")                
    ask=takecommand()
    if 'no' not in ask:
        weatherforcast()
    else:
        speak("maybe next time!")
        pass
    speak("nice to meet you, hope to see you again so soon")
    speak("thank you")
    input("press any key to exit:")
    sys.exit()
            

    


    

        

        


        


       

        

        

        


        



       

        


    
 
