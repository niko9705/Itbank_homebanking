#print(f'El num de cheque es: {}')

nroDeCheque = int(input("Ingrese número de cheque"))
CodigoBanco = int(input('Ingrese el código del banco que figura en la parte superior del cheque'))
CodigoSucursal = int(input("Ingrese el código que figura en la parte inferior del cheque"))
NumeroCuentaOrigen = int(input("Ingrese el número de cuenta al que pertenezca"))
NumeroCuentaDestino = int(input("Ingrese el número de la cuenta destinatario "))
FechaPago = 110722
Valor = int(input("Ingrese un valor"))

FechaOrigen = int(input("Ingrese la fecha origen del cheque")) 

DNI = int(input("Ingrese el DNI"))

FechaPago = int(input("Ingrese una fecha de pago"))

if FechaPago == 110722:
    print("El cheque ha sido aprobado y fue emitido")
    
elif FechaPago > 110722:
     print("El cheque no ha sido emitido, por lo tanto el cheque está pendiente pago")
     

    

