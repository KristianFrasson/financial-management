from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta'  # Substitua por uma chave secreta segura

jwt = JWTManager(app)

users = {
    'usuario': 'senha'  # Usuário de exemplo
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({'msg': 'Username e senha são requeridos'}), 400
    if users.get(username) != password:
        return jsonify({'msg': 'Credenciais inválidas'}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)