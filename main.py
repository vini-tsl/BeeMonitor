import os
from flask import Flask
from models import db

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "chave-temporaria-para-testes"
)

# Configuração do SQLite
if os.environ.get("VERCEL"):
    database_path = "/tmp/beemonitor.db"
else:
    basedir = os.path.abspath(os.path.dirname(__file__))
    instance_path = os.path.join(basedir, "instance")

    os.makedirs(instance_path, exist_ok=True)

    database_path = os.path.join(
        instance_path,
        "beemonitor.db"
    )

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"sqlite:///{database_path}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Importar rotas
from route import *

# Criar tabelas durante a inicialização
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
