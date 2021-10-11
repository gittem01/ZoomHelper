from meeting import Meeting
import datetime
import sys
import json
from tkinter import *
import GUI

timeout = 30

def read():
    with open("data.json", "r") as data:
        return json.load(data)

def save(meetings):
    with open("data.json", "w") as data:
        json.dump(meetings, data, default=lambda o: o.__dict__, indent=4)
    
def config():
    try:
        meetings = read()
    except:
        pass
    
    meetings = GUI.addNewMeeting()

    save(meetings)

def run():
    try:
        meetings = read()
    except:
        meetings = []
    time = datetime.datetime.now()

    day = time.weekday()
    endTime = time.hour * 60 + time.minute

    for m in meetings:
        
        if (day != m["day"]):
            print(f"Wrong Day! ({Meeting.print(m)})\n")
            continue

        if (m["endTime"] - endTime < timeout):
            print("Expired!\n")
            continue

        Meeting.open(m)
        exit

def test():
    GUI.addNewMeeting()
    return

if (len(sys.argv) > 1 and (sys.argv[1] == "--config" or sys.argv[1] == "-c")):
    config()
elif (len(sys.argv) > 1 and sys.argv[1] == "--test"):
    test()
else:
    run()
