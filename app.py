from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
# Import for Migrations
from flask_migrate import Migrate, migrate
import sqlite3

# Settings for migrations


app = Flask(__name__)
app.debug = True
# adding configuration for using a sqlite database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Models
class Profile(db.Model):
    # Id : Field which stores unique id for every row in
    # database table.
    # first_name: Used to store the first name if the user
    # last_name: Used to store last name of the user
    # Age: Used to store the age of the user
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    minority = db.Column(db.String(20), unique=False, nullable=True)
    caste = db.Column(db.String(20), unique=False, nullable=False)
    gender = db.Column(db.String(20), unique=False, nullable=False)
    income = db.Column(db.Integer, nullable=False)

    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"Name : {self.name}, Age: {self.age}, Minority: {self.minority}, Caste: {self.caste}, Gender: {self.gender}, Annual Income: {self.income} "


@app.route('/')
def index():
	return render_template('home.html')
@app.route('/Page-1.html')
def page():
    return render_template('Page-1.html')


# function to add profiles
@app.route('/profiles', methods=["POST"])
def profile():
    # In this function we will input data from the
    # form page and store it in our database.
    # Remember that inside the get the name should
    # exactly be the same as that in the html
    # input fields
    name = request.form.get("name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    caste = request.form.get("caste")
    minority = request.form.get("minority")
    income = request.form.get("income")
    # create an object of the Profile class of models
    # and store data as a row in our datatable
    if name != '':
        p = Profile(name=name, age=age, gender=gender, caste=caste, minority=minority, income=income)
        db.session.add(p)
        db.session.commit()
        conn = sqlite3.connect('bom.db')
        cursor = conn.execute("select scheme from data where gender1=?", (gender,))
        result = cursor.fetchall()
        conn.close()
        return render_template('/Page-2.html', result=result)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run()
