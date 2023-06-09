import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return "Hello, world!"

@app.route('/goodbye', methods=['GET'])
def get_goodbye():
    return "Farewell, to all the earthly remains~"

@app.route('/message', methods=['GET'])
def get_message():
    message = request.args['message']
    return f"{message}"


if __name__ == '__main__':
    app.run(
      debug=True,
      host="0.0.0.0" # Listen for connections _to_ any server
    )
