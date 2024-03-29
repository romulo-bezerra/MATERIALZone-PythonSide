import flask
from flask_restplus import Resource, fields
from application.api.restplus import api
from application.api.resources.dataclassifier.service.data_cleaner_service import DataCleanerService
from application.api.resources.dataclassifier.service.data_classifier_service import DataClassifierService
from application.api.resources.dataclassifier.dto.result_classifier import ResultClassifier

namespace = api.namespace('sortdata', description='Operation related to data classification')
result_get = api.model('ClassifierResult Get', {
    'bancoDadosRanking': fields.Float,
    'programacaoOrientadaObjetoRanking': fields.Float,
    'linguagemMarcacaoRanking': fields.Float,
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

        sliceKeyForSegregation = "#-?_keySlice?_-#"
        textArray = content.split(sliceKeyForSegregation)
        
        content_cleaned = []
        for i in (textArray):
            content_cleaned.append(DataCleanerService.clear_data(i))

        dataframe = DataClassifierService.rateContent(content_cleaned)

        # print("Dataframe: ", dataframe)

        bd = "banco de dados"
        poo = "programacao orientada a objeto"
        lm = "linguagem de marcacao"
        ls = "linguagem de script"

        df = dataframe.max()
        punct_bd = df[bd]
        punct_lm = df[lm]
        punct_poo = df[poo]
        punct_ls = df[ls]
        # punct_ts = df[ts]

        print("Maximum values: ", df)

        return ResultClassifier(punct_bd, punct_poo, punct_lm, punct_ls)

