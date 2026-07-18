from app.models import db

# giving initial idea here for puja :-

# class User(db.model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)

#     def __repr__(self):
#     return f'<User {self.username}>'