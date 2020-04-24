from utils import classes
from utils import variables

"""
Copyright (c) 2020 etkmlm
Project Database
"""

def tableWizard():
    tablename = input("Table Name: ")
    print("OK, now you should enter table body. Example: Name TEXT,Surname TEXT,Age INTEGER")
    body = input("Table Body(for def 0): ")
    if (body == 0 or body == "0"):
        body = "Person_ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Name TEXT,Surname TEXT,Age INTEGER,Phone TEXT"
    classes.createTable(tablename, body)
    print("")
    print("Table created successfully.")

def delTableWizard():
    print("")
    print("Please enter table name for delete. (cancel 0)")
    name = input("Table Name: ")
    if (name == "0"):
        pass
    else:
        classes.delTable(name)
        print("Table deleted !")
def addWizard(tname):
    print("")
    print("Write like Column:Value")
    print("Note: Per line one column, for break press 0")
    addList = []
    while(True):
        value = input()
        if (value == "0"):
            break
        else:
            addList.append(value)
    classes.addData(tname, addList)
    print("Success")
def delWizard(tname):
    print("")
    print("Caution: TO PREVENT DATA LOSS, PLEASE ONLY ENTER ID COLUMN")
    column = input("Column: ")
    value = input("Value: ")
    sc = input("Are You Sure ? (Y/N)").islower()
    if (sc == True or sc == "y" or sc == "True"):
        classes.delData(tname, column, value)
        print("Success")
    else:
        pass

def upWizard(tname):
    print("")
    print("Caution: TO PREVENT DATA LOSS, PLEASE ONLY ENTER ID COLUMN")
    column = input("Target Column: ")
    id = input("Target Data: ")
    print("Write like Column:Value")
    print("Note: Per line one column, for break press 0")
    addList = []
    while(True):
        value = input()
        if (value == "0"):
            break
        else:
            addList.append(value)
    classes.upData(tname, column, id, addList)
    print("Success")
def seaWizard(tname):
    print("")
    column = input("Target Column: ")
    case = input("Search Case: ")
    classes.listSea(tname, column, case)
def colWizard(tname):
    print("id/name/type/notnull/dlft/primary")
    for col in classes.listColumns(tname):
        print(col)

def main(tabb):
    print("")
    print("")
    print("Choose an option")
    print("[1] Add Data")
    print("[2] Delete Data")
    print("[3] Update Data")
    print("[4] List Datas")
    print("[5] Search in Datas")
    print("[6] See Columns")
    print("[7] Exit")
    print("")
    choice = input("Choice: ")
    if choice == "1":
        addWizard(tabb)
        main(tabb)
    elif choice == "2":
        delWizard(tabb)
        main(tabb)
    elif choice == "3":
        upWizard(tabb)
        main(tabb)
    elif choice == "4":
        classes.list(tablee)
        main(tabb)
    elif choice == "5":
        seaWizard(tabb)
        main(tabb)
    elif choice == "6":
        colWizard(tabb)
        main(tabb)
    elif choice == "7":
        print("See you !")
        pass
try:
    print("Welcome to full-modular data controller!")
    if (variables.init("", True) == True):
        print("Please register database file !")
        name = input("Database Name(Without .db): ")
        variables.init(name, False)
        print("")
        print("Register complete, please restart the program !")
    else:
        variables.init("", False)
        print("")
        if (classes.controlTables() == False):
            print("No such table or data detected, let's create a new one!")
            tableWizard()
        print("")
        print("Select a table for control datas (Add 0, delete 1): ")
        mylist = classes.listTables()
        count = 0
        for table in mylist:
            print(str(table).replace('(', '').replace(')', '').replace("'", "").replace(',', ''))
        tablee = input("Choice: ")
        if (tablee == "0"):
            tableWizard()
        elif tablee == "1":
            delTableWizard();
        else:
            main(tablee)
except KeyboardInterrupt:
    print("User Aborted :O")
except:
    print("An error occured, please try again.")
