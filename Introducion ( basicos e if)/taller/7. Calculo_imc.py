

print("\ncalculadora de imc\n")

print("para calcular necesitamos los sigientes datos masa y altura")

masa = float(input("\ndigite su masa en kilogramos: "))
altura = float(input("digite su altura en metros: "))

imc = masa / pow(altura, 2)

if (imc < 18.5):
    print("Su imc(",imc,") lo define con un peso bajo")

if((imc >= 18.5) & (imc < 25)):
    print("Su imc(",imc,") lo define con un peso ideal")

if((imc >= 25) & (imc < 30)):
    print("Su imc(",imc,") lo define con un sobrepeso")

if((imc >= 30) & (imc < 35)):
    print("Su imc(",imc,") lo define con obesidad")

if((imc >= 35) & (imc < 40)):
    print("Su imc(",imc,") lo define con obesidad severa")


if((imc >= 40)):
    print("Su imc(",imc,") lo define con obesidad morvida")