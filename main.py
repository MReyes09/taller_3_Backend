from flask import Flask, jsonify, request
from sqlalchemy.orm import sessionmaker
from models import user
from models.base import Base
from config import credenciales
from sqlalchemy import create_engine


app = Flask(__name__)

engine = create_engine(credenciales.DB_URL)
Session = sessionmaker(engine)

Session_ = Session() # Instancia a utilizar

@app.route('/', methods = {'GET'})

def home():
    
    return jsonify({'Respuesta':'Hola Mundo'})

def init_database():
    
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    
    with app.app_context():
        init_database()
        app.run(host = "0.0.0.0", port = 8000, debug=True)