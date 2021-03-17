import sqlite3


# --- Only for Reading all database
def read_all_data():
    sqliteConnection = sqlite3.connect('./inc/main.db')
    cursor = sqliteConnection.cursor()
    sqlite_select_query = """SELECT * from projects"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    return records


# --- Set data to DataBase
def write_data(id_i, title_i, link_i):
    if check_data(id_i) == 0:
        sqliteConnection = sqlite3.connect('./inc/main.db')
        cursor = sqliteConnection.cursor()

        sqlite_insert_query = """INSERT INTO projects (id, title, links) VALUES (?,?,?)"""

        data = (id_i, title_i, link_i)
        cursor.execute(sqlite_insert_query, data)
        sqliteConnection.commit()
        print("Record {} inserted successfully into database :)))".format(id_i))
        cursor.close()
    else:
        print("Data {} is in database :(".format(id_i))


# --- Check Database for exist new data
def check_data(id_i):
    sqliteConnection = sqlite3.connect('./inc/main.db')
    cursor = sqliteConnection.cursor()
    sqlite_select_query = """SELECT * from projects WHERE id=?"""
    cursor.execute(sqlite_select_query, (id_i,))
    records = cursor.fetchall()

    return len(records)
