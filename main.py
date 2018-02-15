import lexico, sintatico, semantico

print("########################################")
print("INICIO DA ANALISE LEXICA")
print("########################################\n\n")
l = lexico.lexico()
if(l.iniciar()):
    print ("\n\n+++++++++++++++")
    print ("LÉXICO OK")
    print ("+++++++++++++++\n\n")
else:
    print ("\n\n*****ERRO LÉXICO*****")
    exit()



print("########################################")
print("INICIO DA ANALISE SINTÁTICA")
print("########################################\n\n")
s = sintatico.sintatico()
if(s.iniciar("saidaTokens.npy")):
    print ("\n\n+++++++++++++++")
    print ("SINTÁTICO OK")
    print ("+++++++++++++++\n\n")
else:
    print ("\n\n*****ERRO SINTÁTICO*****")
    exit()


print("########################################")
print("INICIO DA ANALISE SEMÂNTICA")
print("########################################\n\n")
se = semantico.semantico()
if(se.iniciar("saidaTokens.npy")):
    print("\n\n+++++++++++++++")
    print("SEMÂNTICO OK")
    print("+++++++++++++++\n\n")
else:
    print("\n\n*****ERRO SEMÂNTICO*****")
    exit()

print("########################################")
print("COMPILAÇÃO CONCLUIDA COM SUCESSO.")
print("########################################\n\n")