import flask
from flask_restplus import Resource, fields
from application.api.restplus import api
from application.api.resources.dataclassifier.service.data_cleaner_service import DataCleanerService
from application.api.resources.dataclassifier.service.data_classifier_service import DataClassifierService
from application.api.resources.dataclassifier.dto.result_classifier import ResultClassifier

namespace = api.namespace('sortdata', description='Operation related to data classification')
# result_post = api.model('ClassifierResult Post', {
#     'bancoDadosRanking': fields.Float(required=True, description='Email'),
#     'programacaoOrientadaObjetoRanking': fields.Float(required=True, description='Email'),
#     'linguagemMarcacaoRanking': fields.Float(required=True, description='Email'),
#     'testeSoftwareRanking': fields.Float(required=True, description='Email'),
#     'linguagemScriptRanking': fields.Float(required=True, description='Email')
# })

result_get = api.model('ClassifierResult Get', {
    'bancoDadosRanking': fields.Float,
    'programacaoOrientadaObjetoRanking': fields.Float,
    'linguagemMarcacaoRanking': fields.Float,
    'testeSoftwareRanking': fields.Float,
    'linguagemScriptRanking': fields.Float
})

# @namespace.route('/<string:content>')
# @namespace.route('/<content>')
@namespace.route('')
@namespace.param('content')
@api.response(404, 'Content is null.')
@namespace.param('content', 'Content to analyzer')
class DataClassifierResource(Resource):

    @api.marshal_with(result_get)
    def get(self):

        content = flask.request.args.get("content")

        print("Content = ", content)

        sliceKeyForSegregation = "#-?_keySlice?_-#"
        textArray = content.split(sliceKeyForSegregation)
        
        content_cleaned = []
        for i in (textArray):
            content_cleaned.append(DataCleanerService.clear_data(i))

        dataframe = DataClassifierService.rateContent(content_cleaned)

        print("Dataframe: ", dataframe)

        bdi = "banco de dados i"
        poo = "programacao orientada a objeto"
        lm = "linguagem de marcacao"
        # ts = "teste de software"
        # ls = "linguagem de script"

        df = dataframe.max()
        punct_bd = df[bdi]
        punct_lm = df[lm]
        punct_poo = df[poo]
        # punct_ts = df[ts]
        # punct_ls = df[ls]

        print("Maximum values: ", df)

        return ResultClassifier(punct_bd, punct_poo, punct_lm, 0, 0)
