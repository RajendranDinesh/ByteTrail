from . import main

@main.route('/')
def index():
    return "Hello, Main!"

@main.route('/health')
def health_check():
    return "", 200
