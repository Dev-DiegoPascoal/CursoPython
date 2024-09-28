#Atividade 3 - Crie um programa que solicite 
# o raio de um circulo e calcule sua área

raio = float(input("Informe o raio do círculo em centímetros: "))

#fórmula seria A = 3,14 . 7², onde 7² = 49. 

area = float(3.14 * raio**2)
print(f"A área do círculo é: {area} CM de Comprimento")