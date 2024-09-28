print("********************************************")
print("*************Escola SENAI*******************")
print("********************************************")
nome = input("Olá boa Tarde, digite seu nome:")
print("********************************************")
print("Seu nome é:",nome)

# O sinal de mais + não adiciona espaço entre as palavras
print("Olá, "+ nome + "!")

# O sinal de vírugula, adiciona espaço enre as palavras
print("Olá, ", nome, "!")

# O sinal de percentagem % é ama forma antiga de formatar strings
print("Olá, %s!" % nome)

# O método format{} é uma forma mais moderna de formatar strings
print("Olá, {}!".format(nome))

# O f - string é a forma mais moderna de formatar strings
print(f"Olá, {nome}!")

numeroUm = int(input("Digite um numero: "))
numeroDois = float(input("Digite outro numero: "))
print("A soma dos dois numeros é ", numeroUm + numeroDois)