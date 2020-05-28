import time
import os
from flask import Flask, request
from pymongo import MongoClient

template_path = os.environ.get('TEMPLATE_DIR')

app = Flask(__name__, template_folder=template_path)

## Populate the mongodb
books = [
    {'author':{
        'first_name': 'Leo',
        'last_name' : 'Tolstoy'
        },
    'title': 'Anna Karenina'
    },
    {'author':{
        'first_name': 'Walt',
        'last_name' : 'Whitman'
        },
    'title': 'Leaves of Grass'
    },
    {'author':{
        'first_name': 'Tom',
        'last_name' : 'Wolfe'
        },
    'title': 'Bonfire of the Vanities'
    },
    {'author':{
        'first_name': 'Charles',
        'last_name' : 'Bukowski'
        },
    'title': 'Ham on Rye'
    }
]

## Create a client instance
client = MongoClient('mongo')

db = client.books

db.favorites.insert_many(books)

@app.route('/')
def get_favorites():
    book_client = MongoClient('mongo')
    book_db = book_client.books
    books = []
    for entry in book_db.favorites.find():
        books.append(entry)
    return render_template("index.html", books=books)

# @app.route('/add', methods=['POST'])
# def add_book():
#     new_book = request.json
#     if 'author' in new_book and 'title' in new_book:
#       book_client = MongoClient('mongo')
#       book_db = book_client.books
#       book_db.favorites.insert_one(new_book)
#       return "success"
#     else:
#       abort(400, message="Book not correctly formatted")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"))
