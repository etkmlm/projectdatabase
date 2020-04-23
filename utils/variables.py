import sqlite3
import os

"""
Copyright (c) 2020 etkmlm
Project Database
"""

global conn,cursor
conn = sqlite3.connect("")
cursor = conn.cursor()
def init(database, control):
    status = False
    f = open("info.txt", "a+")
    size = os.path.getsize("info.txt");
    if (control == True):
        if (size == 0):
            status = True
    else:
        dbname = ""

        if (size == 0):
            f = open("info.txt", "w+")
            f.write("Name:" + database)
            dbname = database + ".db";
        else:
            f = open("info.txt", "r+")
            dbname = f.readline().split(':')[1] + ".db";
        f.close();
        conn = sqlite3.connect(dbname);
        cursor = conn.cursor();
    return status

def getname():
    f = open("info.txt", "r+")
    dbname = f.readline().split(':')[1];
    return dbname

def getSize(path):
    size = os.path.getsize(path)
    return size
