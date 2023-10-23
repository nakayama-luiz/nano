import sqlite3


def insert_sprint(sprint, work):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"insert into sprint (nome) values ('{sprint}')")
    conn.commit()
    conn.close()