from app import db

class LogEntry(db.Model):
    __tablename__ = 'cron_log'
    
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(255), db.ForeignKey('device.id'), nullable=False)
    endpoint = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'device_id': self.device_id,
            'endpoint': self.endpoint,
            'status': self.status,
            'timestamp': self.timestamp
        }
