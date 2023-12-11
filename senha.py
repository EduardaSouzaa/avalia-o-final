#escrever um programa que repita a leitura de uma senha até que seja valido

#criar variavel para receber a senha 
senha = int(input("digite a sua senha "))
#criar condicional para saber se a senha está correta ou não
#se a senha estiver incorreta, escrever mensagem "senha invalida"
if senha != 2002 :
    print("senha invalida")
#se a senha estiver correta, escrever mensagem " acesso permitido"
else:
    print("acesso permitido ")