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

# CORS(app)

api = Api(app)

class UserByID(Resource):
    def get(self, user_id):
        user = User.query.filter_by(User.id == id).first()
        response_body = user.to_dict()
        return make_response(jsonify(response_body), 200)

    def post(self):
        data = request.get_json()
        new_user = User(username=data['username'], password=data['password'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        response_body = new_user.to_dict()
        return make_response(jsonify(response_body), 201)
    
api.add_resource(UserByID, '/users/<int:user_id>')

class Countries(Resource):
    def get(self):
        countries = Country.query.all()
        response_body = [country.to_dict() for country in countries]
        return make_response(jsonify(response_body), 200)
    
api.add_resource(Countries, '/countries')

class CountryByID(Resource):
    def get(self, country_id):
        country = Country.query.filter_by(Country.id == id).first()
        response_body = country.to_dict()
        return make_response(jsonify(response_body), 200)

api.add_resource(CountryByID, '/countries/<int:country_id>')

class TripsByID(Resource):
    def get(self, trip_id):
        trip = Trip.query.filter_by(Trip.id == id).first()
        response_body = trip.to_dict()
        return make_response(jsonify(response_body), 200)

    def post(self):
        data = request.get_json()
        new_trip = Trip(
            user_id=data['user_id'], 
            country_id=data['country_id'], 
            date_visited=data['date_visited']
        )
        db.session.add(new_trip)
        db.session.commit()
        response_body = new_trip.to_dict()
        return make_response(jsonify(response_body), 201)

    def patch(self, trip_id):
        trip = Trip.query.filter_by(Trip.id == id).first()
        data = request.get_json()
        for attr in data:
            setattr(trip, attr, data[attr])
        db.session.commit()
        response_body = trip.to_dict()
        return make_response(jsonify(response_body), 200)

    def delete(self, trip_id):
        trip = Trip.query.filter_by(Trip.id == id).first()
        db.session.delete(trip)
        db.session.commit()
        return make_response(jsonify({'message': 'Trip deleted'}), 200)

api.add_resource(TripsByID, '/trips/<int:trip_id>')

if __name__ == '__main__':
    app.run(port=7000, debug=True)