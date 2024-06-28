from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connection string for MongoDB
mongo_uri = "mongodb://localhost:27017"

# Create a connection to MongoDB
client = MongoClient(mongo_uri)

# Connect to the 'todo_app' database
db = client.todo_app


tasks_collection = db.tasks

@app.route('/')
def hello_world():
    return 'Hello World! Connected to MongoDB!'


@app.route('/index')
def home():  # put application's code here
    return render_template('index.html',name='PyCharm')

if __name__ == '__main__':
    app.run()
