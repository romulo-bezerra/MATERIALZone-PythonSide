from flask_restplus import Api

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(version='1.0', title='Data Classifier API',
          description='A machine learning classification application for the Data Analysis Service',
          authorizations=authorizations, security='apikey')
