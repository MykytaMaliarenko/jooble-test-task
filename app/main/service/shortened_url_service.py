import string, random
from datetime import timedelta
from urllib.parse import urlparse, urlunparse

from app import db
from flask import url_for

from app.main.model.shortened_url import ShortenedUrl


class ShortenedUrlService:
    ID_VALUES = string.digits + string.ascii_letters

    @staticmethod
    def create(_id: str, url: str, ttl: timedelta) -> ShortenedUrl:
        return ShortenedUrl(id=_id, full_url=url, ttl=ttl)

    @staticmethod
    def generate_id(length: int) -> str:
        return "".join([random.choice(ShortenedUrlService.ID_VALUES) for _ in range(length)])

    @staticmethod
    def generate_unique_id(length: int) -> str:
        while True:
            _id = ShortenedUrlService.generate_id(length)
            if not ShortenedUrlService.has_id(_id):
                break
        return _id

    @staticmethod
    def has_id(_id: str) -> bool:
        return ShortenedUrl.query.filter_by(id=_id).first() is not None

    @staticmethod
    def get_by_id(_id: str) -> ShortenedUrl:
        return ShortenedUrl.query.filter_by(id=_id).first()

    @staticmethod
    def delete_old_records():
        db.engine.execute("delete from shortened_url where creation_date + ttl < now();")

    @staticmethod
    def generate_redirect_url(_id: str, endpoint_name="api.redirect", scheme="http") -> str:
        o = urlparse(url_for(endpoint_name, _external=True, url_id=_id))
        return urlunparse((scheme, o.netloc, o.path, "", "", ""))

