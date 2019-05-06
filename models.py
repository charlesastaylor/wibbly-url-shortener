from app import db


class UrlRule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(128), index=True, nullable=False, unique=True)
    url = db.Column(db.String(2000), nullable=False)

    def __repr__(self):
        return f'<UrlRule {self.key}>'
