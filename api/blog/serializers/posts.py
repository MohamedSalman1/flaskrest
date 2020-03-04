from flask_restplus import fields
from api.restplus import api
from api.serializers import pagination

blog_post = api.model('Blog post', {
    'id': fields.Integer(
        readOnly=True,
        description='The unique identifier of a blog post'
    ),
    'title': fields.String(required=True, description='Article title'),
    'body': fields.String(required=True, description='Article content'),
    'pub_date': fields.DateTime,
    'category_id': fields.Integer(attribute='category.id'),
    'category': fields.String(attribute='category.name'),
})

page_of_blog_posts = api.inherit('Page of blog posts', pagination, {
    'items': fields.List(fields.Nested(blog_post))
})
