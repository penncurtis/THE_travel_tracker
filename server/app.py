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
        user = User.query.get_or_404(user_id)
        response_body = user.to_dict()
        return make_response(jsonify(response_body), 200)

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.username = data['username']
        user.password = data['password']
        user.email = data['email']
        db.session.commit()
        response_body = user.to_dict()
        return make_response(jsonify(response_body), 200)

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return make_response(jsonify({'message': 'User deleted'}), 200)

api.add_resource(UserByID, '/users/<int:user_id>')

class Trips(Resource):
    def get(self):
        trips = Trip.query.all()
        response_body = [trip.to_dict() for trip in trips]
        return make_response(jsonify(response_body), 200)

    def post(self):
        try:
            data = request.get_json()
            new_trip = Trip(user_id=data['user_id'], country_id=data['country_id'], date_visited=data['date_visited'])
            db.session.add(new_trip)
            db.session.commit()
            response_body = new_trip.to_dict()
            return make_response(jsonify(response_body), 201)
        except ValueError as error:
            response_body = {
                "error": error.args
            }
            return make_response(jsonify(response_body), 422)

api.add_resource(Trips, '/trips')

class TripByID(Resource):
    def get(self, trip_id):
        trip = Trip.query.get_or_404(trip_id)
        response_body = trip.to_dict()
        return make_response(jsonify(response_body), 200)

    def put(self, trip_id):
        trip = Trip.query.get_or_404(trip_id)
        data = request.get_json()
        trip.user_id = data['user_id']
        trip.country_id = data['country_id']
        trip.date_visited = data['date_visited']
        db.session.commit()
        response_body = trip.to_dict()
        return make_response(jsonify(response_body), 200)

    def delete(self, trip_id):
        trip = Trip.query.get_or_404(trip_id)
        db.session.delete(trip)
        db.session.commit()
        return make_response(jsonify({'message': 'Trip deleted'}), 200)

api.add_resource(TripByID, '/trips/<int:trip_id>')

class CountryByID(Resource):
    def get(self, country_id):
        country = Country.query.get_or_404(country_id)
        response_body = country.to_dict()
        return make_response(jsonify(response_body), 200)

api.add_resource(CountryByID, '/countries/<int:country_id>')

if __name__ == '__main__':
    app.run(port=7000, debug=True)