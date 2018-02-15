import re
import gramatica
import numpy as np

class lexico(object):

    def iniciar(self):

        print("\n\n########################################")
        print("INICIO DO LOOP DO ANALISADOR LEXICO")
        print("########################################\n\n")
        tokens = []

        codigoFonte = open("codigoFonte.txt", 'r')
        saida = open("saidaLexico.txt" , "w")

        contLinha = 1

        token = ""
        caracter = codigoFonte.read(1)

        g = gramatica.gramatica()

        if caracter == "":  # ARQ VAZIO
            pass
        #####LOOP PRINCIPAL#####
        else:
            while True:
                print(".....novo loop")
                token = ""

                if caracter == "":  # END OF FILE
                    break

                if re.match("\d", caracter) is not None:
                    #####NUMERAL ENCONTRADO#########
                    print(".....numeral")
                    token = token + caracter
                    flag = 0
                    while True:
                        caracter = codigoFonte.read(1)
                        if re.match("\d", caracter) is not None:
                            token = token + caracter
                        elif re.match("\.", caracter) is not None and flag == 0:
                            flag = 1
                            token = token + caracter
                        else:
                            tokens.append([token, contLinha, "ID"])
                            break

                elif re.match("\:", caracter) is not None:
                    ###########ATRIBUIÇÃO ENCONTRADA######
                    print(".....simbolo :")
                    token = token + caracter
                    caracter = codigoFonte.read(1)
                    if re.match("\=", caracter) is not None:
                        print(".....simbolo =")
                        token = token + caracter
                        tokens.append([token, contLinha, "DUP"])
                        caracter = codigoFonte.read(1)
                    else:
                        tokens.append([token, contLinha, "SIM"])

                elif g.isSSimples(caracter):
                    ###########SIMBOLO SIMPLES ENCONTRADO######
                    print(".....simbolo simples")
                    token = token + caracter
                    tokens.append([token, contLinha, "SIM"])
                    caracter = codigoFonte.read(1)


                elif re.match("[a-z]|[A-Z]", caracter) is not None:
                    ###########ID ENCONTRADA######
                    print(".....string")
                    token = token + caracter
                    #tokens.append([token, contLinha, "IDD"])
                    while True:
                        caracter = codigoFonte.read(1)
                        if re.match("[a-z]|[A-Z]", caracter) is not None:
                            token = token + caracter
                        else:
                            if g.isReservada(token):
                                tokens.append([token, contLinha, "RES"])
                            else:
                                tokens.append([token, contLinha, "ID"])
                            break

                elif re.match("\n", caracter):
                    ###########NOVA LINHA ENCONTRADA######
                    print(".....nova linha")
                    caracter = codigoFonte.read(1)
                    contLinha = contLinha + 1

                elif re.match("\ ", caracter) is not None:
                    print(".....espaço")
                    caracter = codigoFonte.read(1)

                else:
                    print("\n\n*****ERRO NA LINHA", contLinha, "CARACTER", caracter, "NÃO EXISTE*****")
                    return False

        print("\n\n\n\n##########################")
        print("LISTA DE TOKENS")
        print("##########################\n\n")
        for token in tokens:
            if(token[2] == "ID"):
                print(token[0], "- linha", token[1], "- Identificador")
                saida.write(str(token[0]) + " - linha " + str(token[1])+ " - Identificador\n")
            elif(token[2] == "RES"):
                print(str(token[0]), "- linha", str(token[1]), "- Palavra Reservada")
                saida.write(str(token[0]) + " - linha " + str(token[1]) + " - Palavra Reservada\n")
            elif (token[2] == "SIM"):
                print(str(token[0]), "- linha", str(token[1]), "- Simbolo Simples")
                saida.write(str(token[0]) + " - linha " + str(token[1]) + " - Simbolo Simples\n")
            elif (token[2] == "DUP"):
                print(token[0], "- linha", token[1], "- Simbolo Duplo")
                saida.write(str(token[0]) + " - linha " + str(token[1]) + " - Simbolo Duplo\n")
        saida.close()

        np.save("saidaTokens", tokens)

        return True