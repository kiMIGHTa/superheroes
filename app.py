#!/usr/bin/env python3

from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Hero, HeroPower, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
CORS(app)

@app.route('/')
def home():
    return ''

@app.route('/heroes', methods=['GET'])
def heroes():
    if request.method == 'GET':
        heroes = [hero.to_dict() for hero in Hero.query.all()]
        return make_response(jsonify(heroes),200)

@app.route('/heroes/<int:id>', methods=['GET'])    
def hero(id):
    if request.method == 'GET':
        hero = Hero.query.filter_by(id=id).first()
        if hero is None:
            return jsonify({"error": "Hero not found"}), 404
        return make_response(jsonify(hero.to_dict()),200)
    
@app.route('/powers', methods=['GET'])
def powers():
    if request.method == 'GET':
        powers = [power.to_dict() for power in Power.query.all()]
        return make_response(jsonify(powers),200)
    
@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def power(id):
    if request.method == 'GET':
        power = Power.query.filter_by(id=id).first()
        if power is None:
            return jsonify({"error": "Power not found"}), 404
        return make_response(jsonify(power.to_dict()),200)
    elif request.method == 'PATCH':
        power = Power.query.filter_by(id=id).first()
        data=request.get_json()
        for attr in data:
            setattr(power, attr, data[attr])
        db.session.commit()
        return make_response(jsonify(power.to_dict()),200)    

@app.route('/hero_powers', methods=['POST'])   
def hero_powers():
    if request.method == 'POST':
        new_hero_power = HeroPower(
            strength=request.form['strength'],
            hero_id=request.form['hero_id'],
            power_id=request.form['power_id']
        )
        db.session.add(new_hero_power)
        db.session.commit()

        return make_response(jsonify(new_hero_power.to_dict()),201)
    
    




if __name__ == '__main__':
    app.run(port=5555)
