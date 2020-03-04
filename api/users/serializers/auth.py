from flask_restplus import fields
from api.restplus import api

login_post = api.model('User Login', {
    'email': fields.String(required=True, description='Login email address'),
    'password': fields.String(required=True, description='Login password')
})

register_post = api.model('Registration', {
    'name': fields.String(required=True, description='User full name'),
    'email': fields.String(required=True, description='Login email address'),
    'password': fields.String(required=True, description='Login password')
})
