from flask import request

from app import db
from . import main
from .models import LogEntry
from ..device.models import Device

@main.route('/', methods=['POST', 'GET'])
def log():
    if request.method == 'GET':
        logs = LogEntry.query.all()

        return f"{[log.to_dict() for log in logs]}", 200
    
    data = request.get_json()

    device_id = data.get('device')
    if not device_id:
        return "Missing device", 400
    
    endpoint = data.get('endpoint')
    if not endpoint:
        return "Missing endpoint", 400
    
    status = data.get('status')
    if not status:
        return "Missing status", 400
    
    try:
        device = Device.query.filter_by(id=device_id).first()

        if device is None:
            return "Device not found", 400
        
    except:
        return "Device not found", 400
    
    try:
        new_log = LogEntry(endpoint=endpoint, status=status, device_id=device_id)

        device.last_uplink = db.func.now()

        db.session.add(device)
        db.session.add(new_log)
        
        db.session.commit()

    except:
        return "Log entry failed", 500
    
    return "", 200
