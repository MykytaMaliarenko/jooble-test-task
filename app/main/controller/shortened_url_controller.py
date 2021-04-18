from datetime import timedelta

import flask

from app import db
from app.main.service.shortened_url_service import ShortenedUrlService
from app.main.service.redis import RedisService
from flask import redirect
from flask_restful import Resource, reqparse, abort

shortened_url_parser = reqparse.RequestParser(bundle_errors=True)
shortened_url_parser.add_argument(
    'url', type=str, required=True,
    trim=True, help='url to shorten',
)
shortened_url_parser.add_argument(
    'ttl', type=int, dest='raw_ttl',
    help='time to live in seconds',
)


class UrlGeneratorController(Resource):
    def post(self):
        args = shortened_url_parser.parse_args()
        if args.raw_ttl:
            if args.raw_ttl < 0:
                abort(400, message="ttl must be positive int")

            ttl = timedelta(seconds=args.raw_ttl)
            if ttl.days < 1 or ttl.days >= 365:
                abort(400, message="ttl must be from 1 day to 1 year")
        else:
            ttl = timedelta(days=90)

        _id = RedisService.pick_id()
        shorten_url = ShortenedUrlService.create(_id, args.url, ttl)
        db.session.add(shorten_url)
        db.session.commit()

        redirect_url = ShortenedUrlService.generate_redirect_url(shorten_url.id)

        # manually creating response to change content-type from json to text
        response = flask.make_response(redirect_url)
        response.headers['content-type'] = 'text/plain'
        return response


class RedirectController(Resource):
    def get(self, url_id: str):
        shorten_url = ShortenedUrlService.get_by_id(url_id)
        if shorten_url is None:
            abort(404)
        else:
            return redirect(shorten_url.full_url, 301)
