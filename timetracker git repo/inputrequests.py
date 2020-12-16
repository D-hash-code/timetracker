
from datetime import datetime
import time
import sqlite3


def access_database(dbfile, query, inputs = 0):
    connect = sqlite3.connect(dbfile)
    cursor = connect.cursor()
    if inputs == 0:
        cursor.execute(query)
    else:
        cursor.execute(query,inputs)
    connect.commit()
    connect.close()

def access_database_with_result(dbfile, query, inputs = 0):
    connect = sqlite3.connect(dbfile)
    cursor = connect.cursor()
    if inputs ==0:
        rows = cursor.execute(query).fetchall()
    else:
        rows = cursor.execute(query,inputs).fetchall()
    connect.commit()
    connect.close()
    return rows

def satisfactioninput():
    try:
        satisfaction = input("Satisfaction (1-5):")
        satisfaction = int(satisfaction)
        assert 1<=satisfaction<=5
    except (ValueError,AssertionError): 
        print("Nah you made some mistake in input bro")
        satisfaction= -1
    return satisfaction

def productivityinput():
    #productivity
    try:
        productivity = input("Productivity (1-5):")
        productivity = int(productivity)
        assert 1<=productivity<=5
    except (ValueError,AssertionError): 
        print("Nah you made some mistake in input bro")
        productivity= -1
    return productivity

def focusinput():
    #focus
    try:
        focus = input("Focus (1-5):")
        focus = int(focus)
        assert 1<=focus<=5
    except (ValueError,AssertionError): 
        print("Nah you made some mistake in input bro")
        focus= -1
    return focus

def thoughtsinput():
    return input("Write some of your thoughts on the session. Did you get done what you hoped? What did you like/not like about it? What distracted you?")

def labelsinput():
    print("Labels: One word snippets") 
    print('')
    time.sleep(0.4)
    def addlabel(label):
        if label == '0':
            print("Current labels;")
            for e, l in enumerate(labels):
                print(str(e+1)+": " +l)
                print('')
                time.sleep(0.2)
            pass
        else:
            labels.append(label)
            print("Current labels;")
            for e, l in enumerate(labels):
                print(str(e+1)+": " +l)
                print('')
                time.sleep(0.2)
            label = input("Add Label (one at a time, 0 to finish adding labels):")
            
            if len(labels)==10:
                print('')
                print("max of 10 labels allowed")
                pass
            return addlabel(label)
    labels = []
    label = input("Add Label (one at a time, 0 to finish adding labels):")
    print('')
    print('')
    time.sleep(0.5)
    addlabel(label)

    return str(labels)

def sessiontimeinput():
    startdate = input("Session start (date - YYYY/MM/DD):")
    print('')
    time.sleep(0.2)
    starttime = input("Session start (time - HH:MM):")
    print('')
    time.sleep(0.2)
    startdatetime = startdate + " " + starttime

    enddate = input("Session end (date - YYYY/MM/DD):")
    print('')
    time.sleep(0.2)
    endtime = input("Session end (time - HH:MM):")
    print('')
    time.sleep(0.2)
    enddatetime = enddate + " " + endtime

    try:
        a = datetime.strptime(startdatetime,'%Y/%m/%d %H:%M')
        b = datetime.strptime(enddatetime,'%Y/%m/%d %H:%M')
        assert b>a
    except (ValueError,AssertionError):
        print("Date not inputted in the correct format or invalid dates!!!")
        print('')
        time.sleep(0.7)
        print("Aborting log. Please try again...")
        return 0,0

    starttime = str(startdatetime)
    starttime = starttime[:4]+'-'+starttime[5:7]+'-'+starttime[8:10]+' '+starttime[11:13]+':'+starttime[14:]

    endtime = str(enddatetime)
    endtime = endtime[:4]+'-'+endtime[5:7]+'-'+endtime[8:10]+' '+endtime[11:13]+':'+endtime[14:]
    return starttime,endtime

def objectiveinput():
    return input("What is the objective?:")

def bucketinput():
    Bucketoptions = access_database_with_result("mytime.db","SELECT DISTINCT Bucket FROM sessions")
    
    try:
        if len(Bucketoptions)==0:
            bucket = input("Bucket name - no vowels:").upper()
        else:
            print("Which Bucket?")
            for i,opt in enumerate(Bucketoptions):
                opt = str(opt[0])
                print(str(i+1)+": "+opt)
                print('')
                time.sleep(0.2)
            print(str(i+2)+": new/other")
            print('')
            time.sleep(0.2)
            bucket = input("Bucket Number:")
            print('')
            if int(bucket) == i+2: 
                time.sleep(0.4)
                bucket = input("Bucket name - no vowels:").upper()
            else:
                bucket = Bucketoptions[int(bucket)-1][0]
    except: 
        print("Some error so using default, pls change manually")
        bucket = "DFLT"
    
    return bucket



    