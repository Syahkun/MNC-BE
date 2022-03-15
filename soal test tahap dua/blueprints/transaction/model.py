from blueprints import db
from datetime import datetime
from sqlalchemy.sql import func
from flask_restful import fields
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text


class Transaction(db.Model):
    __tablename__ = "transaction"
    transaction_id = db.Column(db.String(100), primary_key=True)
    status = db.Column(db.String(50))
    user_id = db.Column(db.String(100), db.ForeignKey('user_app.user_id'), nullable=False)
    transaction_type = db.Column(db.String(50))
    transaction_method = db.Column(db.String(50))
    amount = db.Column(db.Integer, nullable=False)
    remarks = db.Column(db.String(100))
    balance_before = db.Column(db.Integer, default=0)
    balance_after = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())

    response_fields_topup = {
        'transaction_id': fields.String,
        'amount': fields.Integer,
        'balance_before': fields.Integer,
        'balance_after': fields.Integer,
        'created_date': fields.DateTime
    }

    response_fields_payment_transfer = {
        'transaction_id': fields.String,
        'amount': fields.Integer,
        'remarks': fields.String,
        'balance_before': fields.Integer,
        'balance_after': fields.Integer,
        'created_date': fields.DateTime
    }

    response_fields_transactions = {
        'transaction_id': fields.String,
        'status': fields.String,
        'user_id': fields.String,
        'transaction_type': fields.String,
        'amount': fields.Integer,
        'remarks': fields.String,
        'balance_before': fields.Integer,
        'balance_after': fields.Integer,
        'created_date': fields.DateTime
    }

    def __init__(self, transaction_id, status, user_id, transaction_type, transaction_method, amount, remarks, balance_before, balance_after):
        self.transaction_id = transaction_id
        self.status = status
        self.user_id = user_id
        self.transaction_type = transaction_type
        self.transaction_method = transaction_method
        self.amount = amount
        self.remarks = remarks
        self.balance_before = balance_before
        self.balance_after = balance_after

    def __repr__(self):
        return '<Transaction %r>' % self.id