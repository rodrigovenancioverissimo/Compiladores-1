import numpy as np

linhaToken = 0
tokens = []

class sintatico(object):

    def iniciar(self, caminhoArquivo):
        print("\nFunção iniciar")
        global tokens, linhaToken
        linhaToken = 0
        tokens = np.load(caminhoArquivo)

        print("\n\n########################################")
        print("LISTA DE TOKENS CARREGADA NO SINTATICO")
        print("########################################\n\n")
        print(tokens, "\n\n")

        if(self.Z() and linhaToken == len(tokens) - 1  ):
            print("\n\n########################################")
            print("PARABÉNS PASSOU NA ANÁLISE SINTÁTICA!!")
            print("########################################")
            return True

        print("\n\n*****ERRO SINTATICO NA LINHA ", tokens[linhaToken][1], "*****")
        print("-Token: ", tokens[linhaToken])
        return False

    def D(self):
        print("Função D")
        global tokens, linhaToken
        if(self.L()):
            if(tokens[linhaToken][0] == ":"):
                self.linhaToken()
                if(self.K()):
                    if(self.O()):
                        return True
        return False

    def E(self):
        print("Função E")
        global tokens, linhaToken
        if(self.T()):
            if(self.R()):
                return True
        return False

    def I(self):
        print("Função I")
        global tokens, linhaToken
        if(tokens[linhaToken][0] == "var"):
            self.linhaToken()
            if(self.D()):
                return True
        return False

    def K(self):
        print("Função K")
        global tokens, linhaToken
        if(tokens[linhaToken][0] == "integer" or tokens[linhaToken][0] == "real"):
            self.linhaToken()
            return True
        return False

    def L(self):
        print("Função L")
        global tokens, linhaToken
        if(tokens[linhaToken][2] == "ID"):
            self.linhaToken()
            if(self.X()):
                return True
        return False

    def O(self):
        print("Função O")
        global tokens, linhaToken
        if(tokens[linhaToken][0] == ";"):
            self.linhaToken()
            if(self.D()):
                return True
            else:
                return False
        return True

    def R(self):
        print("Função R")
        global tokens, linhaToken
        if(tokens[linhaToken][0] == "+" ):
            self.linhaToken()
            if(self.T()):
                return self.R()
            return False
        return True

    def S(self):
        print("Função S")
        global tokens, linhaToken
        if(tokens[linhaToken][2] == "ID"):
            self.linhaToken()
            if(tokens[linhaToken][0] == ":="):
                self.linhaToken()
                if(self.E()):
                    if(tokens[linhaToken][0] == "then"):
                        self.linhaToken()
                        return self.S()
                    return True
        elif(tokens[linhaToken][0] == "if"):
            self.linhaToken()
            if (self.E()):
                if (tokens[linhaToken][0] == "then"):
                    self.linhaToken()
                    return self.S()
                return True
        return False

    def T(self):
        print("Função T")
        global tokens, linhaToken
        if(tokens[linhaToken][2] == "ID"):
            self.linhaToken()
            return True
        return False

    def X(self):
        print("Função X")
        global tokens, linhaToken
        if(tokens[linhaToken][0] == ","):
            self.linhaToken()
            if(self.L()):
                return True
            return False
        return True

    def Z(self):
        print("Função Z")
        global tokens
        if(self.I()):
            if(self.S()):
                return True
        return False

    def linhaToken(self):
        global linhaToken, tokens
        print("Achou o Terminal", tokens[linhaToken][0])
        if (linhaToken < len(tokens) - 1):
            linhaToken += 1
            return True
        elif(linhaToken > len(tokens) - 1):
            print("*****ESTOURO DO ARRAY DE TOKENS*****")
        return False
