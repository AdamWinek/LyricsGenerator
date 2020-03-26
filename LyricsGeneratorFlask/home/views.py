
from flask import Blueprint, jsonify, make_response, render_template

from home.modelLoader import getJsonFile

home_view = Blueprint('home_view',__name__)
@home_view.route('/')  # Route for the page
def display_home_page():
	return render_template('index.html', num=10)

@home_view.route('/generate') #route for lyrics generation
def generate():	
	jsonText = getJsonFile()
	print(jsonText)
	jsonFile = jsonify(
        lyrics=jsonText
    )
	return make_response(jsonFile,200)
