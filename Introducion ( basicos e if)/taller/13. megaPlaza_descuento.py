print("\nalmacen Mega Plaza")

valor_compra = int(input("\nDigite el valor de su compra: "))

if(valor_compra >= 300):
    descuento = valor_compra * 0.2
    valor_final = valor_compra - descuento
    print("\nel descuento fue(",descuento,") y el valor a pagar es: " , valor_final)

else: 
    print("\nLo sentimos no puede acceder al descuento el valor a pagar es: " , valor_compra)