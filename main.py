from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)

app.config['SECRET_KEY'] = 'test'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

def add_to_db(new_name, new_desc):
    existing_drink = Drink.query.filter_by(name=new_name).first()
    if existing_drink is None:
        drink = Drink(name= new_name, description=new_desc)
        db.session.add(drink)
        db.session.commit()
        print(f'Added: {drink}')
    else:
        print(f'Drink with name {new_name} already exists. Skipping.')

@app.route('/')
def index():
    return 'Hello'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []

    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)

    return {"drinks":output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return jsonify({"name": drink.name, "description": drink.description})

@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    existing_drink = Drink.query.filter_by(name=drink.name).first()
    if existing_drink is None:
        db.session.add(drink)
        db.session.commit()
        print(Drink.query.all())
        return {'id': drink.id}
    else:
        return {'error': f"{drink.name} already Exists in db"}
    
with app.app_context():
    db.create_all()
    add_to_db("test name", "test description")
    add_to_db("soda", "very sweet")
    add_to_db("cola", "cola cola")
    add_to_db("sprite", "lime")
    print(Drink.query.all())

if __name__ == '__main__':
    app.run(debug=True)

