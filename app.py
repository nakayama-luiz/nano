from flask import Flask, render_template, request, redirect
import sqlite3
import user

app = Flask(__name__)


@app.route('/')
def index():
    # return redirect('https://api.kanye.rest/')
    return render_template("selector.html")

@app.route('/all_users', methods=['GET'])
def show_all_users():
    print('entrou')
    return user.all_users()

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


if __name__ == '__main__':
    app.run(debug=True)
