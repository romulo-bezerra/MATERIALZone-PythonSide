from flask import Flask
from flask_cors import CORS

application = Flask(__name__, instance_relative_config=True)
CORS(application, resources={r"/*": {"origins": "*"}})

application.config.setdefault('RESTPLUS_MASK_SWAGGER', False)
