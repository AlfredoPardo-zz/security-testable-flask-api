from flask_restplus import Resource, Namespace, fields

api = Namespace('cloud_providers', description='Cloud Providers')

marshal = api.model('cloud_providers', {
    'id': fields.String(required=True, description='Cloud Provider ID'),
    'name': fields.String(required=True, description='Cloud Provider Name')
})

CLOUD_PROVIDERS = [
            {
                "id": "aws",
                "name": "Amazon Web Services"
            },
            {
                "id": "azure",
                "name": "Microsoft Azure"
            },
            {
                "id": "gcp",
                "name": "Google Cloud Platform"
            }
        ]

@api.route('/')
class Cloud_Providers(Resource):
    '''Shows a list of all Cloud Providers'''
    
    @api.doc("get_cp")
    @api.marshal_list_with(marshal)
    def get(self):
        '''Lists all Cloud Providers'''
        return CLOUD_PROVIDERS