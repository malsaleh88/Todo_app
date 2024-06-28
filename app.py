from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Connection string for MongoDB
mongo_uri = "mongodb://localhost:27017"

# Create a connection to MongoDB
client = MongoClient(mongo_uri)

# Connect to the 'todo_app' database
db = client.todo_app

# Reference the 'tasks' collection
tasks_collection = db.tasks

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_task', methods=['POST'])
def add_task():
    try:
        task = request.json.get('task')
        if task:
            result = tasks_collection.insert_one({"task": task})
            logging.debug(f"Inserted task with _id: {result.inserted_id}")
            return jsonify({"status": "success", "task": task}), 200
        else:
            logging.error("No task provided")
            return jsonify({"status": "error", "message": "No task provided"}), 400
    except Exception as e:
        logging.error(f"Error inserting task: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
