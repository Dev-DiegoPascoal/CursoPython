#2 - Crie um programa que solicite números para o usuário até que ele digite 0. 
#Ao final deve ser perguntado ao usuário se é ordem crescente e decrescente 
#e mostrar a lista ordenada.

resposta = "1"
ordenar = "0"
ordenar = "cres"
numeros = []

while resposta == "1":
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
    resposta = input("Deseja incluir mais um número? (sim = 1/Não = 0)")

if resposta == 0:
    for i in range(len(numeros)):
        print(f"{i + 1} - Números: {numeros[i]}")
        ordenar = input("Deseja ordenar de forma descrecente (desc) ou Crescente (cres)")
            #if ordenar == "desc":
                #if numero