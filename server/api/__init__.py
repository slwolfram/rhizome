from flask import Blueprint
from flask_restplus import Api

from .post_api import api as post_api

api = Blueprint('api', __name__)
_api = Api(api, title='', description='')

_api.add_namespace(post_api)
