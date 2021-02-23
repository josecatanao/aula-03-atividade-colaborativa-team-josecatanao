#3) Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00,calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input('digite o valor do salario:'))

if salario > 1250 :
  salario = salario+(salario*(10/1000))
else:
   salario = salario+(salario*(15/1000))

print(salario)
