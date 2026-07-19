from flask import Blueprint

main_bp = Blueprint('main', __name__)

# Importing routes here to avoid circular dependencies

from app.main import routes