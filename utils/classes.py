import sqlite3
from utils import variables

"""
Copyright (c) 2020 etkmlm
Project Database
"""

def list(table):
    string = ""
    for i in lcOp(table):
        if (string == ""):
            string = i
        else:
            string += "/"+i
    print(string)
    variables.conn = sqlite3.connect(variables.getname() + ".db")
    variables.cursor = variables.conn.cursor();
    variables.cursor.execute("Select *from " + table);
    rows = variables.cursor.fetchall();
    for row in rows:
        print(row)
    variables.cursor.close()
def listSea(table, column, case):
    string = ""
    for i in lcOp(table):
        if (string == ""):
            string = i
        else:
            string += "/"+i
    print(string)
    variables.conn = sqlite3.connect(variables.getname() + ".db")
    variables.cursor = variables.conn.cursor();
    variables.cursor.execute("Select *from " + table + " where " + column + " like '%"+case+"%'");
    rows = variables.cursor.fetchall();
    for row in rows:
        print(row)
    variables.cursor.close()
def createTable(name,body):
    variables.conn = sqlite3.connect(variables.getname() + ".db")
    variables.cursor = variables.conn.cursor();
    variables.cursor.execute("CREATE TABLE IF NOT EXISTS "+name+" ("+body+")");
    variables.conn.commit();
    variables.cursor.close()
def addData(table,columns):
    variables.conn = sqlite3.connect(variables.getname() + ".db")
    variables.cursor = variables.conn.cursor();
    colString = ""
    afterMaxString = ""
    afterString = ""
    for i in range(0, len(columns)):
        data = columns[i]
        column = data.split(':')[0]
        value = data.split(':')[1]
        if colString != "":
            colString += ","+column
        else:
            colString = column
        if afterString != "":
            afterString += ",'"+value+"'"
        else:
            afterString = "'"+value+"'"
        if afterMaxString != "":
            afterMaxString += " AND "+column+"='"+value+"'"
        else:
            afterMaxString = column+"='"+value+"'"
    variables.cursor.execute("Select *from " + table + " where " + afterMaxString);
    rows = variables.cursor.fetchall();
    kontrol = False
    for row in rows:
        kontrol = True
    if kontrol != True:
        variables.cursor.execute("REPLACE INTO "+table+" ("+colString+") VALUES ("+afterString+")");
        variables.conn.commit()
    variables.cursor.close()

def listTables():
    variables.conn = sqlite3.connect(variables.getname() + ".db")
    variables.cursor = variables.conn.cursor()
    variables.cursor.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'")
    rows = variables.cursor.fetchall()
    list = []
    for row in rows:
        list.append(row)
    return list

def delTable(table):
    variables.conn = sqlite3.connect(variables.getname() + ".db")
    variables.cursor = variables.conn.cursor()
    variables.cursor.execute("DROP TABLE " + table);
    variables.conn.commit()
    variables.cursor.close()

def controlTables():
    control = False
    variables.conn = sqlite3.connect(variables.getname() + ".db")
    variables.cursor = variables.conn.cursor()
    variables.cursor.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'")
    rows = variables.cursor.fetchall()
    for row in rows:
        control = True
    variables.cursor.close()
    return control
def listColumns(table):
    list = []
    variables.conn = sqlite3.connect(variables.getname() + ".db")
    variables.cursor = variables.conn.cursor()
    variables.cursor.execute("PRAGMA table_info("+table+")")
    rows = variables.cursor.fetchall()
    for row in rows:
        list.append(row)
    variables.cursor.close()
    return list

def lcOp(table):
    list = []
    variables.conn = sqlite3.connect(variables.getname() + ".db")
    variables.cursor = variables.conn.cursor()
    variables.cursor.execute("PRAGMA table_info("+table+")")
    rows = variables.cursor.fetchall()
    for row in rows:
        list.append(str(row).split(',')[1].replace("'", ""))
    variables.cursor.close()
    return list

def delData(table, column, value):
    variables.conn = sqlite3.connect(variables.getname() + ".db")
    variables.cursor = variables.conn.cursor();
    variables.cursor.execute("Delete from " + table + " where " + column +"=" + value);
    variables.conn.commit()
    variables.cursor.close()

def upData(table,col,target,columns):
    variables.conn = sqlite3.connect(variables.getname() + ".db")
    variables.cursor = variables.conn.cursor();
    afterMaxString = ""
    for i in range(0, len(columns)):
        data = columns[i]
        column = data.split(':')[0]
        value = data.split(':')[1]
        if afterMaxString != "":
            afterMaxString += " AND "+column+"='"+value+"'"
        else:
            afterMaxString = column+"='"+value+"'"
    variables.cursor.execute("UPDATE " + table + " set " + afterMaxString + " where "+ col + "='"+target+"'");
    variables.conn.commit()
    variables.cursor.close()
