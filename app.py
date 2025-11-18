from flask import Flask, render_template
import os
from datetime import datetime

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Define uma rota para a página inicial
@app.route("/")
def home():
    # Coleta informações para passar ao template
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    app_version = os.environ.get("APP_VERSION", "1.0.0") # Exemplo de variável de ambiente
    deployment_env = os.environ.get("RAILWAY_ENVIRONMENT_NAME", "Local")

    # Renderiza o template index.html, passando as variáveis
    return render_template(
        "index.html",
        titulo="CI/CD Flask Profissional",
        versao=app_version,
        hora_atual=current_time,
        ambiente=deployment_env
    )

# Comentado para usar Gunicorn (melhor prática de CI/CD/deploy)
# if __name__ == "__main__":
#     app.run(debug=True)