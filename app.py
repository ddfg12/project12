# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/me")
def me():

    name = "Afreen" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/aboutmyfather")
def aboutmyfather():

    name = "Valibaha" # write your name
    age = "42" # write your age

    return render_template('father.html' , name = name , age = age)
# define the route to mother webpage
@app.route("/aboutmymother")
def aboutmymother():

    name = "Zainabunnisha" # write your name
    age = "38" # write your age

    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/aboutmyfriend")
def aboutmyfriend():

    name = "Arushi" # write your name
    age = "14" # write your age

    return render_template('friend.html' , name = name , age = age)


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
