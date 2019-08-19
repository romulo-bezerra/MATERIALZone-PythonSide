from flask import Blueprint

from application import application
from application.api.resources.dataclassifier.resource.data_classifier_resource import namespace as data_classifier_namespace
from application.api.restplus import api
from application.api.resources.dataclassifier.service.singleton.properties_classification import PropertiesClassification

blueprint = Blueprint('api', __name__)
api.init_app(blueprint)
api.add_namespace(data_classifier_namespace)
application.register_blueprint(blueprint)

if __name__ == '__main__':
    PropertiesClassification.instance()
    application.debug = False
    application.run(host='0.0.0.0')
