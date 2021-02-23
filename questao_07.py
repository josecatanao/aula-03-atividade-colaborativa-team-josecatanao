#7) Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.



kwh = int(input('Digite a quantidade de kWh consumido :'))
print("|----------------------------|")
print('DIGITE O TIPO DE INSTALAÇÃO:')
print('R para residências \nI para indústrias\nC para comércios')
print("|----------------------------|")
simbolo = input("Digite a Letra: ")

if simbolo == 'r':
   if kwh < 500 :
     print('O preço é de R$0,40')
   else:
       print('O preço é de R$0,65')

if simbolo == 'i':
   if kwh < 1000 :
     print('O preço é de R$0,55')
   else :
       print('O preço é de R$0,60')

if simbolo == 'c':
   if kwh < 5000 :
     print('O preço é de R$0,55')
   else :
       print('O preço é de R$0,60')