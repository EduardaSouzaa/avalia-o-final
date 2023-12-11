#faça um programa que leia 5 valores inteiros. 

#criar uma lista na variavel "valoresInt" para armazenar os 5 numeros inteiros 
valoresInt = []

#criar uma variavel para saber quais numeros são pares 
numPares = 0 
#fazer uma execução de loop para repetir os cinco numeros 
for valores in range (0,5):
    numero = int(input(f"digite o {valores} numero: "))
    valoresInt.append(numero)

#criar condicional para saber se os numeros são pares 
    if numero % 2 == 0:
        numPares +=1
        print(f"{numPares} numeros pares")


