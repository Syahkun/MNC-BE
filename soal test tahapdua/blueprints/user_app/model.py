from blueprints import db
from datetime import datetime
from sqlalchemy.sql import func
from flask_restful import fields
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text


class UserApp(db.Model):
    __tablename__ = "user_app"
    user_id = db.Column(db.String(255), primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone_number = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(255))
    pin = db.Column(db.String(255), nullable=False)
    salt = db.Column(db.String(255))
    saldo = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_date = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    transaction = db.relationship('Transaction', backref='user_app', lazy=True)   

    response_fields = {
        'user_id': fields.String,
        'first_name': fields.String,
        'last_name': fields.String,
        'phone_number': fields.String,
        'address': fields.String,
        'updated_date': fields.DateTime
    }

    response_fields_update = {
        'user_id': fields.String,
        'first_name': fields.String,
        'last_name': fields.String,
        'address': fields.String,
        'updated_date': fields.DateTime
    }

    jwt_claims_fields = {
        'user_id': fields.String,
        'phone_number': fields.String,
        'pin': fields.String
    }

    def __init__(self, user_id, first_name, last_name, phone_number, address, pin, salt):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.pin = pin
        self.salt = salt

    def __repr__(self):
        return '<UserApp %r>' % self.user_id