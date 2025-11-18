from flask import Flask, render_template
from data.portfolio import PERFIL, PROJETOS  # <-- Importando os dados!

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Define uma rota para a página inicial
@app.route("/")
def home():
    # Passa todos os dados (PERFIL e PROJETOS) para o template
    return render_template(
        "index.html",
        perfil=PERFIL,
        projetos=PROJETOS
    )
    
# O resto do arquivo (Gunicorn, etc.) permanece o mesmo.
# Lembre-se que o Gunicorn está configurado no Railway para iniciar!