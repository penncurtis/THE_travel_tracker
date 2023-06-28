from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    trips = db.relationship('Trip', backref='user', lazy=True)

    @validates('username', 'password', 'email')
    def validate_account(self, key, value):
        if not value:
            raise ValueError('Please create an account to continue :)')
        return value


class Country(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    trips = db.relationship('Trip', backref='country', lazy=True)


class Trip(db.Model):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    date_visited = db.Column(db.Date, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

    def __repr__(self):
        return f"Trip #{self.id}: User #{self.user_id} visited {self.country.name} on {self.date_visited}"