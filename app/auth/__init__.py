
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

# avoiding circular dependencies
from app.auth import routes