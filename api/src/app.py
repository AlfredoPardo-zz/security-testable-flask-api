from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from apis import api

from config import get_config

app = Flask(__name__)



db = MongoEngine()

CONFIG = get_config()

#app["JWT_SECRET_KEY"] = CONFIG["jwt"]["secret_key"]
app.config["JWT_SECRET_KEY"] = CONFIG["jwt"]["secret_key"]
#app.JWT_SECRET_KEY = CONFIG["jwt"]["secret_key"]
#app.JWT_ALGORITHM = CONFIG["jwt"]["algorithm"]
jwt = JWTManager(app)

db.connect(db=CONFIG["mongodb"]["db_name"],
            username=CONFIG["mongodb"]["username"],
            password=CONFIG["mongodb"]["password"],
            host=CONFIG["mongodb"]["host"],
            port=CONFIG["mongodb"]["port"],
            authentication_source=CONFIG["mongodb"]["auth_source"])

#api = Api(app)
api.init_app(app)

#app.run(host="0.0.0.0", port=5000, ssl_context=('certs/api_cert.pem','certs/api_key.pem'), debug=True)