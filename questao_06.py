#6) Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valorCasa = int(input('Digite o valor da casa :'))
salario = int(input('Digite o valor do salario :'))
QuantAnos = int(input('Digite a quantidade de anos :'))

limite = (salario * (30/1000))
prestacao = (valorCasa/(QuantAnos*12))
print(limite)
print(prestacao)

if prestacao> limite :
  print('O valor da prestação passa o limite maximo, vc não pode fazer o emprestimo')
else:
  print('voce pode realizr o emprestimo')

