import sqlite3


def insert_work(work):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"insert into work (nome) values ('{work}')")
    conn.commit()
    conn.close()


def delete_work(work_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"delete from work where codwork = {work_id}")
    conn.commit()
    conn.close()

def update_work_name(id, nome):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"update work set nome = '{nome}' where codwork = {id}")
    conn.commit()
    conn.close()

def view_work(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"select * from work where codwork = '{id}' ")
    usuario = cursor.fetchall()
    conn.commit()
    conn.close()
    return usuario[0]

def get_all_work():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"select * from work ")
    usuario = cursor.fetchall()
    conn.commit()
    conn.close()
    return usuario

def update_work_total(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"update work set word_total = (select sum(s.words) from sprint s) where codwork = {id}")
    usuario = cursor.fetchall()
    conn.commit()
    conn.close()