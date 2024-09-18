# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.

# digite um numero inteiro

inteiro = int(input("digite seu numero inteiro : "))

# calcular fatorial

fatorial = 1
for i in range (1,inteiro+1):
    fatorial*=i

# exibir resuldado

print(fatorial)