#criar variavel para receber o valor do
salario = float(input("digite seu salario"))
# verificar se o salário é menor que 400.00 
if salario <= 400.00:
    print(f"Novo salário: {salario+(salario*(15/100)):.2f}")
    print(f"Reajuste ganho:{salario*(15/100):.2f}")
    print(" percentual: 15 %")

# verificar se o salário é  maior que 400.01 e menor que 800.00 
elif salario >= 400.01 and salario <= 800.00:
    print(f"Novo salário: {salario+(salario*(12/100)):.2f}")
    print(f"Reajuste ganho:{salario*(12/100):.2f}")
    print("percentual: 12 %")

# verificar se o salário , é maior que 800.01 e menor que 1200.00 
elif salario >= 800.01 and salario <= 1200.00:
    print(f"Novo salário: {salario+(salario*(10/100)):.2f}")
    print(f"Reajuste ganho:{salario*(10/100):.2f}")
    print(" percentual: 10 %")

#o verificarse o salário ,  é maior que 1200.01 e menor que 2000.00 
elif salario >= 1200.01 and salario <= 2000.00:
    print(f"Novo salário: {salario+(salario*(7/100)):.2f}")
    print(f"Reajuste ganho:{salario*(7/100):.2f}")
    print(" percentual: 7 %")

# verificar se o salário é  maior que 2000.01 
elif salario >  2000.01:
    print(f"Novo salário: {salario+(salario*(4/100)):.2f}")
    print(f"Reajuste ganho:{salario*(4/100):.2f}")
    print(" percentual: 4 %")