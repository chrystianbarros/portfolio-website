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
def apresentacao_page():
    return render_template('apresentacao.html')

@app.route("/container")
def container_id():
    return f"Container ID: {socket.gethostname()}"

if __name__ == "__main__":
    app.run(debug=True)