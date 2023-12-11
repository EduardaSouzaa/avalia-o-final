#criar programa que leia 6 numeros 
#mostre quantos valores digitados foram positivos

#criar variavel para receber o numero  
valoresPos = 0
soma= 0 
#fazer uma execução de loop para repetir os seis numeros 
for valor in range (0,6):
    numero = float(input("digite o {valor} numero: "))
    if numero > 0:
        valoresPos += 1 
        soma += numero
#criar a variavel da media 
media = soma/valoresPos
#mostrar quais numeros são positivos 
print(f"{valoresPos} numeros posiivos")
#mostrar a media da variavel valoresPos
print(f"{round(media,2)}")



