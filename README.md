# Biblioteca_Flask
Exemplo de operações CRUD em bibilioteca Python utilizando Flask.

Código obtido a partir do canal Dev Aprender | Jhonatan de Souza

1 - Para realizar a consulta dos livros, utilize:
(Get) http://localhost:5000/livros

2 - Para realizar a consulta de um livro específico, por exemplo o livro de id 1:
(Get) http://localhost:5000/livros/1

3 - Para inserir um novo livro, por exemplo o livro de id 4:
(POST) http://localhost:5000/livros/
{
    "autor": "George Orwell",
    "id": 4,
    "titulo": "1984"
}

4 - Para modificar livro, por exemplo o livro de id 1:
(PUT) http://localhost:5000/livros/1
{
    "autor": "Kim Scott",
    "titulo": "Empatia Assertiva"
}


5 - Para excluir um livro, por exemplo o livro de id 3:
(DELETE) http://localhost:5000/livros/3
