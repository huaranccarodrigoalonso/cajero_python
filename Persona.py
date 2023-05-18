import os
from datetime import datetime

class Persona:
    name=""
    password=""
    depositoTotal=0
    retiroTotal=0
    saldo=0

    def __init__(self, name, password, deposito, retiro, saldo, dia):
        self.name = name
        self.password = password
        self.depositoTotal = deposito
        self.retiroTotal = retiro
        self.saldo = saldo
        self.dia = dia

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password
    
    def setDepositoTotal(self, depositoTotal):
        self.depositoTotal = depositoTotal
    
    def getDepositoTotal(self):
        return self.depositoTotal
    
    def setRetiroTotal(self, retiroTotal):
        self.retiroTotal = retiroTotal

    def getRetiroTotal(self):
        return self.retiroTotal
    
    def setSaldo(self, saldo):
        self.saldo = saldo
    
    def getSaldo(self):
        return self.saldo
    
    def setDia(self, dia):
        self.dia = dia
    
    def getDia(self):
        return self.dia