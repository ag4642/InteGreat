from flask import Flask
from flask import request
from PyMongo import MongoClient

app = Flask(__name__)
mongo = MongoClient('localhost', 5000)
db = mongo['we<3mongo']

@app.route('/add', methods = ['POST'])
def add_to_workbook():
    if request.method == 'POST':
        jpeg = request.form['jpeg']
        book = request.form['name']

        if db.books.count() == 0:
            db.books.createCollection(book)

        else:




@app.route('/get', methods=['GET'])
def get_workbook():
    if request.method == 'GET':
        name = request.args.get['name']

        return db.name
