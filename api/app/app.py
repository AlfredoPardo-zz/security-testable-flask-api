from flask import Flask
from flask_mongoengine import MongoEngine

from apis import api

from config import get_config

app = Flask(__name__)

db = MongoEngine()

CONFIG = get_config()
db.connect(db=CONFIG["mongodb"]["db_name"],
            username=CONFIG["mongodb"]["username"],
            password=CONFIG["mongodb"]["password"],
            host=CONFIG["mongodb"]["host"],
            port=CONFIG["mongodb"]["port"],
            authentication_source=CONFIG["mongodb"]["auth_source"])

api.init_app(app)

#app.run(host="0.0.0.0", port=5000, ssl_context=('certs/api_cert.pem','certs/api_key.pem'), debug=True)