from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'b5088b36e65e4133acc6133996837e2b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://iptrackdb:FUAnBGaAMf6kD7WB@localhost/iptrack'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from iptrack import routes
