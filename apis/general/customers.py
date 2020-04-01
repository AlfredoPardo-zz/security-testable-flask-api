from flask_restplus import Resource, Namespace, fields

api = Namespace('customers', description='Customers')

marshal = api.model('customers', {
    'id': fields.String(required=True, description='Customer ID'),
    'name': fields.String(required=True, description='Customer Name')
})

CUSTOMERS = [
            {
                "id": "netflix",
                "name": "Netflix"
            },
            {
                "id": "spotify",
                "name": "Spotify"
            },
            {
                "id": "tiktok",
                "name": "TikTok"
            }
        ]

@api.route('/')
class Customers(Resource):
    '''Shows a list of all Customers'''
    
    @api.doc("get_cp")
    @api.marshal_list_with(marshal)
    def get(self):
        '''Lists all Customers'''
        return CUSTOMERS