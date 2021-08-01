from flask import Flask, render_template


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

# Create a route decorator
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