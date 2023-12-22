import base64
from io import BytesIO
import io
from flask import Flask, render_template, request, redirect, jsonify, send_file
import sqlite3
from PIL import Image
import work
import sprint
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

@app.route('/work/<id>')
def hello(id):
    project = work.view_work(id)
    daily = work.diaria(id)
    print(id)
    project_data = {
        "name": project[1],
        "total": project[2],
        "goal": project[3],
        "diaria": daily

    }
    return render_template('project.html', proje=project_data)

@app.route('/imagem', methods=['GET'])
def exibir_imagem():
    conector = sqlite3.connect("database.db")
    dentro = conector.execute(f"select magem from imagem_teste where idimage = 2;")
    finalidades = dentro.fetchone()[0]  
    sua_string_binaria = finalidades
    
    imagem = Image.open(io.BytesIO(sua_string_binaria))
    caminho_temporario = 'temp_image.png'
    imagem.save(caminho_temporario)
    imagem_bytes = base64.b64decode(sua_string_binaria)

    return send_file(caminho_temporario, mimetype='image/png')
    return render_template("teste.html", image=imagem_bytes)

@app.route('/works', methods=['GET'])
def works():
    return render_template("works.html")

@app.route('/work_control')
def create_work():
    return render_template("central_carnes.html")

@app.route('/insert_new_work')
def criafendas():
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
    mentiras = sprint.view_new_sprint_data()
    total = work.total_works()
    totalizante = {
        "words_writen": mentiras,
        "sao_paulo": total
    }
    return render_template("insert-sprint.html", value=totalizante)




if __name__ == '__main__':
    app.run(debug=True)