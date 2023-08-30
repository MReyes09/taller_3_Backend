from flask import Flask, jsonify, request
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.base import Base
from config import credenciales
from sqlalchemy import create_engine
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

engine = create_engine(credenciales.DB_URL)
Session = sessionmaker(engine)

session_ = Session() # Instancia a utilizar

@app.route('/', methods = ['GET'])

def home():
    
    return jsonify({'Respuesta':'Hola Mundo'})

def init_database():
    
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

@app.route('/usuario_nuevo', methods = ['POST'])

def create_User():
    
    try:
        
        data = request.json
        username = data.get('username')
        password = data.get('password')
        # creo un objeto usuario para agregarlo a mi DB
        user_new = User(username = username, password = password)
        session_.add(user_new) # envio mi objeto usuario a la DB
        session_.commit() # guardo los cambios
        return jsonify({'msj':'Usuario creado correctamente', 'User creado':data})
        
    except KeyError:
        
        print("No se incluyeron todos los atributos")
        return jsonify({"error":"No se incluyeron todos los atributos"})

@app.route('/listar_Usuarios', methods = ['GET'])

def list_User():
    
    data = session_.query(User.username,
                          User.password).all()
    response = []
    
    for d in data:
        
        response.append({
            'username': d.username,
            'passowrd': d.password
        })
        
    return jsonify(response)

@app.route('/actualizar_Usuario/<int:id>', methods=['PUT'])

def update_User(id):
    
    user_ = session_.query(User).get(id)
    
    if user_ is None:
        
        return jsonify({"msj":"El usuario no fue encontrado"})
    
    data = request.get_json()
    
    if 'id' in data:
        
        return jsonify({"msj":"El id no es un dato actualizable"})
    
    username = data.get('username')
    password = data.get('password')
    
    if username:
        
        user_.username = username
        
    if password:
        
        user_.password = password
        
    session_.commit()
    
    return jsonify({"msj":"El usuario fue actualizado"})
    
@app.route('/eliminar_Usuario/<int:id>', methods=['DELETE'])

def delete_User(id):

    user_ = session_.query(User).get(id)
    
    if user_ is None:
        
        return jsonify({"msj":"El usuario no fue encontrado"})
    
    session_.delete(user_)
    session_.commit()
    return jsonify({"msj":"El usuario fue eliminado"})
        
if __name__ == "__main__":
    
    with app.app_context():
        # init_database()
        app.run(host = "0.0.0.0", port = 8000, debug=True)