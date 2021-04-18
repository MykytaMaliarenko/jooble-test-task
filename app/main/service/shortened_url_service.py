from datetime import timedelta
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
