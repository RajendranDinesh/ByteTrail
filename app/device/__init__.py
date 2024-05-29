from flask import Blueprint

main = Blueprint('kg_log', __name__)

from . import routes
