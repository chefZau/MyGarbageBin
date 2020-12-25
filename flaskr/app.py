from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


def main():
    app.run(debug=True)

main()