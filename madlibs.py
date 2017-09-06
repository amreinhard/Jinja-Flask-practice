"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/game')
def show_madlib_form():
    """Shows madlib form to user."""

    answer = request.args.get("yes-no")

    if answer == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/goodbye')
def goodbye():
    """Shows madlib form to user."""

    return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    """Returns completed madlib to user."""

    picked = choice(["madlib.html", "madlib1.html", "madlib2.html", "madlib3.html"])
    listy = ['person', 'color', 'noun', 'adjective', 'cat', 'dog', 'thrones']

    person = request.args.get('person')
    color = request.args.get('color')
    noun = request.args.get('noun')
    adjective = request.args.get('adjective')
    thrones = request.args.get('thrones')
    cat = request.args.get('cat')
    dog = request.args.get('dog')

    return render_template(picked, person=person, color=color,
    noun=noun, adjective=adjective, cat=cat, dog=dog, thrones=thrones, listy=listy)

@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    person = request.args.get("person")

    compliment = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=person,
                           compliment=compliment)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
