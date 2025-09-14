from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db=SQLAlchemy()

def create_app():
    app=Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "my-secret-key")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI", "sqlite:///todo.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", "False")
    
    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app





