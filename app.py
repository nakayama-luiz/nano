from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import work

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/who')
def who():
    return render_template("user-insert.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/all_profies', methods=['GET'])
def profiles():
    dicios = {
        "teste": 1
    }
    print('jogos')
    return jsonify(dicios)

@app.route('/insert_user', methods=['POST'])
def insert_user():
    if request.method == 'POST':
        print("entou?")
        nome = request.form['nome']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO perfil (nome) VALUES ('{nome}')")
        conn.commit()
        conn.close()
        return render_template("sucess.html")

@app.route('/create_work', methods=['POST'])
def insert_word():
    if request.method == 'POST':
        print("entrando.")
        namen = request.form['workName']
        work.insert_work(work=namen)
        return render_template("sucess.html")

@app.route('/works', methods=['GET'])
def work():
    return render_template("works.html")


if __name__ == '__main__':
    app.run(debug=True)