#Atividade 2 - Crie um programa que solicita a temperatura 
#em graus Celsius e converte para Fahrenheit.

temp = float(input("Insira a temperatura: "))
#A fórmula para converter a temperatura em
#  graus Celsius (C) para Fahrenheit (F) é F = C x 1,8 + 32. 
Fahre = float(int(temp * (1.8) + 32))
print("Em Fahrenheit: ", Fahre, "F")
