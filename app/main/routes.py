
from flask import render_template
from app.main import main_bp
# from app.models.user import User

@main_bp.route('/')
def index():
    return "Hello from index"
    # return render_template('index.html')
