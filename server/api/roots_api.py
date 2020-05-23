from flask import current_app
from flask_restplus import Namespace, Resource, fields

from ..service import roots_service

api = Namespace('roots', description='stringy tendrils')


def recursive_root_model(depth):
    root_json_mapping = {
        'root_id': fields.Integer(),
        'root_sk': fields.Integer(),
        'shoot_id': fields.Integer(),
        'name': fields.String(),
        'type': fields.String(),
        'body': fields.String(),
        'create_dttm': fields.DateTime(),
        'update_dttm': fields.DateTime(),
    }
    if depth:
        root_json_mapping['shoots'] = (fields.List(
            fields.Nested(recursive_root_model(depth - 1))))
    return api.model('root_model' + str(depth), root_json_mapping)


new_root_model = api.model('root_new', {
    'name': fields.String(),
    'type': fields.String(),
    'body': fields.String(),
})

new_shoot_model = api.clone('shoot', new_root_model,
                            {'root_sk': fields.Integer()})


@api.route('/')
class RootList(Resource):
    @api.marshal_with(recursive_root_model(0), skip_none=True)
    def get(self):
        roots = roots_service.get_roots(0)
        return roots, 200

    @api.expect(new_root_model)
    def post(self):
        req = api.payload
        res = roots_service.create_root(req)
        current_app.logger.info(res)
        return 'Success', 200

    @api.expect(recursive_root_model(0))
    def put(self):
        req = api.payload
        res = roots_service.update_root(req)
        current_app.logger.info(res)
        return 'Success', 200


@api.route('/<int:depth>')
class RootDict(Resource):
    @api.marshal_with(recursive_root_model(50), skip_none=True)
    def get(self, depth):
        if depth > 50:
            return 'maximum depth (50) exceeded', 400
        roots = roots_service.get_roots(depth)
        return roots, 200


@api.route('/shoots')
class ShootList(Resource):
    @api.expect(new_shoot_model)
    def post(self):
        req = api.payload
        roots_service.create_shoot(req)
        return 'Success', 200
