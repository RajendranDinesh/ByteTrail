from flask import Blueprint

main = Blueprint('cron_log', __name__)

from . import routes
