import logging

from flask import request
from flask_restplus import Resource
from api.users.serializers.auth import login_post, register_post
from api.users.helpers.helpers import Users

from api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace(
    'auth',
    description='Operations related to users authentication'
)


@ns.route('/login')
class LoginCollection(Resource):

    @api.expect(login_post)
    def post(self):
        """
        Login user via jwt access token.
        """
        response = Users.login(request.json)
        return response, 201


@ns.route('/register')
class RegisterCollection(Resource):

    @api.expect(register_post)
    def post(self):
        """
        Register new user in application
        """
        response = Users.new_user(request.json)
        return response, 201
