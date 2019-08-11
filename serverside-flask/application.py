from flask import Blueprint

from application import application
from application.api.resources.user.user_resource import namespace as users_namespace
from application.api.resources.user.datacleaner_resource import namespace as datacleaner_namespace
from application.api.restplus import api

from application.loader_proper_classification_singleton import LoaderPropertiesClassificationSingleton

# jwt = JWT(application, verify, identity)

blueprint = Blueprint('api', __name__)
api.init_app(blueprint)
api.add_namespace(users_namespace)
api.add_namespace(datacleaner_namespace)
application.register_blueprint(blueprint)

if __name__ == '__main__':
    s1 = LoaderPropertiesClassificationSingleton.instance()
    application.debug = False
    application.run(host='0.0.0.0')
