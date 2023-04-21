#!/usr/bin/python3
"""Starts a Flask web application.
100-hbnb
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """The hbnb page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                            states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """The Flask app/request context end event listener."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
