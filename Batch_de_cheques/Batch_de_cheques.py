import csv
import sys

PATH_CHEQUES = "Batch_de_cheques//cheques.csv"
argumentos = sys.argv[1:]
#para leer los argumentos (los imprime por pantalla en forma de lista)


def lectura():
    with open(PATH_CHEQUES) as archivo:
        cheques = csv.DictReader(archivo)  ##lector de diccionarios (convierte cada linea del archivo csv en un diccionario)
        for cheque in cheques:
            if(cheque['DNI'] == argumentos[0] and cheque['Tipo'] == argumentos[2] and cheque['Estado'] == argumentos[3]):
                if(argumentos[1] == 'PANTALLA'):
                    print(f"Número de cheque: {cheque['NroCheque']}\nCódigo de banco: {cheque['CodigoBanco']}\nCódigo de sucursal: {cheque['CodigoSucursal']}\nNúmero de cuenta de origen: {cheque['NumeroCuentaOrigen']}\nNúmero de cuenta de destino: {cheque['NumeroCuentaDestino']}\nValor: {cheque['Valor']}\nFecha de origen: {cheque['FechaOrigen']}\nFecha de pago: {cheque['FechaPago']}\nDNI: {cheque['DNI']}\nTipo: {cheque['Tipo']}\nEstado: {cheque['Estado']}")
                elif(argumentos[1] == 'CSV'):
                    with open(f"{cheque['DNI']}_{cheque['FechaPago']}.csv", "w", newline="") as archivocsv:
                        cheques.writer = csv.DictWriter(archivocsv, fieldnames = ["NroCheque","CodigoBanco","CodigoSucursal","NumeroCuentaOrigen","NumeroCuentaDestino","Valor","FechaOrigen","FechaPago","DNI","Tipo","Estado"])
                        cheques.writer.writeheader()
                        cheques.writerow(cheque)
                    #va el codigo para armar el cheque en formato CSV
#para encontrar el archivo hay que escribir Batch_de_cheques//Batch_de_cheques.py

lectura()









#print(f'El num de cheque es: {}')

#nroDeCheque = int(input("Ingrese número de cheque"))
#CodigoBanco = int(input('Ingrese el código del banco que figura en la parte superior del cheque'))
#CodigoSucursal = int(input("Ingrese el código que figura en la parte inferior del cheque"))
#NumeroCuentaOrigen = int(input("Ingrese el número de cuenta al que pertenezca"))
#NumeroCuentaDestino = int(input("Ingrese el número de la cuenta destinatario "))
#Valor = int(input("Ingrese un valor"))

#FechaOrigen = int(input("Ingrese la fecha origen del cheque")) 

#DNI = int(input("Ingrese el DNI"))

#FechaPago = int(input("Ingrese una fecha de pago"))

#FechaFinal = FechaPago + 30 
#FechaDeposito = int(input('Ingrese la fecha de depósito'))

#if (FechaPago <= FechaDeposito <= FechaFinal):
#    print("El cheque ha sido emitido y aprobado")
#elif (FechaDeposito < FechaPago):
#    print("El cheque ha sido emitido pero todavía no puede ser depositado")
#else:
#    print("El cheque ya no puede ser depositado") #La fecha de depósito es mayor a la fecha final y por lo tanto se pasaron los 30 días


