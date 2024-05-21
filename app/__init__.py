from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('app.config.Config')

    db.init_app(app)    
    
    # Register blueprints
    from .main import main as main_blueprint
    from .cron_log import main as cron_log_blueprint
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(cron_log_blueprint)
    
    return app
