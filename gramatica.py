#no geral verifica se os simbolos pertence a gramatica
import re

class gramatica(object):
    def __init__(self):
        self.string = ''
        self.pReservada = ['if', 'then', 'integer', 'real', 'var']
        self.sSimples = [':', ',', ';', '+']
        self.sDuplo = [':=']

    def isReservada(self, string=''):
        if (string != ''):
            self.setString(string)
        return self.string in self.pReservada

    def isSSimples(self, string=''):
        if(string!=''):
            self.setString(string)
        return self.string in self.sSimples

    def isSDuplo(self, string=''):
        if (string != ''):
            self.setString(string)
        return self.string in self.sDuplo

    def classificar(self):
        if self.isReservada(self.string):
            return 'RES'
        elif self.isSDuplo(self.string):
            return 'DUP'
        elif self.isSSimples(self.string):
            return 'SIM'
        else:
            return 'ERR'

    def setString(self, valor):
        self.string = valor




