from flask_restful import Api
from flask import Blueprint
from .controller.shortened_url_controller import \
    UrlGeneratorController, RedirectController

api_blueprint = Blueprint('api', __name__)

api = Api(api_blueprint)
api.add_resource(UrlGeneratorController, '/generate')
api.add_resource(RedirectController, '/<string:url_id>', endpoint="redirect")
