from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Nova Versão do Site: CI/CD Funciona Mesmo!"

if __name__ == "__main__":
    app.run(debug=True)
