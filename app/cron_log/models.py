from app import db

class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    endpoint = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
