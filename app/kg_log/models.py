from app import db

class LogEntry(db.Model):
    __tablename__ = 'kg_log'

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(255), nullable=False)
    log = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

class Device(db.Model):
    __tablename__ = 'device'

    id = db.Column(db.String(255), primary_key=True)
    last_uplink = db.Column(db.DateTime)
    added_on = db.Column(db.DateTime, server_default=db.func.now())
