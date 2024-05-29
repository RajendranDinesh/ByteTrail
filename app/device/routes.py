from flask import jsonify

from . import main
from .models import Device

@main.route('/device/all')
def get_all_devices():
    devices = Device.query.all()
    return jsonify([device.to_dict() for device in devices])
