from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Confirmado(db.Model):
    __tablename__ = "confirmado"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)


@app.route("/")
def lista():

    pessoas = Confirmado.query.order_by(
        Confirmado.nome
    ).all()

    return render_template(
        "confirmados.html",
        pessoas=pessoas
    )


if __name__ == "__main__":
    app.run(debug=True)