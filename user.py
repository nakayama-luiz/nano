import sqlite3


def insert_user(name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"insert into perfil (nome) values ('{name}')")
    conn.commit()
    conn.close()


def delete_user(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"delete from perfil where id = {id}")
    conn.commit()
    conn.close()


def view_user(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"select * from perfil where id = {id}")
    usuario = cursor.fetchall()
    conn.commit()
    conn.close()
    return usuario



def update_user_name(id, nome):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute(f"update perfil set nome = '{nome}' where id = {id}")
  conn.commit()
  conn.close()
  print(f'teve seu usuário atualizado para: {nome}')


def get_id_by_name(name):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute(f"select * from perfil where nome = '{name}' ")
  usuario = cursor.fetchall()
  conn.commit()
  conn.close()
  return usuario[0][0]