from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)
Base = declarative_base()
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

from app import routes, models
