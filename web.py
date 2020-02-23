from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from hashing import hasheo
import sqlite3
from flask_marshmallow import Marshmallow

#Flask configs
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./prueba.db'

#db configs
db = SQLAlchemy(app)
ma = Marshmallow(app)


#Db structure
class posthash(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String)


#Helping marshamllow make the json file
class Postschema(ma.ModelSchema):
    class Meta:
        model = posthash


#for adding hashes to the db
def addhashtodb():
    last = posthash.query.order_by(posthash.id.desc()).first()
    if last == None:
        elid = 1
    else:    
        elid = int(last.id) + 1
    elhash = posthash(id=elid,hash=hasheo())
    #This part adds them to the db file
    db.session.add(elhash)
    db.session.commit()


#routes
@app.route('/')
def hello_world():
    return ('<form action="/chain" method="GET"><input type="submit" value="See hash chain"></form>')


#This route will show every object added to the db
@app.route('/chain', methods=['GET', 'POST'])
def writehash():

    if request.method == 'POST':
        addhashtodb()
        return(render_template('post.html'))
    elif request.method == 'GET':
        hashes = posthash.query.all()
        return render_template('get.html',hashes = hashes, title= "Show hashes")
 

#This route will show the last object added to the db
@app.route('/chain/last', methods=['GET'])
def getlasthash():
    last = posthash.query.order_by(posthash.id.desc()).first()
    return render_template('last.html', last=last, title="Last hash")


#This route will show the db objects in a .json file
@app.route('/api/v1/chain')
def showjson():
    #main()
    hashes = posthash.query.all()
    
    hash_schema = Postschema(many=True)
    output = hash_schema.dump(hashes)
    return(jsonify({'hashes' : output}))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')