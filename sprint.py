import sqlite3


def insert_sprint(word_count, work):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"insert into sprint (cod_work, words) values ({work},{word_count})")
    conn.commit()
    conn.close()