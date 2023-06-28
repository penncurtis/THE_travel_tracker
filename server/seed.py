#!/usr/bin/env python3

from app import app
from models import db, User, Country, Trip
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    # List of countries
    country_names = [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
        "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
        "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
        "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
        "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada",
        "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
        "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark", "Djibouti",
        "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador",
        "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji",
        "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece",
        "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
        "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq",
        "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan",
        "Kenya", "Kiribati", "Korea, North", "Korea, South", "Kosovo", "Kuwait",
        "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
        "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
        "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius",
        "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro",
        "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
        "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway",
        "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru",
        "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda",
        "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
        "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
        "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
        "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka",
        "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan",
        "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia",
        "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
        "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City",
        "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
    ]

    def seed_countries():
        for country_name in country_names:
            country = Country(name=country_name)
            db.session.add(country)

        db.session.commit()

    user_data = [
        {"username": "john123", "password": "password123", "email": "john@example.com"},
        {"username": "emma456", "password": "password456", "email": "emma@example.com"},
        {"username": "alex789", "password": "password789", "email": "alex@example.com"},
    ]

    # Function to seed users
    def seed_users():
        for data in user_data:
            user = User(**data)
            db.session.add(user)

        db.session.commit()
    
    # List of trip data
    trip_data = [
        {"user_id": 1, "country_id": 10, "date_visited": date(2022, 5, 10)},
        {"user_id": 1, "country_id": 27, "date_visited": date(2022, 7, 22)},
        {"user_id": 2, "country_id": 5, "date_visited": date(2023, 1, 5)},
        {"user_id": 3, "country_id": 45, "date_visited": date(2023, 3, 18)},
    ]

    # Function to seed trips
    def seed_trips():
        for data in trip_data:
            trip = Trip(**data)
            db.session.add(trip)

        db.session.commit()

    # Main seeding function
    def seed():
        seed_countries()
        seed_users()
        seed_trips()

    # Run the seeding function
    seed()
    print("🌱 Countries, Users, and Trips successfully seeded! 🌱")
