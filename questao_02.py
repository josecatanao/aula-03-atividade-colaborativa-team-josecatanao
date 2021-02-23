#2) Escreva um programa que leia três números e que imprima o maior e o menor.

n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))

vetor = [n1,n2,n3]
menor=vetor[0]
maior=vetor[0]

for i in vetor:
    if i >= menor:
      maior = i
    else:
      menor = i

    if i < menor:
      menor = i
    else:
      maior = i

print('O maior numero é: ',maior)
print('O menor numero é: ',menor)
   


