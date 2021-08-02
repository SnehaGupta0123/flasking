from operator import methodcaller
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# FILTERS!!!
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags

# Create Flask Instance 
app = Flask(__name__)
# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Secret Key!
app.config['SECRET_KEY'] = "mysupersecretkey"
# Initialize the Database
db = SQLAlchemy(app)

# Create Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create A String
    def __repr__(self):
        return '<Name %r>' % self.name


# Create a Form Class
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's Your Name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create a route decorator

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    return render_template('add_user.html', form=form)

@app.route('/')

def index():
    first_name = "Sneha"
    some_stuff = "This is bold text"
    fav_pizza = ['Cheese', 'Capsicum', 'Triple Cheese', 55]
    return render_template('index.html', fn=first_name, stuff=some_stuff, pizza=fav_pizza)


@app.route('/user/<name>')

def user(name):
    return render_template('user.html', name=name)

#Create Custom Error Pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Internal Server Error 
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully!!")
    return render_template('name.html', name=name, form=form)