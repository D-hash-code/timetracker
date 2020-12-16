import sqlite3

#Create database:
def access_database(dbfile, query):
    connect = sqlite3.connect(dbfile)
    cursor = connect.cursor()
    cursor.execute(query)
    connect.commit()
    connect.close()
def access_database_with_result(dbfile, query):
    connect = sqlite3.connect(dbfile)
    cursor = connect.cursor()
    rows = cursor.execute(query).fetchall()
    connect.commit()
    connect.close()
    return rows


def setup_tables(dbfile):
    #Get rid of existing database
    access_database(dbfile, "DROP TABLE IF EXISTS sessions") 
    #Freshly set-up tables
    access_database(dbfile, "CREATE TABLE sessions (sessionid INTEGER PRIMARY KEY AUTOINCREMENT, Bucket TEXT, Objective TEXT, starttime DATE, endtime DATE, Productivity INT, Satisfaction INT, Focus INT, Thoughts TEXT, Labels TEXT)")

setup_tables("mytime.db")

