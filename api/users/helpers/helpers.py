from database import db
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt
)
from models.User import User


class Users:

    @staticmethod
    def new_user(data):
        user = User.query.filter(User.email == data['email']).scalar()
        if user is not None:
            return dict(
                status="invalid",
                message="Email address already registered"
            )

        new_user = User(
            name=data['name'],
            email=data['email'],
            password=User.generate_hash(data['password'])
        )
        db.session.add(new_user)
        db.session.commit()

        return dict(
            status="success",
            message="User successfully registered"
        )

    @staticmethod
    def login(data):
        current_user = User.find_by_email(data['email'])
        if current_user is None:
            return dict(
                status="invalid",
                message="Invalid Credentials!"
            )

        if User.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=current_user.email)
            refresh_token = create_refresh_token(identity=current_user.email)
            return dict(
                status='success',
                access_token=access_token,
                refresh_token=refresh_token
            )

        return dict(
            status="invalid",
            message="Not able validate user credentials!"
        )
