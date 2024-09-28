#4 - Crie um programa que solicite ao usuário 
#qual a tabuada desejada e escreva a tabuada correspondente:

contador = 0

tabuada = int(input("Qual Tabuada deseja ver:"))
while contador <= 10:
    print(f"{tabuada} X {contador} = {tabuada * contador}")
    contador +=1
