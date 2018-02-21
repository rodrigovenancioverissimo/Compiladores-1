import numpy as np

tokens = list()
linhaToken = 0
tabelaDeSimbolos = dict()
msg = ""
posicoes = list()
firstID = False
tipo = ""

class semantico(object):

    def iniciar(self, caminhoArquivo):
        print("\nFunção iniciar")
        global tokens, linhaToken, tabelaDeSimbolos
        linhaToken = 0
        tokens = np.load(caminhoArquivo)

        print("\n\n########################################")
        print("LISTA DE TOKENS CARREGADA NO SEMÂNTICO")
        print("########################################\n\n")
        print(tokens, "\n\n")

        if (self.Z() and linhaToken == len(tokens) - 1  ):
            print("\n\n########################################")
            print("PARABÉNS PASSOU NA ANÁLISE SEMÂNTICA!!")
            print("########################################")
            print(tabelaDeSimbolos)
            return True

        print("\n\n*****ERRO SEMÂNTICO NA LINHA ", tokens[linhaToken][1], "*****")
        print(msg)
        print("-Token: ", tokens[linhaToken])
        return False

    def D(self):
        print("Função D")
        global tokens, linhaToken, posicoes
        posicoes.clear()
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
        if(tokens[linhaToken][0] == "integer"):
            self.tipo("int")
            self.linhaToken()
            return True
        elif(tokens[linhaToken][0] == "real"):
            self.tipo("float")
            self.linhaToken()
            return True
        return False

    def L(self):
        print("Função L")
        global tokens, linhaToken
        if(tokens[linhaToken][2] == "ID"):
            if(self.inserir(tokens[linhaToken])):
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
        global tokens, linhaToken, tipo, firstID
        tipo = ""
        print("Tipo = ", tipo)
        firstID = True
        if(tokens[linhaToken][2] == "ID"):
            if(self.buscar(tokens[linhaToken])):
                if(self.igualdade(tokens[linhaToken])):
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
            if(self.buscar(tokens[linhaToken])):
                if(self.igualdade(tokens[linhaToken])):
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

    def inserir(self, token):
        print("Função Inserir")
        global tabelaDeSimbolos, msg, posicoes
        key = token[0]
        if(key not in tabelaDeSimbolos):
                                    # lexema, categoria, tipo, valor
            tabelaDeSimbolos[key] = [token[0], token[2],  "",   ""]
            posicoes.append(key)
            return True
        msg += "-ID já declarada"
        return False

    def buscar(self, token):
        print("Função Buscar")
        global tabelaDeSimbolos, msg
        key = token[0]
        if (key in tabelaDeSimbolos):
            return True
        msg += "-ID não foi declarada"
        return False

    def tipo(self, tipo):
        print("Função Tipo")
        global posicoes, tabelaDeSimbolos
        for p in posicoes:
            tabelaDeSimbolos[p][2] = tipo
        return True

    def igualdade(self, token):
        print("Função Igualdade")
        global msg, firstID, tipo, tabelaDeSimbolos
        print("Tipo = ", tipo)
        if(firstID == True):
            tipo = tabelaDeSimbolos[token[0]][2]
            print("O ID", token[0], "é o", "FirstID")
            print("tipo = ", tipo)
            firstID = False
            return True
        elif (tabelaDeSimbolos[token[0]][2] == tipo):
            print("Igualdade de Tipo está OK")
            return True
        msg += "\n-Tipos diferentes\n"
        msg += "-ID na Tabela: "
        msg += str(tabelaDeSimbolos[token[0]])
        return False