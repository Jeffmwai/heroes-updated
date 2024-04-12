from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from app.models import Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def serialize_hero(hero):
    return {
        'id': hero.id,
        'name': hero.name,
        'super_name': hero.super_name,
        'powers': [serialize_power(power) for power in hero.powers]
    }

def serialize_power(power):
    return {
        'id': power.id,
        'name': power.name,
        'description': power.description
    }

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([serialize_hero(hero) for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(serialize_hero(hero))
    else:
        return jsonify({'error': 'Hero not found'}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([serialize_power(power) for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(serialize_power(power))
    else:
        return jsonify({'error': 'Power not found'}), 404

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    data = request.json
    power = Power.query.get(id)
    if power:
        if 'description' in data:
            power.description = data['description']
            try:
                db.session.commit()
                return jsonify(serialize_power(power))
            except IntegrityError:
                db.session.rollback()
                return jsonify({'errors': ['Validation errors']}), 400
        else:
            return jsonify({'error': 'Missing description field'}), 400
    else:
        return jsonify({'error': 'Power not found'}), 404


@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    if all(key in data for key in ['strength', 'power_id', 'hero_id']):
        hero = Hero.query.get(data['hero_id'])
        power = Power.query.get(data['power_id'])
        if hero and power:
            try:
                hero_power = HeroPower(strength=data['strength'], hero=hero, power=power)
                db.session.add(hero_power)
                db.session.commit()
                return jsonify(serialize_hero(hero))
            except IntegrityError:
                db.session.rollback()
                return jsonify({'errors': ['Validation errors']}), 400
        else:
            return jsonify({'error': 'Hero or Power not found'}), 404
    else:
        return jsonify({'error': 'Missing fields'}), 400

if __name__ == '__main__':
    app.run(port=5555)
