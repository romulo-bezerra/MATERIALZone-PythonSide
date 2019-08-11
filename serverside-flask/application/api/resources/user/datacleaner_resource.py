from flask_restplus import Resource, fields
from application.api.restplus import api
from flask_jwt import jwt_required
from flask import request, abort
from application.serialize import Serializer
from application.api.resources.user.datacleaner_service import DataCleanerService
from application.api.resources.user.data_classifier_service import DataClassifierService

namespace = api.namespace('dataclear', description='Operations related to data cleaner')
user_post = api.model('User Post', {'result': fields.String(required=True, description='X', max_length=80)})
result_get = api.model('User Get', {'result': fields.String})

@namespace.route('/<string:text>')
@api.response(404, 'Text is null.')
@namespace.param('text', 'The text to analyzer')
class DataCleanerResource(Resource):

    @api.marshal_with(result_get)
    def get(self, text):

        textArray = text.split("#-?_keySlice?_-#")
        
        content_cleaned = []
        for i in (textArray):
            content_cleaned.append(DataCleanerService.clear_data(i))

        print("Dados limpos: ")
        print(content_cleaned)

        datagrama = DataClassifierService.classficandoTemp(content_cleaned)
        
        bdi = "banco de dados i"
        poo = "programacao orientada a objeto"
        lm = "linguagem de marcacao"
        
        punct_bd = datagrama[bdi].argmax()
        punct_poo = datagrama[poo].argmax()
        punct_lm = datagrama[lm].argmax()
        
        result = bdi + '=' + str(punct_bd) + ',' + poo + '=' + str(punct_poo) + ',' + lm + '=' + str(punct_lm) 

        return {'result': result}