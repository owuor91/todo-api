#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
	'id':1,
	'title': u'Buy groceries',
	'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
	'id':2,
	'title': u'Learn python',
	'description': u'Need to find a good python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
