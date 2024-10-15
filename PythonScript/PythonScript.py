from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {'id': 1, 'title': 'How to kill a dog', 'author': 'Ali Nazeer'},
    {'id': 2, 'title': 'Gotta love life', 'author': 'Ali Tamer'}
    ]

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, world")

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    book = next((book for book in books if book['id'] == id), None)
    return jsonify(book) if book else ("Not found", 404)

@app.route('/books', methods=['POST'])
def add_books():
    new_book = request.json
    new_book['id'] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_books(id):
    book = next((book for book in books if book['id'] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    
    data = request.json
    book['title'] = data.get('title', book['title'])
    book['author'] = data.get('author', book['author'])
    return jsonify(book)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    book = next((book for book in books if book['id'] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    books = [b for b in books if b['id'] != id]
    return jsonify({"message": "Book deleted successfully"}), 204


if __name__ == '__main__':
    app.run(debug=True)