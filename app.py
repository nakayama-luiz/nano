from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import work
import sprint
import json
from flask_cors import CORS

app = Flask(__name__, static_url_path='/static')
CORS(app)


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/who')
def who():
    return render_template("user-insert.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/all_works', methods=['GET'])
def profiles():
    pre_requisite = work.get_all_work()

    return jsonify(pre_requisite)

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
        arbeit_namen = request.form['work_name']
        goal = request.form['word_goal']
        work.insert_work(work=arbeit_namen, goal=goal)
        return render_template("works.html")
    
@app.route('/add_sprint', methods=['POST'])
def add_sprint():
    if request.method == 'POST':
        print("entrando.")
        work = request.form['nao']
        word_count = request.form['word-count']
        sprint.insert_sprint(word_count=word_count, work=work)
        return f"inserido conm suceeeso {work} ganhou {word_count}"

@app.route('/works', methods=['GET'])
def works():
    return render_template("works.html")

@app.route('/work_control')
def create_work():
    return render_template("new-work.html")

@app.route('/list_project_name', methods=['GET'])
def list_project_names():
    future_names = work.get_all_work()
    lista = []

    for x in future_names:
        nario = {
            "work_id": x[0],
            "work_name": x[1]
        }
        lista.append(nario)
    return jsonify(lista)


@app.route('/insert_sprint', methods=['GET'])
def insert_sprint():
    return render_template("insert-sprint.html")




if __name__ == '__main__':
    app.run(debug=True)