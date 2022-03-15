from flask_restful import Resource, Api
from blueprints import app
from logging.handlers import RotatingFileHandler
import logging
import sys


# You may want your app to return an error message with the correct media type on 404 Not Found errors; 
# in which case, use the catch_all_404s parameter of the Api constructor
api = Api(app, catch_all_404s=True)

if __name__ == '__main__':
        
    app.run(debug=True)