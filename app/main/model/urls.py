import datetime
from .. import db
from sqlalchemy import Column, DateTime


class ShortenedUrl(db.Model):
    """ ShortenedUrl model for shortened url id and storing original url and ttl """

    __tablename__ = "shortened_url"

    id = db.Column(db.String(length=5), primary_key=True)
    full_url = db.Column(db.Text())
    creation_date = Column(DateTime, default=datetime.datetime.utcnow)
    ttl = Column(DateTime, default=datetime.datetime.utcnow)
