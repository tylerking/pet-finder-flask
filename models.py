from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    name = db.Column('Name', db.String())
    age = db.Column('Age', db.String())
    breed = db.Column('Breed', db.String())
    color = db.Column('Color', db.String())
    size = db.Column('size', db.String())
    weight = db.Column('Weight', db.String())
    url = db.Column('URL', db.String())
    alt = db.Column('ALT Text', db.String())
    pet_type = db.Column('Type', db.String())
    gender = db.Column('Gender', db.String())
    spay = db.Column('Spay', db.String())
    house_trained = db.Column('House Trained', db.String())
    description = db.Column('Description', db.Text)

    def __repr__(self):
        return f'''<Pet Name: {self.name} Age: {self.age} 
                    Breed: {self.breed} Color: {self.color}
                    Size: {self.size} Weight: {self.weight}
                    URL: {self.url} Type: {self.pet_type}
                    Gender: {self.gender} Spay: {self.spay}
                    House Trained: {self.house_trained}
                    Description: {self.description}>'''