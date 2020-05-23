from flask import current_app
from flask_restplus import Namespace, Resource, fields

from ..service import post_service

api = Namespace('posts', description='')


def post_model(iteration_number=10, **kwargs):
    json_mapping = {
        'name': fields.String(required=True),
        'type': fields.String(required=True),
        'body': fields.String(required=True),
        'filepath': fields.String(required=True)
    }
    if 'has_dates' in kwargs:
        json_mapping.update({
            'create_dttm': fields.DateTime(required=True),
            'update_dttm': fields.DateTime(required=True)
        })
    if 'has_id' in kwargs:
        json_mapping['post_id'] = fields.Integer(required=True)
    if iteration_number:
        json_mapping['children'] = fields.List(
            fields.Nested(post_model(iteration_number - 1)))
    return api.model('Person' + str(iteration_number), json_mapping)


@api.route('/')
class PostList(Resource):
    @api.marshal_with(post_model(0, has_dates=True, has_id=True),
                      skip_none=True)
    def get(self):
        roots = post_service.get_roots(0)
        return roots, 200

    @api.expect(post_model(0))
    def post(self):
        req = api.payload

        res = post_service.create_post(req)
        current_app.logger.info(res)
        return 'Success', 200

    @api.expect(post_model(0))
    def put(self, has_id=True):
        req = api.payload
        res = post_service.update_post(req)
        current_app.logger.info(res)
        return 'Success', 200


@api.route('/depth=<int:depth>/')
class RootList(Resource):
    @api.marshal_with(post_model(10, has_dates=True, has_id=True),
                      skip_none=True)
    def get(self, depth):
        if depth > 10:
            depth = 10
        roots = post_service.get_roots(depth)
        return roots, 200


@api.route('/post_id=<int:post_id>/depth=<int:depth>/')
class Post(Resource):
    @api.marshal_with(post_model(10, has_dates=True, has_id=True),
                      skip_none=True)
    def get(self, post_id, depth):
        if depth > 10:
            depth = 10
        post = post_service.get_post(post_id, depth)
        return list(post), 200
