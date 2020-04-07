from flask_restplus import Api

from apis.cloud.cloud_accounts import api as cloud_accounts_ns
from apis.cloud.cloud_providers import api as cloud_providers_ns
from apis.general.customers import api as customers_ns

api = Api(
    title='Security-testable Flask API',
    version='1.0',
    description='This API is able to be automatically tested by providing a swagger.json file to feed Vulnerability Assessment Tools like OWASP ZAP and Burp Suite. Additionally it is documented from the get-go which is important for an organized Software Development Life Cycle.',
    # All API metadatas
)

api.add_namespace(cloud_accounts_ns)
api.add_namespace(cloud_providers_ns)
api.add_namespace(customers_ns)
