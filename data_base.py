import sqlite3


def read_data():
    sqliteConnection = sqlite3.connect('./inc/main.db')
    cursor = sqliteConnection.cursor()

    sqlite_select_query = """SELECT * from projects"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")
    for row in records:
        print("Id: ", row[0])
        print("Title: ", row[1])
        print("link: ", row[2])
    cursor.close()


def write_data(id_i, title_i, link_i):
    sqliteConnection = sqlite3.connect('./inc/main.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO projects (id, title, links) VALUES (?,?,?)"""

    data = (id_i, title_i, link_i)
    cursor.execute(sqlite_insert_query, data)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

