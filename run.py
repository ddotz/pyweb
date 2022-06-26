from flask import Flask
from extensions import db
from routes.main import main
from routes.book import book
import models.book, models.user

if __name__ =='__main__':
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/book'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(main)
    app.register_blueprint(book, url_prefix='/book')
    app.secret_key = 'zhang'
    db.init_app(app)
    # db.create_all(app=app)
    #from gevent import pywsgi
    # server = pywsgi.WSGIServer(('0.0.0.0',5001),app)
    # server.serve_forever()
    app.run(host='0.0.0.0',port=5000)