print("Tienda")


print("\n seleccione el numero del mes") 
print("_________________________________________") 

print("___________MENU DE OPCIONES______________") 
print("____ 1  ..... enero _____________________") 
print("____ 2  ..... febrero____________________") 
print("____ 3  ..... marzo _____________________") 
print("____ 4  ..... abril _____________________") 
print("____ 5  ..... mayo_______________________") 
print("____ 6  ..... junio______________________") 
print("____ 7  ..... julio______________________") 
print("____ 8  ..... agosto ____________________") 
print("____ 9  ..... septiembre_________________") 
print("____ 10  .....octubre____________________") 
print("____ 11 ..... noviembre__________________") 
print("____ 12  .....diciembre__________________") 

mes = int(input("\nDijite el numero correspondiente al mes: "))
importe = int(input("Dijite el importe correspondiente: "))

def enero():
	print("en el mes de enero usted debe pagar: " ,importe)

def febrero():
	print("en el mes de febrero usted debe pagar: " ,importe)

def marzo():
	print("en el mes de marzo usted debe pagar: " ,importe)

def abril():
	print("en el mes de abril usted debe pagar: " ,importe)

def mayo():
	print("en el mes de mayo usted debe pagar: " ,importe)

def junio():
	print("en el mes de junio usted debe pagar: " ,importe)

def julio():
	print("en el mes de julio usted debe pagar: " ,importe)

def agosto():
	print("en el mes de agosto usted debe pagar: " ,importe)

def septiembre():
	print("en el mes de septiembre usted debe pagar: " ,importe)

def octubre():
    descuento = importe * 0.15
    total = importe - descuento
    print("en el mes octubre de usted debe pagar con el descunto: " ,total)

def noviembre():
	print("en el mes noviembre de usted debe pagar: " ,importe)

def diciembre():
	print("en el mes de diciembre usted debe pagar: " ,importe)

def error():
	print('error')

switch_semana = {
	1: enero,
	2: febrero,
	3: marzo,
	4: abril,
	5: mayo,
	6: junio,
	7: julio,
    8: agosto,
	9: septiembre,
	10: octubre,
	11: noviembre,
    12: diciembre
}

#tomamos la función asociada a la variable y la invocamos
switch_semana.get(mes, error)()