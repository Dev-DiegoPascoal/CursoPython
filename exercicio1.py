#1- Crie um programa que simule um sistema básico 
#de reserva de voos. O programa deve permitir que 
#o usuário adicione reservas de voos enquanto desejar.
#Cada reserva deve incluir o nome do passageiro e o destino.
#Ao final, o programa deve listar todas as reservas feitas.

reserva = 0
resposta = "sim"

while resposta == "sim":
    reserva = input("Digite seu nome:") 
    reserva = input("Informe seu destino")
    resposta = input("Deseja realizar mais alguma reserva?")

for i in reserva:
    print(reserva)