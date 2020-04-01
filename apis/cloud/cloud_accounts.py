from flask_restplus import Resource, Namespace, fields

# Included Models for Marshalling
from .cloud_providers import marshal as cp 

api = Namespace('cloud_accounts', description='Cloud Accounts')

marshal = api.model('cloud_accounts', {
    'id': fields.String(required=True, description='Cloud Account ID'),
    'name': fields.String(required=True, description='Cloud Account Name'),
    'cloud_provider': fields.Nested(cp, "The Cloud Provider")
})

CLOUD_ACCOUNTS = [
            {
                "id": "netflix_financial_account",
                "name": "Netflix Financial Account",
                "cloud_provider": {
                    "id": "aws",
                    "name": "Amazon Web Services"
                }
            },
            {
                "id": "netflix_sandbox_account",
                "name": "Netflix Sandbox Account",
                "cloud_provider": {
                    "id": "aws",
                    "name": "Amazon Web Services"
                }
            },
            {
                "id": "spotify_security",
                "name": "Spotify Security",
                "cloud_provider": {
                    "id": "azure",
                    "name": "Microsoft Azure"
                }
            },
            {
                "id": "tiktok_test",
                "name": "TikTok Test",
                "cloud_provider": {
                    "id": "gcp",
                    "name": "Google Cloud Platform"
                }
            }
        ]

@api.route('/')
class Cloud_Accounts(Resource):
    '''Shows a list of all Cloud Accounts, and lets you POST to add new ones'''
    
    @api.doc("get_cp")
    @api.marshal_list_with(marshal)
    def get(self):
        '''Lists all Cloud Accounts'''
        return CLOUD_ACCOUNTS