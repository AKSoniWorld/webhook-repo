from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from read_config import DATABASE_URI


# handler = logging.FileHandler(ERROR_LOG_PATH)
# handler.setLevel(logging.INFO)

app = Flask(__name__)  # , template_folder='../templates'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
# app.logger.addHandler(handler)
db = SQLAlchemy(app)

from API.View import mobile_api, web_api
