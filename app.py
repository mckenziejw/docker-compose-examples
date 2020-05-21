import time
from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)

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
client = MongoClient('mongo')
db = client.books

db.favorites.insert_many(books)

@app.route('/')
def get_favorites():
    book_client = MongoClient('mongo')
    book_db = book_client.books
    out = ''
    for entry in book_db.favorites.find():
        out += str(entry)
    return out

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"))