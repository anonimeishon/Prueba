from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from hashing import hasheo
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./prueba.db'
db = SQLAlchemy(app)

class posthash(db.Model):
    id = db.Column(db.String, primary_key=True)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/chain', methods=['GET', 'POST'])
def writehash():
    if request.method == 'POST':
        elhash = posthash(id=hasheo())
        db.session.add(elhash)
        db.session.commit()
        return '<h1>Added hash</h1>'
    elif request.method == 'GET':
        return(posthash.query.all())
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')