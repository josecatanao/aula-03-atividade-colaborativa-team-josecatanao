#5) Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

n1 = int(input('digite um numero :'))
n2 = int(input('digite um numero :'))

print("|----------------------------|")
print('DIGITE O SIMBOLO DA OPERAÇÃO QUE DESEJAREALIZAR:')
print('soma (+)\nsubtração (-)\nmultiplicação (*)\ndivisão (/)')
print("|----------------------------|")
simbolo = input("Digite o simbolo: ")

if simbolo == '+' :
          print(n1,'+',n2,'=',n1+n2)
elif simbolo == '-' :
  print(n1,'-',n2,'=',n1-n2)
elif simbolo == '*' :
  print(n1,'*',n2,'=',n1*n2)
elif simbolo == '/' :
  print(n1,'/',n2,'=',n1/n2)
else:
  print('simbolo invalido')