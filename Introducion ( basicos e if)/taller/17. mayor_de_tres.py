print("\nmayor de 3 numeros")

a = int(input("\ndigite el primer numero: "))
b = int(input("digite el segundo numero: "))
c = int(input("digite el tercer numero: "))

if((a>b)&(a>c)):
    print("\nEl mayor numero es el primero: ",a)

if((b>a)&(b>c)):
    print("El mayor numero es el segundo: ",b)

if((c>a)&(c>b)):
    print("El mayor numero es el tercero: ",c)