from datetime import timedelta
from urllib.parse import urlparse, urlunparse

from flask import url_for

from app.main.model.shortened_url import ShortenedUrl


class ShortenedUrlService:

    @staticmethod
    def create(_id: str, url: str, ttl: timedelta) -> ShortenedUrl:
        return ShortenedUrl(id=_id, full_url=url, ttl=ttl)

    @staticmethod
    def has_id(_id: str) -> bool:
        return ShortenedUrl.query.filter_by(id=_id).exists()

    @staticmethod
    def get_by_id(_id: str) -> ShortenedUrl:
        return ShortenedUrl.query.filter_by(id=_id).first()

    @staticmethod
    def generate_redirect_url(_id: str, endpoint_name="api.redirect", scheme="http") -> str:
        o = urlparse(url_for(endpoint_name, _external=True, url_id=_id))
        return urlunparse((scheme, o.netloc, o.path, "", "", ""))

