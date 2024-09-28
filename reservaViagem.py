#1- Crie um programa que simule um sistema básico de reserva de voos. 
#O programa deve permitir que o usuário adicione reservas de voos enquanto desejar. 
#Cada reserva deve incluir o nome do passageiro e o destino. Ao final, 
#o programa deve listar todas as reservas feitas.

import os
#os.system('cls')  

passagens= []
resposta = "sim"

while resposta == "sim":
    nome = input("Informe seu nome: ")
    destino = input("Informe o Destino: ")
    passagens.append((nome, destino))
    os.system('cls')  
    resposta = input("Deseja incluir mais uma passagem? (sim/nao)")

    os.system('cls')  
print(f"As passagens criadas são: ")
for i in range(len(passagens)):

        print(f"{i + 1} - Nome do Passageiro: {passagens[i][0]} - Destino: {passagens[i][1]}")
 

