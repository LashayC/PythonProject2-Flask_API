#!/usr/bin/env python3
""" Flask API for Chinese Zodiac Animals """

# imports
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template
from flask import escape
from flask import url_for
import json

# create instance of Flask object
app = Flask(__name__)

# read zodiac.json from file
with open("zodiac.json", "r") as zodiac_file:
    # decode json to pythonic data
    zodiac_data = json.load(zodiac_file)

# route to return JSON data
@app.route("/alldata")
def alldata():
    # convert pythonic data to json
    return jsonify(zodiac_data)

# root route
@app.route("/")
def index():
    return render_template("zodiac.html", chinese_zodiac = zodiac_data["zodiac_animals"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
