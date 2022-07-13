#print(f'El num de cheque es: {}')

nroDeCheque = int(input("Ingrese número de cheque"))
CodigoBanco = int(input('Ingrese el código del banco que figura en la parte superior del cheque'))
CodigoSucursal = int(input("Ingrese el código que figura en la parte inferior del cheque"))
NumeroCuentaOrigen = int(input("Ingrese el número de cuenta al que pertenezca"))
NumeroCuentaDestino = int(input("Ingrese el número de la cuenta destinatario "))
Valor = int(input("Ingrese un valor"))

FechaOrigen = int(input("Ingrese la fecha origen del cheque")) 

DNI = int(input("Ingrese el DNI"))

FechaPago = int(input("Ingrese una fecha de pago"))

FechaFinal = FechaPago + 30 
FechaDeposito = int(input('Ingrese la fecha de depósito'))

if (FechaPago <= FechaDeposito <= FechaFinal):
    print("El cheque ha sido emitido y aprobado")
elif (FechaDeposito < FechaPago):
    print("El cheque ha sido emitido pero todavía no puede ser depositado")
else:
    print("El cheque ya no puede ser depositado") #La fecha de depósito es mayor a la fecha final y por lo tanto se pasaron los 30 días


