import sqlite3


def insert_work(work, goal):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"insert into work (nome,meta) values ('{work}', '{goal}')")
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
    work = cursor.fetchall()
    conn.commit()
    conn.close()
    return work[0]

def get_all_work():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"select * from work ")
    works = cursor.fetchall()
    conn.commit()
    conn.close()
    return works


def update_work_total(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"update work set word_total = (select sum(s.words) from sprint s) where codwork = {id}")
    conn.commit()
    conn.close()

def to_write(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    apossentado = cursor.execute(f"select w.meta from work w where w.codwork = {id}")
    isso = apossentado.fetchone()
    conn.commit()
    conn.close()
    return isso[0]

def diaria(id):
    return float(to_write(id)/30)

def total_works():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    isso = cursor.execute(f"SELECT count(codwork) from work;")
    menos = isso.fetchall()
    conn.commit()
    conn.close()
    return menos[0][0]