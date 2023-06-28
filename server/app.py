#!/usr/bin/env python3

import ipdb

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from models import db, User, Country, Trip

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

CORS(app)

api = Api(app)

class Users(Resource):
    def get(self):
        users = User.query.all()
        response_body = [user.to_dict() for user in users]
        return make_response(jsonify(response_body), 200)
    
    def post(self):
        data = request.get_json()
        new_user = User(username=data['username'], password=data['password'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        response_body = new_user.to_dict()
        return make_response(jsonify(response_body), 201)

api.add_resource(Users, '/users')

class UserByID(Resource):
    def get(self, id):
        user = User.query.filter_by(id = id).first()
        response_body = user.to_dict()
        return make_response(jsonify(response_body), 200)
    
    def delete(self, id):
        user = User.query.filter_by(id = id).first()
        db.session.delete(user)
        db.session.commit()
        return make_response(jsonify({'message': 'User deleted'}), 204)
    
api.add_resource(UserByID, '/users/<int:id>')

class Countries(Resource):
    def get(self):
        countries = Country.query.all()
        response_body = []
        for country in countries:
            response_body.append(country.to_dict())
        return make_response(jsonify(response_body), 200)
    
api.add_resource(Countries, '/countries')

class CountryByID(Resource):
    def get(self, id):
        country = Country.query.filter_by(id = id).first()
        response_body = country.to_dict()
        return make_response(jsonify(response_body), 200)

api.add_resource(CountryByID, '/countries/<int:id>')


class Trips(Resource):
    def get(self):
        trips = Trip.query.all()
        response_body = [trip.to_dict() for trip in trips]
        return make_response(jsonify(response_body), 200)
    
    def post(self, id):
        data = request.get_json()
        new_trip = Trip(
            user_id=data['user_id'], 
            country_id=data['country_id'], 
            date_visited=data['date_visited'].date()
        )
        db.session.add(new_trip)
        db.session.commit()
        response_body = new_trip.to_dict()
        return make_response(jsonify(response_body), 201)
    
api.add_resource(Trips, '/trips')

class TripsByID(Resource):
    def get(self, id):
        trip = Trip.query.filter_by(id=id).first()
        response_body = trip.to_dict()
        return make_response(jsonify(response_body), 200)

    def patch(self, id):
        trip = Trip.query.filter_by(id = id).first()
        data = request.get_json()
        for attr in data:
            setattr(trip, attr, data[attr])
        db.session.commit()
        response_body = trip.to_dict()
        return make_response(jsonify(response_body), 202)

    def delete(self, id):
        trip = Trip.query.filter_by(id = id).first()
        db.session.delete(trip)
        db.session.commit()
        return make_response(jsonify({'message': 'Trip deleted'}), 204)

api.add_resource(TripsByID, '/trips/<int:id>')

if __name__ == '__main__':
    app.run(port=7000, debug=True)