from flask import request

from app import db
from . import main
from .models import LogEntry, Device

@main.route('/', methods=['POST'])
def log():
    try:
        data = request.get_json()
    except:
        return "", 200
    
    fields = ['log', 'device_id']
    for field in fields:
        if field not in data:
            return "", 200

    device_id = data['device_id']

    device = Device.query.filter_by(id=device_id).first()

    if device is None:
        device = Device(id=device_id)

    new_log = LogEntry(log=data["log"], device_id=device_id)
    db.session.add(new_log)

    device.last_uplink = db.func.now()

    db.session.add(device)

    db.session.commit()

    return "", 200
