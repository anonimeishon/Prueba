from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from hashing import hasheo
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////./prueba.db'
db = SQLAlchemy(app)

class posthash(db.Model):
    id = db.Column(db.String(80), unique=True)
    def __repr__(self):
        return '<hashed %r>' % self.hashed

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/chain')
def adioh():
    return 'adioh'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')