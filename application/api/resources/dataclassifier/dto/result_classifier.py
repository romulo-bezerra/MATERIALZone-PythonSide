class ResultClassifier:

    def __init__(self, bancoDadosRanking, programacaoOrientadaObjetoRanking, linguagemMarcacaoRanking, testeSoftwareRanking, linguagemScriptRanking):
        self.bancoDadosRanking = bancoDadosRanking
        self.programacaoOrientadaObjetoRanking = programacaoOrientadaObjetoRanking
        self.linguagemMarcacaoRanking = linguagemMarcacaoRanking
        self.testeSoftwareRanking = testeSoftwareRanking
        self.linguagemScriptRanking = linguagemScriptRanking

    def getBancoDadosRanking(self):
        return self.bancoDadosRanking

    def setBancoDadosRanking(self, bdRanking):
        self.bancoDadosRanking = bdRanking

    def getProgramacaoOrientadaObjetoRanking(self):
        return self.programacaoOrientadaObjetoRanking

    def setProgramacaoOrientadaObjetoRanking(self, pooRanking):
        self.programacaoOrientadaObjetoRanking = pooRanking

    def getLinguagemMarcacaoRanking(self):
        return self.linguagemMarcacaoRanking

    def setLinguagemMarcacaoRanking(self, lmRanking):
        self.linguagemMarcacaoRanking = lmRanking

    def getTesteSoftwareRanking(self):
        return self.testeSoftwareRanking

    def setTesteSoftwareRanking(self, tsRanking):
        self.testeSoftwareRanking = tsRanking

    def getLinguagemScriptRanking(self):
        return self.linguagemScriptRanking

    def setLM(self, lsRanking):
        self.linguagemScriptRanking = lsRanking
