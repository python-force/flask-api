from flask import jsonify, Blueprint

from flask_restful import Resource, Api, reqparse, fields, marshal, marshal_with

import models

todo_fields = {
    'id': fields.Integer,
    'title': fields.String
}

class TodoList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'id',
            required=True,
            help='No ID provided.',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'title',
            required=True,
            help='No Todo Title Provided.',
            location=['form', 'json']
        )
        super().__init__()

    def get(self):
        todos = [marshal(todo, todo_fields) for todo in models.Todo.select()]
        return {'todos':todos}

    def post(self):
        args = self.reqparse.parse_args()
        models.Todo.create(**args)
        return jsonify({'todos':[{'title': 'Big Task!'}]})


class Todo(Resource):
    def get(self, id):
        return jsonify({'todo':[{'title': 'Big Task!'}]})

todos_api = Blueprint('resources.todos', __name__)
api = Api(todos_api)
api.add_resource(
    TodoList,
    '/api/v1/todos',
    endpoint='todos'
)
api.add_resource(
    Todo,
    '/api/v1/todos/<int:id>',
    endpoint='todo'
)