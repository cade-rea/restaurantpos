from flask import Blueprint
from rpos.db import query_db

menuBP = Blueprint('menuBP', __name__, url_prefix='/menu')


@menuBP.route('/')
def hello():
    items = [item['name'] for item in query_db('SELECT * FROM items')]
    return str(items)