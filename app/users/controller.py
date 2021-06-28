from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List
from .schema import user_schema
from .service import user_service
from .model import User
from flask import jsonify
from datetime import datetime

api = Namespace("User")


@api.route("/")
class user_resource(Resource):
    @accepts(schema=user_schema, api=api)
    @responds(schema=user_schema, status_code=201)
    def post(self) -> User:
        obj = request.parsed_obj
        obj['created_at'] = datetime.utcnow()
        obj["full_name"] = obj["first_name"] + " " + obj["last_name"]
        resp = Response(status=201)
        min_length = int(request.headers['Min-Length'])
        print(f"min length{min_length}")
        if len(obj["first_name"]) < min_length:
            return Response(f"message: first name should not be less {min_length}  characters", status=400)
        user1 = user_service.create(obj)
        resp.headers['id'] = user1.id
        return resp

    @responds(schema=user_schema, many=True)
    def get(self) -> List[User]:
        args = request.args
        filters = list()
        if "first_name" in args:
            filters.append({'model': 'User', 'field': 'first_name', 'op': '==', 'value': args["first_name"]})
        if "last_name" in args:
            filters.append({'model': 'User', 'field': 'last_name', 'op': '==', 'value': args["last_name"]})
        return user_service.get_all(filters)




@api.route("/<int:id>")
@api.param("id")
class user_id_resource(Resource):
    @responds(schema=user_schema)
    def get(self, id: int) -> User:
        id = user_service.get_by_id(id)
        if id:
            return id
        else:
            return Response(status=404, response="Id not exists")


    def delete(self, id: int) -> Response:
        """Delete Single User"""

        id = user_service.delete_by_id(id)
        if id:
            return jsonify(dict(status="success", id=id))
        else:
            return "error:Id not found", 404

