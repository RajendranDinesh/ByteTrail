from flask import request

from app import db
from . import main
from .models import LogEntry
from ..device.models import Device

@main.route('/', methods=['POST', 'GET'])
def log():
    if request.method == 'GET':
        decrpt()
        return "", 200

    try:
        data = request.get_json()
    except:
        return "You sure that's JSON?", 400
    
    fields = ['log', 'device_id']
    for field in fields:
        if field not in data:
            return f"You're missing something buddy...", 400

    device_id = data['device_id']

    device = Device.query.filter_by(id=device_id).first()

    if device is None:
        device = Device(id=device_id)

    new_log = LogEntry(log=data["log"], device_id=device_id)
    db.session.add(new_log)

    device.last_uplink = db.func.now()

    db.session.add(device)

    db.session.commit()

    return f"Log intercepted at {db.func.now()}", 200

def decrpt():
    import base64

    def decrypt_string(encrypted_data):
        encrypted_data = base64.b64decode(encrypted_data)
        return encrypted_data

    encrypted_data = """T1M6IHR5cGU6IFdpbmRvd3MKVmVyc2lvbjogMTAuMC4yMjYzMQoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFswNy0yOS0wOV0gfENvZGUuZXhlfHxtYWluLnJzIC0ga2lsbGdyYXZlIC0gUnVzdERldiAtIFZpc3VhbCBTdHVkaW8gQ29kZXwgIChMRUZUX01PVVNFX0JVVFRPTikKWzA3LTI5LTEwXSB8Q29kZS5leGV8fGtleWNhcC5sb2cgKFVudHJhY2tlZCkgKGtleWNhcC5sb2cpIC0ga2lsbGdyYXZlIC0gUnVzdERldiAtIFZpc3VhbCBTdHVkaW8gQ29kZXwgIChMRUZUX01PVVNFX0JVVFRPTikKWzA3LTI5LTExXSB8Q29kZS5leGV8fGtleWNhcC5sb2cgKFVudHJhY2tlZCkgKGtleWNhcC5sb2cpIC0ga2lsbGdyYXZlIC0gUnVzdERldiAtIFZpc3VhbCBTdHVkaW8gQ29kZXwgIChMRUZUX01PVVNFX0JVVFRPTikKWzA3LTI5LTE1XSB8Q29kZS5leGV8fGtleWNhcC5sb2cgKFVudHJhY2tlZCkgKGtleWNhcC5sb2cpIC0ga2lsbGdyYXZlIC0gUnVzdERldiAtIFZpc3VhbCBTdHVkaW8gQ29kZXwgIChMRUZUX01PVVNFX0JVVFRPTikKWzA3LTI5LTE1XSB8Q29kZS5leGV8fG1haW4ucnMgLSBraWxsZ3JhdmUgLSBSdXN0RGV2IC0gVmlzdWFsIFN0dWRpbyBDb2RlfCAgKExFRlRfTU9VU0VfQlVUVE9OKQpbMDctMjktMTZdIHxDb2RlLmV4ZXx8bWFpbi5ycyAtIGtpbGxncmF2ZSAtIFJ1c3REZXYgLSBWaXN1YWwgU3R1ZGlvIENvZGV8ICAoTEVGVF9NT1VTRV9CVVRUT04pClswNy0yOS0xOV0gfENvZGUuZXhlfHxtYWluLnJzIC0ga2lsbGdyYXZlIC0gUnVzdERldiAtIFZpc3VhbCBTdHVkaW8gQ29kZXwgIChMRUZUX01PVVNFX0JVVFRPTikKWzA3LTI5LTIwXSB8Q29kZS5leGV8fG1haW4ucnMgLSBraWxsZ3JhdmUgLSBSdXN0RGV2IC0gVmlzdWFsIFN0dWRpbyBDb2RlfCAgKExFRlRfTU9VU0VfQlVUVE9OKQpbMDctMjktMjBdIHxDb2RlLmV4ZXx8bWFpbi5ycyAtIGtpbGxncmF2ZSAtIFJ1c3REZXYgLSBWaXN1YWwgU3R1ZGlvIENvZGV8ICAoMSkKWzA3LTI5LTIxXSB8Q29kZS5leGV8fOKXjyBtYWluLnJzIC0ga2lsbGdyYXZlIC0gUnVzdERldiAtIFZpc3VhbCBTdHVkaW8gQ29kZXwgIChVTktOT1dOX0tFWV8xNykKWzA3LTI5LTIxXSB8Q29kZS5leGV8fOKXjyBtYWluLnJzIC0ga2lsbGdyYXZlIC0gUnVzdERldiAtIFZpc3VhbCBTdHVkaW8gQ29kZXwgIChMRUZUX0NPTlRST0xfS0VZKQpbMDctMjktMjFdIHxDb2RlLmV4ZXx84pePIG1haW4ucnMgLSBraWxsZ3JhdmUgLSBSdXN0RGV2IC0gVmlzdWFsIFN0dWRpbyBDb2RlfCAgKHMpClswNy0yOS0yMl0gfENvZGUuZXhlfHxtYWluLnJzIC0ga2lsbGdyYXZlIC0gUnVzdERldiAtIFZpc3VhbCBTdHVkaW8gQ29kZXwgIChVTktOT1dOX0tFWV8xNykKWzA3LTI5LTIyXSB8Q29kZS5leGV8fG1haW4ucnMgLSBraWxsZ3JhdmUgLSBSdXN0RGV2IC0gVmlzdWFsIFN0dWRpbyBDb2RlfCAgKExFRlRfQ09OVFJPTF9LRVkpClswNy0yOS0yMl0gfENvZGUuZXhlfHxtYWluLnJzIC0ga2lsbGdyYXZlIC0gUnVzdERldiAtIFZpc3VhbCBTdHVkaW8gQ29kZXwgIChPRU1fM19LRVkpClswNy0yOS0yMl0gfENvZGUuZXhlfHxtYWluLnJzIC0ga2lsbGdyYXZlIC0gUnVzdERldiAtIFZpc3VhbCBTdHVkaW8gQ29kZXwgIChVTktOT1dOX0tFWV8xNykKWzA3LTI5LTIyXSB8Q29kZS5leGV8fG1haW4ucnMgLSBraWxsZ3JhdmUgLSBSdXN0RGV2IC0gVmlzdWFsIFN0dWRpbyBDb2RlfCAgKExFRlRfQ09OVFJPTF9LRVkpCg=="""

    decrypted_data = decrypt_string(encrypted_data)
    print(f"{decrypted_data.decode()}")