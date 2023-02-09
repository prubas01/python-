print("\nCalculadora de salario")

horas_trabajo = int (input("Digite las horas de trabajo: "))

if(horas_trabajo <= 40):
    pago = horas_trabajo * 20000

    print("Su pago es: $",pago)
else:
    horas_extra = horas_trabajo-40
    pago_extra = horas_extra * 25000

    Pago_hora = (horas_trabajo - horas_extra) * 19000

    pago = Pago_hora + pago_extra

    print("Su pago es: $",pago)