from app import db

class Device(db.Model):
    __tablename__ = 'device'

    id = db.Column(db.String(255), primary_key=True)
    last_uplink = db.Column(db.DateTime)
    added_on = db.Column(db.DateTime, server_default=db.func.now())
