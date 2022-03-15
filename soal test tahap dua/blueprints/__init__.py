from flask import Flask
from functools import wraps
from datetime import timedelta
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import JWTManager
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/mnc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = "super-secret" 
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
app.config['JWT_ACCESS_REFRESH_EXPIRES'] = timedelta(days=30)

jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from blueprints.user_app.model import UserApp
from blueprints.transaction.model import Transaction

from blueprints.user_app.resources import bp_user_app
app.register_blueprint(bp_user_app, url_prefix='/register')

from blueprints.profile import bp_profile
app.register_blueprint(bp_profile, url_prefix='/profile')

from blueprints.login import bp_login
app.register_blueprint(bp_login, url_prefix='/login')

from blueprints.transaction.resources import bp_transaction
app.register_blueprint(bp_transaction, url_prefix='/')



