#3 - Crie um programa que solicite ao usuário 5 números e ao final imprima 
#a soma de todos eles.

contador = 0
numeros = []

while contador < 5:
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
    contador = contador + 1

print("Os números inseridos são: ")
for i in range(len(numeros)):
    print(f"{numeros[i]}")

soma = 0
for numero in numeros:
    soma += numero
print("*****************************")
print(f"A soma dos números é: {soma}")
