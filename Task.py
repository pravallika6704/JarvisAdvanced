#Function
from dataclasses import replace
import datetime
from unittest import result
from Speak import Say
import wikipedia
import pywhatkit

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)


def NonInputExecution(query):
    query = str(query)
    
    if "time" in query:
        Time()
    
    elif "date" in query:
        Date()

    elif "day" in query:
        Day()




def InputExecution(tag,query):
    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is",""),replace("tell me about","").replace("wikipedia","")
        result = wikipedia.summary(name)
        Say(result)

    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        pywhatkit.search(query)

    elif "music" in tag:
        query = str(query).replace("play")
        pywhatkit.playonyt(query)


