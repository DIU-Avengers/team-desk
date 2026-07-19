from app.models import db
from datetime import datetime


class User(db.Model):
    """
    PostgreSQL User Table Definition

    Role: Database (Schema Definition Only)
    - Authentication details (password_hash) are handled by auth team
    - User profile data stored here for reference
    - Timestamps for tracking user account lifecycle
    """
    __tablename__ = 'users'

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Core Identity Fields (Unique)
    username = db.Column(db.String(64), index=True,
                         unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)

    # User Profile Information
    first_name = db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), nullable=True)

    # Security (for auth team - password_hash stored here, auth logic handled separately)
    password_hash = db.Column(db.String(255), nullable=False)

    # Account Status
    is_active = db.Column(db.Boolean, default=True, index=True)

    # Timestamps for tracking
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
