from flask_restplus import Resource, Namespace, fields
from flask import request

from models.cloud.cloud_provider import CloudProvider

api = Namespace('cloud_providers', description='Cloud Providers')

model = api.model('cloud_providers', {
    'uid': fields.String(required=True, description='Cloud Provider ID'),
    'name': fields.String(required=True, description='Cloud Provider Name'),
    'abbreviation': fields.String(required=True, description='Cloud Provider Abbreviation')
})

@api.route('/')
class Cloud_Providers(Resource):
    
    @api.marshal_list_with(model)
    def get(self):
        '''Lists all Cloud Providers'''
        return list(CloudProvider.objects()), 200

    @api.expect(model)
    @api.marshal_with(model, code=201)
    def post(self):
        '''Creates a new Cloud Provider'''
        if request.is_json:
            content = request.json
            cloud_provider = CloudProvider(uid=content["uid"], \
                name=content["name"], abbreviation=content["abbreviation"])
            cloud_provider.save()
            return cloud_provider, 201
        else:
            return 400

@api.route('/<string:uid>')
class Cloud_Providers_By_UID(Resource):

    @api.marshal_with(model)
    def get(self, uid):
        '''Shows a Cloud Provider'''
        cloud_provider = CloudProvider.objects(uid=uid).first()

        if cloud_provider:
            return cloud_provider, 200
        else:
            return {}, 404

    def delete(self, uid):
        '''Deletes a Cloud Provider'''
        
        cloud_provider = CloudProvider.objects(uid=uid)
        
        if cloud_provider:
            cloud_provider.delete()
            return {"msg": "{} has been removed.".format(uid)}, 200
        else:
            return {"msg": "{} has not been found.".format(uid)}, 404


    @api.expect(model)
    @api.marshal_with(model, code=200)
    def put(self, uid):
        '''Updates a Cloud Provider'''
        if request.is_json:
            content = request.json
            cloud_provider = CloudProvider.objects(uid=uid).first()
            if cloud_provider:

                cloud_provider.name = content["name"]
                cloud_provider.abbreviation = content["abbreviation"]
                cloud_provider.save()

                return cloud_provider, 200
            
            else:
            
                return {}, 404
        
        else:
            
            return {}, 400