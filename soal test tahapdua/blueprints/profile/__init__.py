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

bp_profile = Blueprint('profile', __name__)
api = Api(bp_profile)

class ProfileResource(Resource):

    @jwt_required(refresh=True)
    def put(self):
        claims = get_jwt()
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', location='json')
        parser.add_argument('last_name', location='json')
        parser.add_argument('address', location='json')

        args = parser.parse_args()

        query = UserApp.query.get(claims['user_id'])
        if query is None:
            return {'Status ': 'Not Found'}, 404

        if args['first_name'] is not None:
            query.first_name = args['first_name']
        if args['last_name'] is not None:
            query.last_name = args['last_name']
        if args['address'] is not None:
            query.address = args['address']
        db.session.commit()

        RESULT_SUCCESS['result'] = marshal(query, UserApp.response_fields_update)

        return RESULT_SUCCESS['result'], 200

api.add_resource(ProfileResource, '', '')
