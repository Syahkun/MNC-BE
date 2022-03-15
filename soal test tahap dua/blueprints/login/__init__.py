from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
from flask import request

from flask_restful import Api
from flask_restful import Resource
from flask_restful import reqparse
from flask_restful import marshal

from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import get_jwt

import hashlib
import json
import uuid
import os

from ..user_app.model import UserApp

bp_login = Blueprint('login', __name__)
api = Api(bp_login)

class CreateTokenResource(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('phone_number', location='json', required=True)
        parser.add_argument('pin', location='json', required=True)
        args = parser.parse_args()

        query = UserApp.query.filter_by(phone_number=args['phone_number']).first()

        if query is not None:
            salt = query.salt
            encoded = ('%s%s' %(args['pin'], salt)).encode('utf-8')
            hash_pass = hashlib.sha512(encoded).hexdigest()
            if hash_pass == query.pin and query.phone_number == args['phone_number']:
                additional_claims = marshal(query, UserApp.jwt_claims_fields)
                access_token = create_access_token(
                    identity=args['phone_number'],  additional_claims=additional_claims
                )
                refresh_token = create_refresh_token(
                    identity=args['phone_number'],  additional_claims=additional_claims
                )
                return {'access_token': access_token, 'refresh_token': refresh_token}, 200
        return {'message': 'Phone number and pin doesn’t match'}, 401

api.add_resource(CreateTokenResource, '')