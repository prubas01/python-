import math
print("\ncalculo de la raiz cuadrada")

numero = int(input("Digite un numero: "))

if(numero < 0):
    print("error")
elif(numero > 0):
    print("el cuadrado es: ",math.sqrt(numero))