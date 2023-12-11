#leia um valor com duas casas decimais, equivalente ao salario de uma pessoa de Lisarb.
#calcule e mostre o valor que esta pessoa deve pagar de impostos de renda, segundo a tabela abaixo.

#criar variavel para receber o valor da renda
renda = float(input("digite o valor"))
#criar condicional ja que as porcentagens são diferentes
if renda <= 2000.00:
    print("isento") 

elif renda > 2000.00 <= 3000.00:
    print(f"R${renda * (8 / 100)}")

elif renda > 3000.00 <= 4500.00:
    print(f"R${renda * (18 /100)}")

else:
    print(f"R${renda * (28 / 100)}") 