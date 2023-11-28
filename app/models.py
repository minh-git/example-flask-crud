from app import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    url = db.Column(db.String(120), index=True, nullable=False)
    last_updated_string = db.Column(db.String(10000), nullable=True)
    status = db.Column(db.Boolean, default=False)