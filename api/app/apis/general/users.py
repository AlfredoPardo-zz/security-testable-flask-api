from flask_restplus import Resource, Namespace, fields, marshal_with
from flask import request

from models.general.user import User

api = Namespace("users", description="Users")

model = api.model("users", {
    "username": fields.String(required=True, description="Username"),
    "password": fields.String(required=True, description="Password"),
    "name": fields.String(required=True, description="User's name")
})

model_auth = api.model("users_auth", {
    "username": fields.String(required=True, description="Username"),
    "password": fields.String(required=True, description="Password")
})

@api.route('/')
class Users(Resource):
   
    @api.marshal_list_with(model)
    def get(self):
        '''Lists all Users'''
        return list(User.objects()), 200

    @api.expect(model)
    @api.marshal_with(model, code=201)
    def post(self):
        '''Creates a new User'''
        if request.is_json:
            content = request.json
            user = User(username=content["username"], \
                password=content["password"], \
                name=content["name"])
            user.save()
            return user, 201
        else:
            return 400

@api.route('/<string:username>')
class Users_By_Username(Resource):

    @api.marshal_with(model)
    def get(self, username):
        '''Shows a User'''

        user = User.objects(username=username).first()

        if user:

            return user, 200

        else: 

            return {}, 404

    def delete(self, username):

        '''Deletes a User'''
        
        user = User.objects(username=username)
        if user:
            user.delete()
            return {"msg": "{} has been removed.".format(username)}, 200
        else:
            return {"msg": "{} has not been found.".format(username)}, 404
        
    @api.expect(model)
    @api.marshal_with(model, code=200)
    def put(self, username):
        '''Updates a User'''
        if request.is_json:
            content = request.json
            user = User.objects(username=username).first()
            if user:
                user.password = content["password"]
                user.name = content["name"]
                user.save()
                return user, 200
            else:
                return {}, 404
        else:
            return {}, 400


@api.route('/auth')
class Users_Auth(Resource):

    @api.expect(model_auth)
    def post(self):
        '''Authenticates a User'''
        if request.is_json:
            content = request.json
            user = User.objects(username=content["username"], password=content["password"]).first()
            if user:
                return {"msg": "Authentication Successful."}, 200
        else:
            return 400