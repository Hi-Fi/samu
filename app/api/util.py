from flask import Blueprint

util = Blueprint("util", __name__)

@util.route("/")
def default_page():
    return "Nothing here, POST to <a href=\"/v1/samu\">/v1/samu</a>"

@util.route("/healthz")
def healthz():
    return "OK"
