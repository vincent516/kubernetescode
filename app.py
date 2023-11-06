from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'The only winning move is not to play!!!'
