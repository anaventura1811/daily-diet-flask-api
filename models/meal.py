from database import db


class Meal(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(400), unique=False)
    date = db.Column(db.String(50), unique=False, nullable=False),
    last_updated = db.Column(
        db.DateTime, unique=False,
        server_default=db.text(
            "CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    in_diet = db.Column(db.Boolean, unique=False, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
