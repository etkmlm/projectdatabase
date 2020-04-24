# Project Database
A fully-modular database controller SQLite

Features:
- SQLite support
- Changeable database file (.db)
- Light data management
- Add/Delete/Update/List/Search commands
- Only 10 KB

Caution:
This program running Python version 3, run with "python3 pdata.py" command.

# The Basic Guide

How to create a database?

If you are running the program for the first time, it asks the database name. Of course, you can drag-drop your database file on the project folder and change the info.txt file.

How to create a table?

If the database hasn't any table, the program asks a new table name. After this, you should enter the table body. It seems like:

Name TEXT, Surname TEXT, Age INTEGER, Phone TEXT

You can this body with any SQLite program. 

How to add data?

Just write "Column:Value" format. Ex:

Name:Noah
Surname:Watson
Age:40
Phone:000

When you finished it, you should write "0".
