from flask_sqlalchemy import SQLAlchemy

from application.enums import UserRole
from application.serialize import Serializer

class CepResponse:
    def __init__(self, bdi, poo, lm):
        self.bdi = bdi
        self.poo = poo
        self.lm = lm
     
    def setBDI(self, bdi):
        self.bdi = bdi
     
    def setPOO(self, poo):
        self.poo = poo
    
    def setLM(self, lm):
        self.lm = lm
        
    def getBDI(self):
        return self.bdi
         
    def getPOO(self):
        return self.poo

    def getLM(self):
        return self.lm