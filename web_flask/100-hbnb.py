#!/usr/bin/python3
""" Script that starts a Flask web application """
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ display HTML page """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities,
                           places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
