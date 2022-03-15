from flask import Flask
from flask import Blueprint

from flask_restful import Api
from flask_restful import reqparse
from flask_restful import Resource
from flask_restful import marshal

from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required

from blueprints.helper import RESULT_SUCCESS

from blueprints import app
from blueprints import db

import uuid
import hashlib
import json

from blueprints.user_app.model import UserApp

bp_user_app = Blueprint('user_app', __name__)
api = Api(bp_user_app)

class UserAppResource(Resource):
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', location='json')
        parser.add_argument('last_name', location='json')
        parser.add_argument('phone_number', location='json', required=True)
        parser.add_argument('address', location='json')
        parser.add_argument('pin', location='json')

        args = parser.parse_args()
            
        user = UserApp.query.filter_by(phone_number=args["phone_number"]).first()
        if user:
            return { "message": "Phone Number already registered" }

        salt = uuid.uuid4().hex
        encoded = ('%s%s' % (args['pin'], salt)).encode('utf-8')
        hash_pin = hashlib.sha512(encoded).hexdigest()
            
        user_id = uuid.uuid1()
        data = UserApp(user_id, args['first_name'], args['last_name'], 
        args['phone_number'], args['address'], hash_pin, salt)
        db.session.add(data)
        db.session.commit()

        app.logger.debug(('DEBUG: %s', data))

        RESULT_SUCCESS['result'] = marshal(data, UserApp.response_fields)
        return RESULT_SUCCESS, 200

api.add_resource(UserAppResource, '', '')