from flask_restx import Api
from flask import Blueprint

api_blueprint = Blueprint('api', __name__, url_prefix="/api/v1")

api = Api(api_blueprint,
          title='UrlShortener',
          version='1.0',
          description='test task for Jooble'
          )
