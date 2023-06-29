###
## World Travel Tracker
Welcome to World Travel Tracker, a Python Flask application that tracks users their trips to different countries. This application utilizes a backend built with Flask and a frontend implemented with React.

## Getting Started
Follow these instructions to get started with World Travel Tracker:

- Fork and then Clone this repository.

- Navigate to the directory (folder) that contains the Pipfile, and run pipenv install in your terminal to install the required Python libraries.

- Activate the pipenv virtual environment by running pipenv shell in your terminal.

- Install the dependencies for the React app by running npm install --prefix client in your terminal.

- Move into the server directory by entering the command cd server in the terminal.

- Run the Flask app by executing python app.py in the terminal. Make sure you are in the server directory before running this command.

- Open a new terminal, and run npm start --prefix client to launch the React app in the browser. If your browser does not automatically open the page, visit http://localhost:4000 to view the app.

Enjoy tracking your world travels with World Travel Tracker!

## Backend
The backend of World Travel Tracker is built using a relational database with three tables: users, trips, and countries. Here is an overview of these tables:

- Users: This table stores information about the users of the application. It includes fields such as id, username, age, and email.

- Countries: This table contains details about different countries. It includes fields such as id, country_name, country_code, and country_image.

- Trips: This table links the users and countries tables and represents the trips taken by the users. It includes fields such as id, date_visited, user_id, and country_name.

## Frontend
The frontend of World Travel Tracker is built using a series of React components.

The user lands on the homepage that showcases all the world's countries and features a search bar that the user can use to sort through them.

There is a route built into the nav bar that brings users to a page through which they can add a new trip that will post to the backend database and persist. 

There is another route built into the nav bar that brings users to a page upon which there are two distinct forms displayed. One form allows the user to modify a value of an existing trip. The other form allows a user to delete a trip in its entirety.

Finally, there is a route built into the nav bar that brings users to a page which showcases all of the distinct users have taken. On this page there is also a search bar that the user can use to sort through the trips by user id.

## Author's notes
There is functionality present in the code that has not been fully fleshed out, but may be at a later date. Specifically, functionality regarding login/logout/sessions to allow for a mode 'social-media-like' experience. For the purposes of this project, we found it more pragmatic to showcase the efficacy of the routes themselves and connection to the front-end for our python flask application.
