from flask_restplus import Resource, Namespace, fields
from flask import request

from models.cloud.cloud_account import CloudAccount
from models.cloud.cloud_provider import CloudProvider
from models.general.customer import Customer
# Included Models for Marshalling
from apis.general.customers import model as cs
from apis.cloud.cloud_providers import model as cp

api = Namespace('cloud_accounts', description='Cloud Accounts')

model = api.model('cloud_accounts', {
    'uid': fields.String(required=True, description='Cloud Account ID'),
    'name': fields.String(required=True, description='Cloud Account Name'),
    'customer': fields.Nested(cs, "Customer"),
    'cloud_provider': fields.Nested(cp, "Cloud Provider")
})

model_cu = api.model('cloud_accounts_cu', {
    'uid': fields.String(required=True, description='Cloud Account ID'),
    'name': fields.String(required=True, description='Cloud Account Name'),
    'customer_uid': fields.String(required=True, description='Customer UID'),
    'cloud_provider_uid': fields.String(required=True, description='Cloud Provider UID')
})

@api.route('/')
class Cloud_Accounts(Resource):

    @api.marshal_list_with(model)
    def get(self):
        '''Lists all Cloud Accounts'''
        return list(CloudAccount.objects()), 200

    @api.expect(model_cu)
    @api.marshal_with(model_cu, code=201)
    def post(self):
        '''Creates a new Cloud Account'''

        if request.is_json:
            content = request.json

            customer = Customer.objects(uid=content["customer_uid"]).first()
            cloud_provider = CloudProvider.objects(uid=content["cloud_provider_uid"]).first()

            cloud_account = CloudAccount(uid=content["uid"], name=content["name"], \
                customer=customer, cloud_provider=cloud_provider)
            
            cloud_account.save()
            
            return cloud_account.to_dict(), 201

        else:
            return 400

@api.route('/<string:uid>')
class Cloud_Accounts_By_UID(Resource):

    @api.marshal_with(model)
    def get(self, uid):
        '''Shows a Cloud Account'''
        cloud_account = CloudAccount.objects(uid=uid).first()

        if cloud_account:
            return cloud_account, 200
        else:
            return {}, 404

    def delete(self, uid):
        '''Deletes a Cloud Account'''
        
        cloud_account = CloudAccount.objects(uid=uid)
        
        if cloud_account:
            cloud_account.delete()
            return {"msg": "{} has been removed.".format(uid)}, 200
        else:
            return {"msg": "{} has not been found.".format(uid)}, 404
        
    @api.expect(model_cu)
    @api.marshal_with(model_cu, code=200)
    def put(self, uid):
        '''Updates a Cloud Account'''
        if request.is_json:
            content = request.json
            cloud_account = CloudAccount.objects(uid=uid).first()
            if cloud_account:

                customer = Customer.objects(uid=content["customer_uid"]).first()
                cloud_provider = CloudProvider.objects(uid=content["cloud_provider_uid"]).first()

                cloud_account.name = content["name"]
                cloud_account.customer = customer
                cloud_account.cloud_provider = cloud_provider
                cloud_account.save()

                return cloud_account.to_dict(), 200
            
            else:
            
                return {}, 404
        
        else:
            
            return {}, 400