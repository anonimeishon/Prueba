from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import random
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./prueba.db'
db = SQLAlchemy(app)

class posthash(db.Model):
    id = db.Column(db.String, primary_key=True)
    def __repr__(self):
        return '<posthash %r>' % self.id


def hasheo():
    x = 'T000'

    for i in range (5):
        x = x + str(random.randint(0,9))
    y = hash(x)
    return (y)
print (hasheo())

x = hasheo()
elhash = posthash(id=x)
db.session.add(elhash)
db.session.commit()

