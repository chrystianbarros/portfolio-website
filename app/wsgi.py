from flask import Flask, redirect, render_template
import socket

app = Flask(__name__)

@app.route("/")
def webapp():
    return redirect("/home", code=302)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/apresentacao")
def apresentacao():
    return render_template('apresentacao.html')

@app.route("/certificacoes")
def certificacoes():
    return render_template('certificacoes.html')

@app.route("/habilidades")
def habilidades():
    return render_template('habilidades.html')

@app.route("/projeto")
def projeto():
    return render_template('projeto.html')

@app.route("/container")
def container_id():
    return f"Container ID: {socket.gethostname()}"

if __name__ == "__main__":
    app.run(debug=True)