from app import db
from . import main
from .models import LogEntry

@main.route('/<endpoint>/<status>', methods=['POST'])
def log(endpoint, status):
    new_log = LogEntry(endpoint=endpoint, status=status)
    db.session.add(new_log)
    db.session.commit()
    return "", 200
