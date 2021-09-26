import sqlite3

def get_connection():
    global conn
    global cur

    conn= sqlite3.connect("bookstore.db")
    cur= conn.cursor()

def createTable():
    get_connection()
    cur.execute("create table if not exists books(id integer primary key, title text, "
                "author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def addRecord(title, author, year, isbn):
    get_connection()
    cur.execute("insert into books values(null, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def viewAll():
    get_connection()
    cur.execute("select * from books")
    data= cur.fetchall()
    for i in data:
        print(i)
    return(data)

def deleteRecord(id):
    get_connection()
    cur.execute("delete from books where id= ?", (id,))
    conn.commit()
    conn.close()

def updateRecord(id, title= "", author="", year="", isbn= ""):
    get_connection()
    cur.execute("update books set title=?, author=?, year=?, isbn=? where id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

def searchRecord(title= "", author="", year="", isbn= ""):
    get_connection()
    cur.execute("select * from books where title= ? or author= ? or year=? or isbn= ?", (title, author, year, isbn))
    data = cur.fetchall()
    for i in data:
        print(i)
    return(data)


#addRecord('Python Learning2', 'Prof.Lewis', 4567, 123456789)
#deleteRecord(2)
viewAll()
print()
searchRecord("", "", 1234)
#updateRecord(3, "Python Learning21", "Prof.Lewis", 2021, 123456789)
#viewAll()