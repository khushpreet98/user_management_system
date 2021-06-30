from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List
from .schema import UserSchema
from .service import UserService
from .model import User
from flask import jsonify
from datetime import datetime

api = Namespace("User")

@api.route("/")
class UserResource(Resource):
    @accepts(schema=UserSchema, api=api)
    @responds(schema=UserSchema, status_code=201)
    def post(self) -> User:
        obj = request.parsed_obj
        obj['created_at'] = datetime.utcnow()
        obj["full_name"] = obj["first_name"] + " " + obj["last_name"]
        resp = Response(status=201)
        min_length = int(request.headers['Min-Length'])
        if len(obj["first_name"]) < min_length:
            return Response(f"message:first name should not be less {min_length}  characters", status=400)
        db_user = UserService.create(obj)
        resp.headers['id'] = db_user.id
        return resp

    @responds(schema=UserSchema, many=True)
    def get(self) -> List[User]:
        args = request.args
        filters = list()
        if "first_name" in args:
            filters.append({'model': 'User', 'field': 'first_name', 'op': '==', 'value': args["first_name"]})
        if "last_name" in args:
            filters.append({'model': 'User', 'field': 'last_name', 'op': '==', 'value': args["last_name"]})
        return UserService.get_all(filters)

@api.route("/<int:id>")
@api.param("id")
class UserIdResource(Resource):
    @responds(schema=UserSchema)
    def get(self, id: int) -> User:
        id = UserService.get_by_id(id)
        if id:
            return id
        else:
            return Response(status=404, response="Id not exists")

    def delete(self, id: int) -> Response:
        """Delete Single User"""
        id = UserService.delete_by_id(id)
        if id:
            return jsonify(dict(status="success", id=id))
        else:
            return "error:Id not found", 404
