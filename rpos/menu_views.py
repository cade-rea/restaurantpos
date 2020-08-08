from flask import Blueprint

menuBP = Blueprint('menuBP', __name__, url_prefix='/menu')


@menuBP.route('/')
def hello():
    return 'Hello, World!'