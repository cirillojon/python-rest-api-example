from flask import Flask
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

@app.route('/')
def index():
    return 'Hello'

@app.route('/drinks')
def get_drinks():
    return {"drinks":"drink data"}

def add_to_db(new_name, new_desc):
    existing_drink = Drink.query.filter_by(name=new_name).first()
    if existing_drink is None:
        drink = Drink(name= new_name, description=new_desc)
        db.session.add(drink)
        db.session.commit()
        print(f'Added: {drink}')
    else:
        print(f'Drink with name {new_name} already exists. Skipping.')

with app.app_context():
    db.create_all()
    add_to_db("test name", "test description")
    add_to_db("soda", "very sweet")
    print(Drink.query.all())

if __name__ == '__main__':
    app.run(debug=True)