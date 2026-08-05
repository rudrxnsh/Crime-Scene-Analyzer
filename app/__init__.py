from flask import Flask
from flask_cors import CORS

from app.config import DEBUG, SECRET_KEY
from app.utils.logging_config import setup_logging

from app.api.health import health_bp
from app.api.upload import upload_bp

def create_app():
    """
        Application Factory
        Creates and configures the Flask application.
    """
    
    app = Flask(__name__)
    
    # -----------------------------
    # Load Configuration
    # -----------------------------
    app.config["DEBUG"] = DEBUG
    app.config["SECRET_KEY"] = SECRET_KEY
    
    
    # Enable CORS
    CORS(app)
    
    # Initialize Logging
    setup_logging()
    
    # -----------------------------
    # Register Blueprints
    # -----------------------------
    app.register_blueprint(health_bp)
    app.register_blueprint(upload_bp)

    return app
    
    
    
    