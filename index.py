from flask import Flask
from getName import getLukesName
app = Flask(__name__)

@app.route('/')
def hello_world():
    return getLukesName()