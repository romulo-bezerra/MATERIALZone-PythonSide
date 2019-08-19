from flask_restplus import Resource, fields
from application.api.restplus import api
from application.api.resources.dataclassifier.service.data_cleaner_service import DataCleanerService
from application.api.resources.dataclassifier.service.data_classifier_service import DataClassifierService
from application.api.resources.dataclassifier.dto.result_classifier import ResultClassifier

namespace = api.namespace('sortdata', description='Operation related to data classification')
result_get = api.model('Classifier Result', {
    'bancoDadosRanking': fields.Float,
    'programacaoOrientadaObjetoRanking': fields.Float,
    'linguagemMarcacaoRanking': fields.Float,
    'testeSoftwareRanking': fields.Float,
    'linguagemScriptRanking': fields.Float
})

@namespace.route('/<string:content>')
@api.response(404, 'Content is null.')
@namespace.param('content', 'Content to analyzer')
class DataClassifierResource(Resource):

    @api.marshal_with(result_get)
    def get(self, content):
        textArray = content.split("#-?_keySlice?_-#")
        
        content_cleaned = []
        for i in (textArray):
            content_cleaned.append(DataCleanerService.clear_data(i))

        dataframe = DataClassifierService.rateContent(content_cleaned)

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

        return ResultClassifier(punct_bd, punct_poo, punct_lm, 0, 0)
