from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import mysql.connector
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://flask_tutorial:flask01.04.2021@localhost:3306/lab-6'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Saw(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    made_of_material = db.Column(db.String(80), unique=False)
    username = db.Column(db.String(80), unique=False)
    length_in_cm = db.Column(db.Float, unique=False)
    material_to_saw = db.Column(db.String(80), unique=False)
    drive_type = db.Column(db.String(80), unique=False)

    def __init__(self, made_of_material, username, length_in_cm, material_to_saw, drive_type):
        self.made_of_material = made_of_material
        self.username = username
        self.length_in_cm = length_in_cm
        self.material_to_saw = material_to_saw
        self.drive_type = drive_type

    def serialize(self):
        return {
                "made_of_material": self.made_of_material,
                "username": self.username,
                "length_in_cm": self.length_in_cm,
                "material_to_saw": self.material_to_saw,
                "drive_type": self.drive_type
                }


class SawSchema(ma.Schema):
    class Meta:
        fields = ('made_of_material', 'username', 'length_in_cm', 'material_to_saw', 'drive_type')


saw_schema = SawSchema()
saws_schema = SawSchema(many=True)


@app.route("/saw", methods=["POST"])
def add_saw():
    made_of_material = request.json['made_of_material']
    username = request.json['username']
    length_in_cm = request.json['length_in_cm']
    material_to_saw = request.json['material_to_saw']
    drive_type = request.json['drive_type']

    new_saw = Saw(made_of_material, username, length_in_cm, material_to_saw, drive_type)

    db.session.add(new_saw)
    db.session.commit()

    return jsonify(new_saw.serialize())


# endpoint to show all users
@app.route("/saw", methods=["GET"])
def get_saw():
    all_saws = Saw.query.all()
    result = saws_schema.dump(all_saws)
    return jsonify(result)


@app.route("/saw/<id>", methods=["GET"])
def saw_detail(id):
    saw = Saw.query.get(id)
    return saw_schema.jsonify(saw)


@app.route("/saw/<id>", methods=["PUT"])
def saw_update(id):
    saw = Saw.query.get(id)
    made_of_material = request.json['made_of_material']
    username = request.json['username']
    length_in_cm = request.json['length_in_cm']
    material_to_saw = request.json['material_to_saw']
    drive_type = request.json['drive_type']

    saw.made_of_material = made_of_material
    saw.username = username
    saw.length_in_cm = length_in_cm
    saw.material_to_saw = material_to_saw
    saw.drive_type = drive_type

    db.session.commit()
    return saw_schema.jsonify(saw)


@app.route("/saw/<id>", methods=["DELETE"])
def saw_delete(id):
    saw = Saw.query.get(id)
    db.session.delete(saw)
    db.session.commit()

    return saw_schema.jsonify(saw)


if __name__ == '__main__':
    app.run(debug=True)
