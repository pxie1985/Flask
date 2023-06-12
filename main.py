# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)


#create a route decorator

@app.route('/')  # root route

def index():
    first_name = 'Peng'
    stuff = 'This is  <strong> bold </strong> font'
    favorite_list = ['PC','PS', 'NS']
    return render_template('index.html', first_name= first_name, stuff= stuff, favorite_list= favorite_list)

#localhost:5000/user/px
@app.route('/user/<name>')

def user(name):
    return render_template('user.html', user_name = name)

# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# interval server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)