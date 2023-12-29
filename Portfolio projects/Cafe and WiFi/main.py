from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
import sqlite3
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
import os

# Get the absolute path of the "instance" folder
basedir = os.path.abspath(os.path.dirname(__file__))
instance_path = os.path.join(basedir, 'instance')

# Specify the database file path inside the "instance" folder
db_path = os.path.join(instance_path, 'somecafes.db')

# Set the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

# Check if the database file exists
if not os.path.exists(db_path):
    # Create the "instance" folder if it doesn't exist
    os.makedirs(instance_path)

    # Create an empty database file
    open(db_path, 'w').close()

db = SQLAlchemy(app)

class Cafe(db.Model):
    __tablename__ = 'cafe'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    map_url = db.Column(db.String(200), nullable=False)
    img_url = db.Column(db.String(200), nullable=False)


class CafeForm(FlaskForm):
    name = StringField('The Name Of The Cafe', validators=[DataRequired()])
    map_url = StringField('The Link to the Google Map', validators=[DataRequired()])
    img_url = StringField('Image Link of the Cafe', validators=[DataRequired()])
    submit = SubmitField('Add Cafe')

@app.route('/')
def hello():
    conn = sqlite3.connect('somecafes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, map_url, img_url FROM cafe')
    results = cursor.fetchall()
    conn.close()

    data = zip([row[0] for row in results], [row[1] for row in results], [row[2] for row in results])
    return render_template('index.html', data=data)

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()  # Create an instance of the CafeForm
    
    if form.validate_on_submit():
        name = form.name.data
        map_url = form.map_url.data
        img_url = form.img_url.data

        new_cafe = Cafe(name=name, map_url=map_url, img_url=img_url)
        db.session.add(new_cafe)
        db.session.commit()

        return 'Cafe added successfully'

    return render_template('add.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
