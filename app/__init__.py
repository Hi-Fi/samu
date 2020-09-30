from flask import Flask
from app.api.v1 import v1
from app.api.util import util

app = Flask(__name__)
app.register_blueprint(v1, url_prefix="/v1")
app.register_blueprint(util)
