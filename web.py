from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from hashing import hasheo
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./prueba.db'
db = SQLAlchemy(app)

class posthash(db.Model):
    id = db.Column(db.String, primary_key=True)
    def __repr__(self):
        return '<posthash %r>' % self.id

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/chain', methods=['GET', 'POST'])
def writehash():

    if request.method == 'POST':
        elhash = posthash(id=hasheo())
        db.session.add(elhash)
        db.session.commit()
        return(render_template('post.html'))
        #return ('<h1>Added hash</h1><form action="/chain" method="GET"><input type="submit" value="Back"></form>')
    elif request.method == 'GET':
        return render_template('get.html')
        #return('<form action="/chain" method="POST"><input type="submit" value="Hash"></form>', )
        #<button type="button" onclick="alert('Hello world!')">Click Me!</button>
        #return(posthash.query.all())
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')