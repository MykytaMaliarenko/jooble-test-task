from app import db
from sqlalchemy import Column


class ShortenedUrl(db.Model):
    """ ShortenedUrl model for storing original url and ttl """

    __tablename__ = "shortened_url"

    id = db.Column(db.String(length=5), primary_key=True)
    full_url = db.Column(db.String)
    creation_date = Column(db.DateTime, server_default="DEFAULT")
    ttl = Column(db.Interval, server_default="DEFAULT")
