import sys
import sqlite3
from datetime import datetime
import inputrequests
import time

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

def startsession():
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    print('')
    bucket = inputrequests.bucketinput()
    time.sleep(1)
    print('')
    print('')

    objective = inputrequests.objectiveinput()
    print('')
    print('')
    time.sleep(1)
    

    access_database("mytime.db","INSERT INTO sessions (Bucket, Objective, starttime) VALUES (?,?,?)",(bucket,objective,now))
    
    print("Mission Successful")
    print('')
    time.sleep(0.5)
    print("Goodnight")

def endsession():
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    sid = access_database_with_result("mytime.db","SELECT sessionid FROM sessions WHERE endtime IS NULL ORDER BY sessionid DESC")
    
    if len(sid) == 0:
        print("No open sessions! What have you been doing this past x amount of time?!")
        return flowcontrol()
    
    sid = sid[0][0]

    print('')
    satisfaction = inputrequests.satisfactioninput()
    print('')
    print('')
    time.sleep(1)
    productivity = inputrequests.productivityinput()
    print('')
    print('')
    time.sleep(1)
    focus = inputrequests.focusinput()
    print('')
    print('')
    time.sleep(1)

    thoughts = inputrequests.thoughtsinput()
    print('')
    print('')
    time.sleep(1)

    labels = inputrequests.labelsinput()
    print('')
    print('')

    access_database("mytime.db","UPDATE sessions SET endtime=?, Productivity=?, Satisfaction=?, Focus=?, Thoughts=?, Labels=? WHERE sessionid=?",(now,productivity,satisfaction,focus,thoughts,labels,sid))

    time.sleep(1)
    print("Mission Successful")
    print('')
    time.sleep(0.5)
    print("Goodnight")

def logsession():

    print('')
    starttime,endtime = inputrequests.sessiontimeinput()
    if starttime == 0 and endtime == 0: return flowcontrol()
    print('')
    print('')
    time.sleep(1)

    bucket = inputrequests.bucketinput()
    print('')
    print('')
    time.sleep(1)

    objective = inputrequests.objectiveinput()
    print('')
    print('')
    time.sleep(1)

    satisfaction = inputrequests.satisfactioninput()
    print('')
    print('')
    time.sleep(0.5)

    productivity = inputrequests.productivityinput()
    print('')
    print('')
    time.sleep(0.5)

    focus = inputrequests.focusinput()
    print('')
    print('')
    time.sleep(0.5)

    thoughts = inputrequests.thoughtsinput()
    print('')
    print('')
    time.sleep(1)

    labels = inputrequests.labelsinput()
    print('')
    print('')
    time.sleep(0.5)

    access_database("mytime.db","INSERT INTO sessions (Bucket, Objective, starttime, endtime, Productivity, Satisfaction, Focus, Thoughts, Labels) VALUES (?,?,?,?,?,?,?,?,?) ",(bucket, objective, starttime, endtime, productivity, satisfaction, focus, thoughts, labels))

    time.sleep(1)
    print("Mission Successful")
    print('')
    time.sleep(0.5)
    print("Goodnight")

def flowcontrol():
    time.sleep(0.4)
    print('')
    print('')
    print("Hi Sir!")
    time.sleep(0.5)
    
    print('')
    print("What would you like to do today?")
    time.sleep(1.3)
    print('')
    print('')
    
    options = ['Start a session','End a session','Log a session','You entered by accident?']
    for e,opt in enumerate(options):
        print(str(e+1)+". "+opt)
        time.sleep(1)
    selection = input('Choose 1-4:')
    time.sleep(1)
    if selection == '1':
        return startsession()
    elif selection == '2':
        return endsession()
    elif selection == '3':
        return logsession()
    elif selection == '4':
        print('')
        print("Ok gooooodbye :)")
        print('')
        time.sleep(1)
        sys.exit()
    else:
        print('')
        print("You had one task. That was invalid input. Gooooodbye you incompetent baby")
        sys.exit()

flowcontrol()

