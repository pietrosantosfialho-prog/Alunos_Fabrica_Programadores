# CALCULADORA DE IMC COM CATEGORIZAÇÃO
# ENTREGA ATÉ 04/09/2025

# FAZER UM FORK E UM PULL REQUEST PARA ENTREGAR
# pietro santos 
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("abaixo do peso: ")
elif imc < 24.9:
    print("peso normal: ")
elif imc < 24.9:
    print("sobre peso: ")
elif imc < 34.9:
    print("obesidade grau 1: ")
elif imc < 39.9:  
    print("obesidade grau: 2")
else: 
    print("obesidade grau: 3")