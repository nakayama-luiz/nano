import datetime as dt
import sqlite3
import user

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


# user.insert_user('marcio')

# user.delete_user(1)
# cursor.execute(
#     f'''insert into sprint (nome, words) values ("paulo", 2000)''')

# cursor.execute(f"update sprint data_hora set = '{dt.datetime.now()}'")

cursor.execute("select * from perfil")

jogos = cursor.fetchall()

"""
cursor.execute('''
    CREATE TABLE sprint(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cod_work INTEGER,
        nome TEXT NOT NULL,
        words INTEGER not null,
        data_hora TIMESTAMP,
        FOREIGN KEY(cod_work) REFERENCES work(id_work)
    )
''')
"""
# print(type(jogos))

conn.commit()

conn.close()

print(user.view_user(2)[0][1])
