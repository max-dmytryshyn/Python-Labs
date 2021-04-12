from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
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

    def update(self, made_of_material, username, length_in_cm, material_to_saw, drive_type):
        self.__init__(made_of_material, username, length_in_cm, material_to_saw, drive_type)


def get_saw_by_id(id):
    saw = Saw.query.get(id)
    if saw is None:
        return abort(404)
    return saw


class SawSchema(ma.Schema):
    class Meta:
        fields = ('made_of_material', 'username', 'length_in_cm', 'material_to_saw', 'drive_type')


saw_schema = SawSchema()
saws_schema = SawSchema(many=True)


@app.route("/saw", methods=["POST"])
def add_saw():
    fields = saw_schema.load(request.json)
    new_saw = Saw(**fields)

    db.session.add(new_saw)
    db.session.commit()

    return saw_schema.jsonify(new_saw)


@app.route("/saw", methods=["GET"])
def get_saw():
    all_saws = Saw.query.all()
    result = saws_schema.dump(all_saws)
    return jsonify(result)


@app.route("/saw/<id>", methods=["GET"])
def saw_detail(id):
    saw = get_saw_by_id(id)
    return saw_schema.jsonify(saw)


@app.route("/saw/<id>", methods=["PUT"])
def saw_update(id):
    saw = get_saw_by_id(id)
    fields = saw_schema.load(request.json)
    saw.update(**fields)

    db.session.commit()
    return saw_schema.jsonify(saw)


@app.route("/saw/<id>", methods=["DELETE"])
def saw_delete(id):
    saw = get_saw_by_id(id)
    db.session.delete(saw)
    db.session.commit()

    return saw_schema.jsonify(saw)


if __name__ == '__main__':
    app.run(debug=True)
