import time, datetime, random, keyboard
from datetime import timedelta
from atproto import Client, client_utils
import os
from dotenv import load_dotenv, dotenv_values

# this is probably over-engineered, I built it to be ran constantly so it could be self contained.
# there are probably better ways of doing this, will looking into that at another time, this works.

# resets hour to 20
def restoreTime(_datetime: datetime.datetime):
    
    newTime = datetime.datetime(_datetime.year, _datetime.month, _datetime.day, 20, 0, 0, 0, _datetime.tzinfo)

    return newTime

# time variables
temp_last_time = restoreTime(datetime.datetime.now(datetime.timezone.utc))
temp_day_after_last_time = temp_last_time + datetime.timedelta(days=1)

last_time_dict = {
    "last time": temp_last_time,
    "day after last time": temp_day_after_last_time
}

def setupLastTimes():
    temp_last_time = restoreTime(datetime.datetime.now(datetime.timezone.utc))
    temp_day_after_last_time = temp_last_time + datetime.timedelta(days=1)

    last_time_dict["last time"] = temp_last_time
    last_time_dict["day after last time"] = temp_day_after_last_time

setupLastTimes()

print(last_time_dict["last time"].strftime("%d/%m/%Y, %H:%M:%S"))
print(last_time_dict["day after last time"].strftime("%d/%m/%Y, %H:%M:%S"))

# the vocab we pull from for the god speak posts
words = open('Vocab.DD').read().split('\n')

load_dotenv()

bsky_user = os.getenv("BLUESKY_USER")
bsky_pass = os.getenv("BLUESKY_PASS")

charLimit = 300

def postGodSpeak():

    text = generateGodSpeak()

    if text is None:
        print("godspeak generation has failed")
        return
    
    print(text)
    print("logging into bsky")

    client = Client()
    profile = client.login(bsky_user, bsky_pass)
    print("Logged into " + profile.display_name)

    post = client.send_post(text)
    #setupLastTimes()


def generateGodSpeak():

    print("generating god speak")

    minWords = 28
    wordCount = 0
    text = ""

    while (wordCount < minWords):
        wordCount = wordCount + 1
        text = text + random.choice(words)
        if (wordCount < minWords):
            text = text + " "
    
    if len(text) > charLimit:
        print("exeeded char limit!")
        text = generateGodSpeak()
    return text

# this is run constantly, via the while loop at the bottom.

def update():

    current_time = datetime.datetime.now(datetime.timezone.utc)

    #debugging
    #print("current:" + current_time.strftime("%d/%m/%Y, %H:%M:%S") + "\n" + "next: " + day_after_last_time.strftime("%d/%m/%Y, %H:%M:%S"))

    current_time_is_greater = current_time >= last_time_dict["day after last time"]

    #debugging
    #print(current_time_is_greater)

    if (current_time_is_greater):
        postGodSpeak()



Timer = 0
forcePost = False
printTimer = False
printLastTime = False
forceTimeUpdate = False

while True:
    if keyboard.is_pressed('p'):
        if (forcePost == False):
            forcePost = True
            postGodSpeak()
    else:
        forcePost = False
    
    if keyboard.is_pressed('t'):
        if (printTimer == False):
            printTimer = True
            print(Timer)
    else:
        printTimer = False
    
    if keyboard.is_pressed('f'):
        if (forceTimeUpdate == False):
            forceTimeUpdate = True
            print("Forcing Last Times Update")
            setupLastTimes()
            print("Last Time Force Update has Finished")
    else:
        forceTimeUpdate = False
    
    if keyboard.is_pressed('l'):
        if (printLastTime == False):
            printLastTime = True
            print(last_time_dict["last time"].strftime("%d/%m/%Y, %H:%M:%S"))
    else:
        printLastTime = False

    if Timer > 0:
        Timer = Timer - 1
    else:
        print("running slow update")
        update()
        Timer = 100000000