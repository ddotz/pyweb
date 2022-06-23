import os

from flask import Flask
from .extensions import db
from .routes.main import main
from .models import user, book
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/book'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()
    db.init_app(app)
    app.secret_key = 'zhang'
    app.register_blueprint(main)
    db.create_all(app=app)
    return app