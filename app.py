# API é um lugar para disponibilizar recursos e/ou funcionalidades
# 1. Objetivo - Criar uma api que disponibiliza a consulta, criação edição e exclusão de livros
# 2. URL Base - localhost
# 3. Endpoints - 
    # - localhost/livros (GET)
    # - localhost/livros (POST)
    # - localhost/livros/id (GET)
    # - localhost/livros/id (PUT)
    # - localhost/livros/id (DELETE)

# 4. Quais recursos: Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

# Fonte de dados
livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Hábitos Atômicos'
    },
]

# Consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


# Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)


# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)
