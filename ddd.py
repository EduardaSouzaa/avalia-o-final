#informe à qual cidade o DDD pertence
#se a entrada for qualquer outro DDD que não esteja presente na tabela, escrever a mensagem "DDD não cadastrado"

#CRIAR VARIAVEL PARA RECEBER O DDD
DDD = int(input("digite o DDD"))

#criar condicional para saber se o DDD está cadastrado
if DDD == 11:
    print("São Paulo")

elif DDD == 19:
    print("Campinas")

elif DDD == 21:
    print("Rio de Janeiro")

elif DDD == 27:
    print("Vitoria")

elif DDD == 31:
    print("Belo Horizonte")

elif DDD == 32: 
    print(" Juiz de Fora")

elif DDD == 61:
    print("Brasilia")

elif DDD == 71:
    print("Salvador")

else:
    print("DDD não cadastrado")