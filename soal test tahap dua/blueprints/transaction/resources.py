from flask import Flask
from flask import Blueprint

from flask_restful import Api
from flask_restful import reqparse
from flask_restful import Resource
from flask_restful import marshal

from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required

from blueprints.helper import RESULT_SUCCESS
from blueprints.helper import BALANCE_IS_NOT_ENOUGH
from blueprints.helper import SUCCESS
from blueprints.helper import CREDIT
from blueprints.helper import DEBIT
from blueprints.helper import PAYMENT
from blueprints.helper import TRANSFER
from blueprints.helper import TOPUP

from blueprints import app
from blueprints import db

import uuid
import hashlib
import json

from blueprints.transaction.model import Transaction
from blueprints.user_app.model import UserApp

bp_transaction = Blueprint('transaction', __name__)
api = Api(bp_transaction)

class TransactionResource(Resource):
    
    @jwt_required(refresh=True)
    def post(self, transaction_type):
        claims = get_jwt()

        # TOP UP
        if transaction_type == "topup":
            
            parser = reqparse.RequestParser()
            parser.add_argument('amount_top_up', location='json', required=True)

            args = parser.parse_args()

            amount_top_up = int(args['amount_top_up'])
            user_app = UserApp.query.get(claims['user_id'])

            # LOGIC
            balance_before = int(user_app.saldo)
            balance_after = balance_before + amount_top_up
            user_app.saldo = balance_after

            top_up_id = uuid.uuid1()
            data = Transaction(top_up_id, SUCCESS, claims['user_id'], CREDIT, TOPUP, 
            amount_top_up, "", balance_before, balance_after)
            db.session.add(data)
            db.session.commit()

            app.logger.debug(('DEBUG: %s', data))

            mshl_topup = marshal(data, Transaction.response_fields_topup)
            mshl_topup['top_up_id'] = mshl_topup.pop('transaction_id')
            mshl_topup['amount_top_up'] = mshl_topup.pop('amount')
            mshl_topup['balance_before'] = mshl_topup.pop('balance_before')
            mshl_topup['balance_after'] = mshl_topup.pop('balance_after')
            mshl_topup['created_date'] = mshl_topup.pop('created_date')
            RESULT_SUCCESS['result'] = mshl_topup

            return RESULT_SUCCESS, 200

        # PAYMENT
        if transaction_type == "payment":
            parser = reqparse.RequestParser()
            parser.add_argument('amount', location='json', required=True)
            parser.add_argument('remarks', location='json')

            args = parser.parse_args()

            amount = int(args['amount'])
            user_app = UserApp.query.get(claims['user_id'])
            
            balance_before = int(user_app.saldo)
            if amount > balance_before:
                return BALANCE_IS_NOT_ENOUGH, 400

            # LOGIC
            balance_after = balance_before - amount
            user_app.saldo = balance_after

            top_up_id = uuid.uuid1()
            data = Transaction(top_up_id, SUCCESS, claims['user_id'], DEBIT, PAYMENT, amount, 
            args['remarks'], balance_before, balance_after)
            db.session.add(data)
            db.session.commit()

            app.logger.debug(('DEBUG: %s', data))

            mshl_payment = marshal(data, Transaction.response_fields_payment_transfer)
            mshl_payment['payment_id'] = mshl_payment.pop('transaction_id')
            mshl_payment['amount'] = mshl_payment.pop('amount')
            mshl_payment['remarks'] = mshl_payment.pop('remarks')
            mshl_payment['balance_before'] = mshl_payment.pop('balance_before')
            mshl_payment['balance_after'] = mshl_payment.pop('balance_after')
            mshl_payment['created_date'] = mshl_payment.pop('created_date')
            RESULT_SUCCESS['result'] = mshl_payment

            return RESULT_SUCCESS, 200

        # TRANSFER
        if transaction_type == "transfer":
            parser = reqparse.RequestParser()
            parser.add_argument('target_user', location='json', required=True)
            parser.add_argument('amount', location='json', required=True)
            parser.add_argument('remarks', location='json')

            args = parser.parse_args()

            target_user = args['target_user']
            amount = int(args['amount'])
            user_app = UserApp.query.get(claims['user_id'])
            target_user = UserApp.query.get(target_user)
            
            balance_before = int(user_app.saldo)
            if amount > balance_before:
                return BALANCE_IS_NOT_ENOUGH, 400

            # LOGIC
            balance_after = balance_before - amount
            user_app.saldo = balance_after
            target_user.saldo += amount

            top_up_id = uuid.uuid1()
            data = Transaction(top_up_id, SUCCESS, claims['user_id'], DEBIT, TRANSFER, amount, 
            args['remarks'], balance_before, balance_after)
            db.session.add(data)
            db.session.commit()

            app.logger.debug(('DEBUG: %s', data))

            mshl_payment = marshal(data, Transaction.response_fields_payment_transfer)
            mshl_payment['transfer_id'] = mshl_payment.pop('transaction_id')
            mshl_payment['amount'] = mshl_payment.pop('amount')
            mshl_payment['remarks'] = mshl_payment.pop('remarks')
            mshl_payment['balance_before'] = mshl_payment.pop('balance_before')
            mshl_payment['balance_after'] = mshl_payment.pop('balance_after')
            mshl_payment['created_date'] = mshl_payment.pop('created_date')
            RESULT_SUCCESS['result'] = mshl_payment

            return RESULT_SUCCESS, 200

    @jwt_required(refresh=True)
    def get(self, transaction_type):
        if transaction_type == "transactions":
            claims = get_jwt()

            transactions = Transaction.query.filter_by(user_id=claims['user_id']).all()
            rows = []

            for transaction in transactions:
                mshl_transaction = marshal(transaction, Transaction.response_fields_transactions)
                if transaction.transaction_method == TRANSFER:
                    mshl_transaction['transfer_id'] = mshl_transaction.pop('transaction_id')
                elif transaction.transaction_method == PAYMENT:
                    mshl_transaction['payment_id'] = mshl_transaction.pop('transaction_id')
                elif transaction.transaction_method == TOPUP:
                    mshl_transaction['top_up_id'] = mshl_transaction.pop('transaction_id')

                mshl_transaction['status'] = mshl_transaction.pop('status')
                mshl_transaction['user_id'] = mshl_transaction.pop('user_id')
                mshl_transaction['transaction_type'] = mshl_transaction.pop('transaction_type')
                mshl_transaction['amount'] = mshl_transaction.pop('amount')
                mshl_transaction['remarks'] = mshl_transaction.pop('remarks')
                mshl_transaction['balance_before'] = mshl_transaction.pop('balance_before')
                mshl_transaction['balance_after'] = mshl_transaction.pop('balance_after')
                mshl_transaction['created_date'] = mshl_transaction.pop('created_date')
                rows.append(mshl_transaction)
            
            RESULT_SUCCESS['result'] = rows
            return RESULT_SUCCESS, 200

api.add_resource(TransactionResource, '', '<transaction_type>')