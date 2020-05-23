from .lib.api_extended import Api
from .lib.flask_extended import Flask
from .lib.config_from_yaml import config_from_yaml
from .api import api
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

config = config_from_yaml('config.yml')
app.config.from_dict(config)
app.register_blueprint(api, url_prefix='/api')
