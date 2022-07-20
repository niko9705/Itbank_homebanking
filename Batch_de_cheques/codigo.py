import csv
import sys

cheque= 
NroCheque= {[5268:4995]}
CodigoBanco=""
CodigoSucursal=""
NumeroCuentaOrigen=""
NumeroCuentaDestino=""
Valor=""
FechaOrigen=""
FechaPago=""
DNI=
Tipo=""
Estado="" 
PATH_CHEQUES = "Batch_de_cheques//cheques.csv"

argumentos = sys.argv[1:]

with open('EIP.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Role']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writerheader()
    writer.writerow({argumentos[0]: cheque['Tipo'],
                     argumentos[2]: cheque['Estado'],
                     argumentos[3]: 'PANTALLA'})
    print(f"Número de cheque: {cheque['NroCheque']}\nCódigo de banco: {cheque['CodigoBanco']}\nCódigo de sucursal: {cheque['CodigoSucursal']}\nNúmero de cuenta de origen: {cheque['NumeroCuentaOrigen']}\nNúmero de cuenta de destino: {cheque['NumeroCuentaDestino']}\nValor: {cheque['Valor']}\nFecha de origen: {cheque['FechaOrigen']}\nFecha de pago: {cheque['FechaPago']}\nDNI: {cheque['DNI']}\nTipo: {cheque['Tipo']}\nEstado: {cheque['Estado']}")
    
    if(argumentos[1] == 'CSV'):
                    with open(f"{cheque['DNI']}_{cheque['FechaPago']}.csv", "w", newline="") as archivocsv:
                        cheques.writer = csv.DictWriter(archivocsv, fieldnames = ["NroCheque","CodigoBanco","CodigoSucursal","NumeroCuentaOrigen","NumeroCuentaDestino","Valor","FechaOrigen","FechaPago","DNI","Tipo","Estado"])
                        cheques.writer.writeheader()
                        cheques.writerow(cheque)
 
print('Datos insertados')