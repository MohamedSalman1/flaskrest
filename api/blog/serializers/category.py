from flask_restplus import fields
from api.restplus import api
from api.blog.serializers.posts import blog_post

category = api.model('Blog category', {
    'id': fields.Integer(
        readOnly=True, description='The unique identifier of a blog category'
    ),
    'name': fields.String(required=True, description='Category name'),
})

category_with_posts = api.inherit('Blog category with posts', category, {
    'posts': fields.List(fields.Nested(blog_post))
})
