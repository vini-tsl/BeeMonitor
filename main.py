from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get("VERCEL"):
    database_path = "/tmp/beemonitor.db"
else:
    database_path = os.path.join(
        basedir, "instance", "beemonitor.db"
    )
    os.makedirs(os.path.dirname(database_path), exist_ok=True)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"sqlite:///{database_path}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ================= CONFIGURAÇÃO DO APP =================
app = Flask(__name__)
app.secret_key = '3j219i3n1bnu1wdh1u2dnh821kj'


from models import db
db.init_app(app)

# Importar rotas DEPOIS de inicializar o app e db
from route import *

if __name__ == "__main__":
    with app.app_context():
        # Criar diretório instance se não existir
        if not os.path.exists('instance'):
            os.makedirs('instance')
        db.create_all()
    app.run(debug=True)