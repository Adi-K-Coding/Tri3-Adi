# import "packages" from flask

from flask import render_template, request
from __init__ import app
import requests




# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True, port=8081)
