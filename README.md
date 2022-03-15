# MNC-BE

requirements:
# Python 
# Flask
# Mysql

How to run apps

1. activate virtual env in folder venv with command => source venv/Scripts/Activate
    for more detail you can open https://flask.palletsprojects.com/en/2.0.x/installation/#virtual-environments

2. Create your database in MYSQL with command => create database mnc; 

3. Set your database in folder blueprints file __init__.py
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/mnc'

    database = mysql
    driver = pymsql
    username = root
    password = root
    port = 3306
    database name = mnc

4. Migrate your database with commands 
    => flask db init
    => flask db migrate -m "initial"
    => flask upgrade
    for more informations you can open https://flask-migrate.readthedocs.io/en/latest/

5. Run your Flask Apps in the root folder soal test tahap dua
    => export FLASK_APP=app.py
    => export FLASK_ENV=development
    => flask run 
    for more informations you can open https://flask.palletsprojects.com/en/2.0.x/quickstart/


