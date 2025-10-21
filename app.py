from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import uuid
import hashlib
import json

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://sonupd8294_db_user:Y6eT3NsBBFwZTGyJ@cluster0.kx2umfo.mongodb.net/")
db = client.todo_db
collection = db.items

@app.route('/')
def home():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form['itemName']
    item_desc = request.form['itemDescription']
    collection.insert_one({
        "_id": str(uuid.uuid4()),
        "name": item_name,
        "description": item_desc
    })
    return jsonify({"message": "Item added successfully!"})

@app.route('/api')
def api_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
