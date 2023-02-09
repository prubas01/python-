print("suma desendente")

## se crea la variable numero con el valor finl de la suma
# y se inicializa la suma en cero
numeros = 100
suma=0

# cuando numero sea menor a cero el ciclo se detrendra
while(numeros >0):

    # se toma la suma del primer valor 100 + 0
    # en la segunda iteraccion el ciclo ya habra restado una unidad a 100
    # ahora numeros = 99 y suma toma el valor de la primera suma =100
    # sindo suma = 100 + 99.
    # asi sucecivamente hasta que numeros sea = -1 donde se terminara la iteraccion
    # y entregrara el resultado 
    suma = numeros + suma 
    numeros = numeros - 1

# muestra el resultado en pantalla
print("La suma es : ",suma)