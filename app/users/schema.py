from marshmallow import fields, Schema

class UserSchema(Schema):

    id = fields.Number(attribute="id")
    first_name = fields.String(attribute="first_name")
    last_name = fields.String(attribute="last_name")
    full_name = fields.String(attribute="full_name")
    salary = fields.Number(attribute="salary")
    address = fields.String(attribute="address")
    created_at = fields.DateTime(attribute="created_at")