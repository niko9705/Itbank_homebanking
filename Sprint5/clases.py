import json
from operator import index
import os
#Las funciones cargar_datos cargan los datos del JSON

classic = {}
gold = {}
black = {}

def razon_de_transacciones_rechazadas_classic(classic):
    if(classic['transacciones'][1]):
        print('se ha excedido del cupo diario restante y del monto máximo')
    elif(classic['transacciones'][2]):
        print('se ha excedido del cupo diario restante')
    elif(classic['transacciones'][3]):
        print('se ha excedido del cupo diario restante')
    elif(classic['transacciones'][4]):
        print('no está permitido poseer tarjeta de crédito')
    elif(classic['transacciones'][5]):
        print('no está permitido poseer chequera')
    elif(classic['transacciones'][6]):
        print('no está permitida la compra de dólares')
    elif(classic['transacciones'][7]):
        print('se ha excedido del monto máximo')
    elif(classic['transacciones'][9]):
        print('se ha excedido del monto máximo')

def razon_de_transacciones_rechazadas_gold(gold):
    if(gold['transacciones'][1]):
        print('Se ha excedido del monto que posee en su cuenta')
    elif(gold['transacciones'][2]):
        print('se ha excedido del cupo diario restante')
    elif(gold['transacciones'][3]):
        print('se ha excedido del cupo diario restante')
    elif(gold['transacciones'][4]):
        print('no está permitido poseer tarjeta de crédito')
    elif(gold['transacciones'][5]):
        print('Se ha excedido del cupo diario restante')
    elif(gold['transacciones'][6]):
        print('Se ha excedido del monto que posee en su cuenta y de su cupo diario restante')
    elif(gold['transacciones'][7]):
        print('se ha excedido del cupo diario restante')
    elif(gold['transacciones'][9]):
        print('Se ha excedido del monto que posee en su cuenta')
        
def razon_de_transacciones_rechazadas_black(black):
    if(black['transacciones'][1]):
        print('Se ha excedido del cupo diario restante')
    elif(black['transacciones'][2]):
        print('se ha excedido del cupo diario restante')
    elif(black['transacciones'][3]):
        print('se ha excedido del cupo diario restante')
    elif(black['transacciones'][4]):
        print('Se ha excedido del cupo diario restante')
    elif(black['transacciones'][5]):
        print('Se ha excedido del cupo diario restante')
    elif(black['transacciones'][6]):
        print('Se ha excedido del cupo diario restante')
    elif(black['transacciones'][7]):
        print('se ha excedido del monto máximo')

def estado_de_transacciones_classic(classic):
    print("\n\nTRANSACCIONES ACEPTADAS Y RECHAZADAS:")
    for ordenDeTransaccion in classic['transacciones']:
        if(ordenDeTransaccion['estado'] == 'ACEPTADA'):
            print('La transacción ha sido ACEPTADA')
        else:
            print(f'La transaccion ha sido RECHAZADA porque {razon_de_transacciones_rechazadas_classic(classic)}')
        

def estado_de_transacciones_gold(gold):
    print("\n\nTRANSACCIONES ACEPTADAS Y RECHAZADAS")
    for ordenDeTransaccion in gold['transacciones']:
        if(ordenDeTransaccion['estado'] == 'ACEPTADA'):
            print('La transacción ha sido ACEPTADA')
        else:
            print(f'La transaccion ha sido RECHAZADA porque {razon_de_transacciones_rechazadas_gold(gold)}')


def estado_de_transacciones_black(black):
    print("\n\nTRANSACCIONES ACEPTADAS Y RECHAZADAS")
    for ordenDeTransaccion in black['transacciones']:
        if(ordenDeTransaccion['estado'] == 'ACEPTADA'):
            print('La transacción ha sido ACEPTADA')
        else:
            print(f'La transaccion ha sido RECHAZADA porque {razon_de_transacciones_rechazadas_black(black)}')
#Tengo que ver cómo hacer para que las funciones me tomen el classic[''][0]['tipo'] como un valor JSON y no como un string
#En estas funciones no es necesario mostrar el nombre, apellido, numero, dni, ni direccion porque ya se muestran
#con el método __str__ de la clase cliente

#La idea es que las funciones clargar_datos muestren los datos de las transacciones y llamen a otras funciones 
#que analicen dichos datos y dependiendo de si figuran como APROBADOS o RECHAZADOS digan por qué lo fueron

def cargar_datos_classic(ruta):
    with open(ruta) as contenido:
        classic = json.load(contenido)
        del(classic['numero'])
        del(classic['nombre'])
        del(classic['apellido'])
        del(classic['dni'])
        del(classic['tipo'])
        del(classic['direccion'])
        print(f"\nTransacción 1:\nEstado: {classic['transacciones'][0]['estado']}\
            \nTipo: {classic['transacciones'][0]['tipo']}\nNúmero de cuenta: {classic['transacciones'][0]['cuentaNumero']}\nCupo diario restante: {classic['transacciones'][0]['cupoDiarioRestante']}\nCantidad de extracciones hechas: {classic['transacciones'][0]['cantidadExtraccionesHechas']}\nMonto: {classic['transacciones'][0]['monto']}\nFecha: {classic['transacciones'][0]['fecha']}\nNúmero: {classic['transacciones'][0]['numero']}\nSaldo en cuenta: {classic['transacciones'][0]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {classic['transacciones'][0]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {classic['transacciones'][0]['totalChequerasActualmente']}\
            \n\nTransacción 2:\nEstado: {classic['transacciones'][1]['estado']}\nRazón: Se ha excedido del cupo diario restante y del monto máximo\nTipo: {classic['transacciones'][1]['tipo']}\nNúmero de cuenta: {classic['transacciones'][1]['cuentaNumero']}\nCupo diario restante: {classic['transacciones'][1]['cupoDiarioRestante']}\nMonto: {classic['transacciones'][1]['monto']}\nFecha: {classic['transacciones'][1]['fecha']}\nNúmero: {classic['transacciones'][1]['numero']}\nSaldo en cuenta: {classic['transacciones'][1]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {classic['transacciones'][1]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {classic['transacciones'][1]['totalChequerasActualmente']}\
            \n\nTransacción 3:\nEstado: {classic['transacciones'][2]['estado']}\nRazón: Se ha excedido del cupo diario restante\nTipo: {classic['transacciones'][2]['tipo']}\nNúmero de cuenta: {classic['transacciones'][2]['cuentaNumero']}\nCupo diario restante: {classic['transacciones'][2]['cupoDiarioRestante']}\nMonto: {classic['transacciones'][2]['monto']}\nFecha: {classic['transacciones'][2]['fecha']}\nNúmero: {classic['transacciones'][2]['numero']}\nSaldo en cuenta: {classic['transacciones'][2]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {classic['transacciones'][2]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {classic['transacciones'][2]['totalChequerasActualmente']}\
            \n\nTransacción 4:\nEstado: {classic['transacciones'][3]['estado']}\nRazón: Se ha excedido del cupo diario restante\nTipo: {classic['transacciones'][3]['tipo']}\nNúmero de cuenta: {classic['transacciones'][3]['cuentaNumero']}\nCupo diario restante: {classic['transacciones'][3]['cupoDiarioRestante']}\nMonto: {classic['transacciones'][3]['monto']}\nFecha: {classic['transacciones'][3]['fecha']}\nNúmero: {classic['transacciones'][3]['numero']}\nSaldo en cuenta: {classic['transacciones'][3]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {classic['transacciones'][3]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {classic['transacciones'][3]['totalChequerasActualmente']}\
            \n\nTransacción 5:\nEstado: {classic['transacciones'][4]['estado']}\nRazón: No está permitido poseer tarjeta de crédito\nTipo: {classic['transacciones'][4]['tipo']}\nNúmero de cuenta: {classic['transacciones'][4]['cuentaNumero']}\nCupo diario restante: {classic['transacciones'][4]['cupoDiarioRestante']}\nMonto: {classic['transacciones'][4]['monto']}\nFecha: {classic['transacciones'][4]['fecha']}\nNúmero: {classic['transacciones'][4]['numero']}\nSaldo en cuenta: {classic['transacciones'][4]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {classic['transacciones'][4]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {classic['transacciones'][4]['totalChequerasActualmente']}\
            \n\nTransacción 6:\nEstado: {classic['transacciones'][5]['estado']}\nRazón: No está permitido poseer chequera\nTipo: {classic['transacciones'][5]['tipo']}\nNúmero de cuenta: {classic['transacciones'][5]['cuentaNumero']}\nCupo diario restante: {classic['transacciones'][5]['cupoDiarioRestante']}\nMonto: {classic['transacciones'][5]['monto']}\nFecha: {classic['transacciones'][5]['fecha']}\nNúmero: {classic['transacciones'][5]['numero']}\nSaldo en cuenta: {classic['transacciones'][5]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {classic['transacciones'][5]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {classic['transacciones'][5]['totalChequerasActualmente']}\
            \n\nTransacción 7:\nEstado: {classic['transacciones'][6]['estado']}\nRazón: No está permitida la compra de dólares\nTipo: {classic['transacciones'][6]['tipo']}\nNúmero de cuenta: {classic['transacciones'][6]['cuentaNumero']}\nCupo diario restante: {classic['transacciones'][6]['cupoDiarioRestante']}\nMonto: {classic['transacciones'][6]['monto']}\nFecha: {classic['transacciones'][6]['fecha']}\nNúmero: {classic['transacciones'][6]['numero']}\nSaldo en cuenta: {classic['transacciones'][6]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {classic['transacciones'][6]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {classic['transacciones'][6]['totalChequerasActualmente']}\
            \n\nTransacción 8:\nEstado: {classic['transacciones'][7]['estado']}\nRazón: Se ha excedido del monto máximo\nTipo: {classic['transacciones'][7]['tipo']}\nNúmero de cuenta: {classic['transacciones'][7]['cuentaNumero']}\nCupo diario restante: {classic['transacciones'][7]['cupoDiarioRestante']}\nMonto: {classic['transacciones'][7]['monto']}\nFecha: {classic['transacciones'][7]['fecha']}\nNúmero: {classic['transacciones'][7]['numero']}\nSaldo en cuenta: {classic['transacciones'][7]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {classic['transacciones'][7]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {classic['transacciones'][7]['totalChequerasActualmente']}\
            \n\nTransacción 9:\nEstado: {classic['transacciones'][8]['estado']}\nTipo: {classic['transacciones'][8]['tipo']}\nNúmero de cuenta: {classic['transacciones'][8]['cuentaNumero']}\nCupo diario restante: {classic['transacciones'][8]['cupoDiarioRestante']}\nMonto: {classic['transacciones'][8]['monto']}\nFecha: {classic['transacciones'][8]['fecha']}\nNúmero: {classic['transacciones'][8]['numero']}\nSaldo en cuenta: {classic['transacciones'][8]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {classic['transacciones'][8]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {classic['transacciones'][8]['totalChequerasActualmente']}\
            \n\nTransacción 10:\nEstado: {classic['transacciones'][9]['estado']}\nRazón: Se ha excedido del monto máximo\nTipo: {classic['transacciones'][9]['tipo']}\nNúmero de cuenta: {classic['transacciones'][9]['cuentaNumero']}\nCupo diario restante: {classic['transacciones'][9]['cupoDiarioRestante']}\nMonto: {classic['transacciones'][9]['monto']}\nFecha: {classic['transacciones'][9]['fecha']}\nNúmero: {classic['transacciones'][9]['numero']}\nSaldo en cuenta: {classic['transacciones'][9]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {classic['transacciones'][9]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {classic['transacciones'][9]['totalChequerasActualmente']}")
        #print(estado_de_transacciones_classic(classic))

def cargar_datos_gold(ruta):
    with open(ruta) as contenido:
        gold = json.load(contenido)
        del(gold['numero'])
        del(gold['nombre'])
        del(gold['apellido'])
        del(gold['dni'])
        del(gold['tipo'])
        del(gold['direccion'])
        print(f"\nTransacción 1:\nEstado: {gold['transacciones'][0]['estado']}\nTipo: {gold['transacciones'][0]['tipo']}\nNúmero de cuenta: {gold['transacciones'][0]['cuentaNumero']}\nCupo diario restante: {gold['transacciones'][0]['cupoDiarioRestante']}\nCantidad de extracciones hechas: {gold['transacciones'][0]['cantidadExtraccionesHechas']}\nMonto: {gold['transacciones'][0]['monto']}\nFecha: {gold['transacciones'][0]['fecha']}\nNúmero: {gold['transacciones'][0]['numero']}\nSaldo en cuenta: {gold['transacciones'][0]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {gold['transacciones'][0]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {gold['transacciones'][0]['totalChequerasActualmente']}\
            \n\nTransacción 2:\nEstado: {gold['transacciones'][1]['estado']}\nRazón: Se ha excedido del monto que posee en su cuenta\nTipo: {gold['transacciones'][1]['tipo']}\nNúmero de cuenta: {gold['transacciones'][1]['cuentaNumero']}\nCupo diario restante: {gold['transacciones'][1]['cupoDiarioRestante']}\nMonto: {gold['transacciones'][1]['monto']}\nFecha: {gold['transacciones'][1]['fecha']}\nNúmero: {gold['transacciones'][1]['numero']}\nSaldo en cuenta: {gold['transacciones'][1]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {gold['transacciones'][1]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {gold['transacciones'][1]['totalChequerasActualmente']}\
            \n\nTransacción 3:\nEstado: {gold['transacciones'][2]['estado']}\nRazón: Se ha excedido del cupo diario restante\nTipo: {gold['transacciones'][2]['tipo']}\nNúmero de cuenta: {gold['transacciones'][2]['cuentaNumero']}\nCupo diario restante: {gold['transacciones'][2]['cupoDiarioRestante']}\nMonto: {gold['transacciones'][2]['monto']}\nFecha: {gold['transacciones'][2]['fecha']}\nNúmero: {gold['transacciones'][2]['numero']}\nSaldo en cuenta: {gold['transacciones'][2]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {gold['transacciones'][2]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {gold['transacciones'][2]['totalChequerasActualmente']}\
            \n\nTransacción 4:\nEstado: {gold['transacciones'][3]['estado']}\nRazón: Se ha excedido del cupo diario restante\nTipo: {gold['transacciones'][3]['tipo']}\nNúmero de cuenta: {gold['transacciones'][3]['cuentaNumero']}\nCupo diario restante: {gold['transacciones'][3]['cupoDiarioRestante']}\nMonto: {gold['transacciones'][3]['monto']}\nFecha: {gold['transacciones'][3]['fecha']}\nNúmero: {gold['transacciones'][3]['numero']}\nSaldo en cuenta: {gold['transacciones'][3]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {gold['transacciones'][3]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {gold['transacciones'][3]['totalChequerasActualmente']}\
            \n\nTransacción 5:\nEstado: {gold['transacciones'][4]['estado']}\nRazón: No está permitido poseer tarjeta de crédito\nTipo: {gold['transacciones'][4]['tipo']}\nNúmero de cuenta: {gold['transacciones'][4]['cuentaNumero']}\nCupo diario restante: {gold['transacciones'][4]['cupoDiarioRestante']}\nMonto: {gold['transacciones'][4]['monto']}\nFecha: {gold['transacciones'][4]['fecha']}\nNúmero: {gold['transacciones'][4]['numero']}\nSaldo en cuenta: {gold['transacciones'][4]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {gold['transacciones'][4]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {gold['transacciones'][4]['totalChequerasActualmente']}\
            \n\nTransacción 6:\nEstado: {gold['transacciones'][5]['estado']}\nRazón: Se ha excedido del cupo diario restante\nTipo: {gold['transacciones'][5]['tipo']}\nNúmero de cuenta: {gold['transacciones'][5]['cuentaNumero']}\nCupo diario restante: {gold['transacciones'][5]['cupoDiarioRestante']}\nMonto: {gold['transacciones'][5]['monto']}\nFecha: {gold['transacciones'][5]['fecha']}\nNúmero: {gold['transacciones'][5]['numero']}\nSaldo en cuenta: {gold['transacciones'][5]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {gold['transacciones'][5]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {gold['transacciones'][5]['totalChequerasActualmente']}\
            \n\nTransacción 7:\nEstado: {gold['transacciones'][6]['estado']}\nRazón: Se ha excedido del monto que posee en su cuenta y de su cupo diario restante\nTipo: {gold['transacciones'][6]['tipo']}\nNúmero de cuenta: {gold['transacciones'][6]['cuentaNumero']}\nCupo diario restante: {gold['transacciones'][6]['cupoDiarioRestante']}\nMonto: {gold['transacciones'][6]['monto']}\nFecha: {gold['transacciones'][6]['fecha']}\nNúmero: {gold['transacciones'][6]['numero']}\nSaldo en cuenta: {gold['transacciones'][6]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {gold['transacciones'][6]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {gold['transacciones'][6]['totalChequerasActualmente']}\
            \n\nTransacción 8:\nEstado: {gold['transacciones'][7]['estado']}\nRazón: Se ha excedido del cupo diario restante\nTipo: {gold['transacciones'][7]['tipo']}\nNúmero de cuenta: {gold['transacciones'][7]['cuentaNumero']}\nCupo diario restante: {gold['transacciones'][7]['cupoDiarioRestante']}\nMonto: {gold['transacciones'][7]['monto']}\nFecha: {gold['transacciones'][7]['fecha']}\nNúmero: {gold['transacciones'][7]['numero']}\nSaldo en cuenta: {gold['transacciones'][7]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {gold['transacciones'][7]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {gold['transacciones'][7]['totalChequerasActualmente']}\
            \n\nTransacción 9:\nEstado: {gold['transacciones'][8]['estado']}\nTipo: {gold['transacciones'][8]['tipo']}\nNúmero de cuenta: {gold['transacciones'][8]['cuentaNumero']}\nCupo diario restante: {gold['transacciones'][8]['cupoDiarioRestante']}\nMonto: {gold['transacciones'][8]['monto']}\nFecha: {gold['transacciones'][8]['fecha']}\nNúmero: {gold['transacciones'][8]['numero']}\nSaldo en cuenta: {gold['transacciones'][8]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {gold['transacciones'][8]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {gold['transacciones'][8]['totalChequerasActualmente']}\
            \n\nTransacción 10:\nEstado: {gold['transacciones'][9]['estado']}\nRazón: Se ha excedido del monto que posee en su cuenta\nTipo: {gold['transacciones'][9]['tipo']}\nNúmero de cuenta: {gold['transacciones'][9]['cuentaNumero']}\nCupo diario restante: {gold['transacciones'][9]['cupoDiarioRestante']}\nMonto: {gold['transacciones'][9]['monto']}\nFecha: {gold['transacciones'][9]['fecha']}\nNúmero: {gold['transacciones'][9]['numero']}\nSaldo en cuenta: {gold['transacciones'][9]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {gold['transacciones'][9]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {gold['transacciones'][9]['totalChequerasActualmente']}")
        #print(estado_de_transacciones_gold(gold))

def cargar_datos_black(ruta):
    with open(ruta) as contenido:
        black = json.load(contenido)
        del(black['numero'])
        del(black['nombre'])
        del(black['apellido'])
        del(black['dni'])
        del(black['tipo'])
        del(black['direccion'])
        print(f"\nTransacción 1:\nEstado: {black['transacciones'][0]['estado']}\nTipo: {black['transacciones'][0]['tipo']}\nNúmero de cuenta: {black['transacciones'][0]['cuentaNumero']}\nCupo diario restante: {black['transacciones'][0]['cupoDiarioRestante']}\nCantidad de extracciones hechas: {black['transacciones'][0]['cantidadExtraccionesHechas']}\nMonto: {black['transacciones'][0]['monto']}\nFecha: {black['transacciones'][0]['fecha']}\nNúmero: {black['transacciones'][0]['numero']}\nSaldo en cuenta: {black['transacciones'][0]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {black['transacciones'][0]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {black['transacciones'][0]['totalChequerasActualmente']}\
            \n\nTransacción 2:\nEstado: {black['transacciones'][1]['estado']}\nRazón: Se ha excedido del cupo diario restante\nTipo: {black['transacciones'][1]['tipo']}\nNúmero de cuenta: {black['transacciones'][1]['cuentaNumero']}\nCupo diario restante: {black['transacciones'][1]['cupoDiarioRestante']}\nMonto: {black['transacciones'][1]['monto']}\nFecha: {black['transacciones'][1]['fecha']}\nNúmero: {black['transacciones'][1]['numero']}\nSaldo en cuenta: {black['transacciones'][1]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {black['transacciones'][1]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {black['transacciones'][1]['totalChequerasActualmente']}\
            \n\nTransacción 3:\nEstado: {black['transacciones'][2]['estado']}\nRazón: Se ha excedido del cupo diario restante\nTipo: {black['transacciones'][2]['tipo']}\nNúmero de cuenta: {black['transacciones'][2]['cuentaNumero']}\nCupo diario restante: {black['transacciones'][2]['cupoDiarioRestante']}\nMonto: {black['transacciones'][2]['monto']}\nFecha: {black['transacciones'][2]['fecha']}\nNúmero: {black['transacciones'][2]['numero']}\nSaldo en cuenta: {black['transacciones'][2]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {black['transacciones'][2]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {black['transacciones'][2]['totalChequerasActualmente']}\
            \n\nTransacción 4:\nEstado: {black['transacciones'][3]['estado']}\nRazón: Se ha excedido del cupo diario restante\nTipo: {black['transacciones'][3]['tipo']}\nNúmero de cuenta: {black['transacciones'][3]['cuentaNumero']}\nCupo diario restante: {black['transacciones'][3]['cupoDiarioRestante']}\nMonto: {black['transacciones'][3]['monto']}\nFecha: {black['transacciones'][3]['fecha']}\nNúmero: {black['transacciones'][3]['numero']}\nSaldo en cuenta: {black['transacciones'][3]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {black['transacciones'][3]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {black['transacciones'][3]['totalChequerasActualmente']}\
            \n\nTransacción 5:\nEstado: {black['transacciones'][4]['estado']}\nRazón: Se ha excedido del cupo diario restante\nTipo: {black['transacciones'][4]['tipo']}\nNúmero de cuenta: {black['transacciones'][4]['cuentaNumero']}\nCupo diario restante: {black['transacciones'][4]['cupoDiarioRestante']}\nMonto: {black['transacciones'][4]['monto']}\nFecha: {black['transacciones'][4]['fecha']}\nNúmero: {black['transacciones'][4]['numero']}\nSaldo en cuenta: {black['transacciones'][4]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {black['transacciones'][4]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {black['transacciones'][4]['totalChequerasActualmente']}\
            \n\nTransacción 6:\nEstado: {black['transacciones'][5]['estado']}\nRazón: Se ha excedido del cupo diario restante\nTipo: {black['transacciones'][5]['tipo']}\nNúmero de cuenta: {black['transacciones'][5]['cuentaNumero']}\nCupo diario restante: {black['transacciones'][5]['cupoDiarioRestante']}\nMonto: {black['transacciones'][5]['monto']}\nFecha: {black['transacciones'][5]['fecha']}\nNúmero: {black['transacciones'][5]['numero']}\nSaldo en cuenta: {black['transacciones'][5]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {black['transacciones'][5]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {black['transacciones'][5]['totalChequerasActualmente']}\
            \n\nTransacción 7:\nEstado: {black['transacciones'][6]['estado']}\nRazón: Se ha excedido del cupo diario restante\nTipo: {black['transacciones'][6]['tipo']}\nNúmero de cuenta: {black['transacciones'][6]['cuentaNumero']}\nCupo diario restante: {black['transacciones'][6]['cupoDiarioRestante']}\nMonto: {black['transacciones'][6]['monto']}\nFecha: {black['transacciones'][6]['fecha']}\nNúmero: {black['transacciones'][6]['numero']}\nSaldo en cuenta: {black['transacciones'][6]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {black['transacciones'][6]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {black['transacciones'][6]['totalChequerasActualmente']}\
            \n\nTransacción 8:\nEstado: {black['transacciones'][7]['estado']}\nRazón: Se ha excedido del monto máximo\nTipo: {black['transacciones'][7]['tipo']}\nNúmero de cuenta: {black['transacciones'][7]['cuentaNumero']}\nCupo diario restante: {black['transacciones'][7]['cupoDiarioRestante']}\nMonto: {black['transacciones'][7]['monto']}\nFecha: {black['transacciones'][7]['fecha']}\nNúmero: {black['transacciones'][7]['numero']}\nSaldo en cuenta: {black['transacciones'][7]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {black['transacciones'][7]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {black['transacciones'][7]['totalChequerasActualmente']}\
            \n\nTransacción 9:\nEstado: {black['transacciones'][8]['estado']}\nTipo: {black['transacciones'][8]['tipo']}\nNúmero de cuenta: {black['transacciones'][8]['cuentaNumero']}\nCupo diario restante: {black['transacciones'][8]['cupoDiarioRestante']}\nMonto: {black['transacciones'][8]['monto']}\nFecha: {black['transacciones'][8]['fecha']}\nNúmero: {black['transacciones'][8]['numero']}\nSaldo en cuenta: {black['transacciones'][8]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {black['transacciones'][8]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {black['transacciones'][8]['totalChequerasActualmente']}\
            \n\nTransacción 10:\nEstado: {black['transacciones'][9]['estado']}\nTipo: {black['transacciones'][9]['tipo']}\nNúmero de cuenta: {black['transacciones'][9]['cuentaNumero']}\nCupo diario restante: {black['transacciones'][9]['cupoDiarioRestante']}\nMonto: {black['transacciones'][9]['monto']}\nFecha: {black['transacciones'][9]['fecha']}\nNúmero: {black['transacciones'][9]['numero']}\nSaldo en cuenta: {black['transacciones'][9]['saldoEnCuenta']}\nTotal de tarjetas de crédito actualmente: {black['transacciones'][9]['totalTarjetasDeCreditoActualmente']}\nTotal de chequeras actualmente: {black['transacciones'][9]['totalChequerasActualmente']}")
        #print(estado_de_transacciones_black(black))


nombre = input('Ingrese el nombre del cliente: ')
nCliente = int(input('Ingrese el número del cliente: '))
dni = int(input('Ingrese el DNI del cliente: '))
tipoCliente = input('Ingrese el tipo de cliente (classic, gold o black): ')



class Cliente():
    def __init__(self, nombre, apellido, numero, dni, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni
        self.direccion = direccion
    
    def __str__(self):
        print(f"\n\nCLIENTE:\nNombre: {self.nombre}\nApellido: {self.apellido}\
            \nNúmero: {self.numero}\nDNI: {self.dni}\nDirección: {self.direccion}")

class Classic(Cliente):
    def __init__(self, nombre, apellido, numero, dni, direccion):
        super().__init__(nombre, apellido, numero, dni, direccion)
        
        self.tipo = "classic"
        self.tarjeta_debito = 1
        self.caja_ahorro_peso = 1
        self.caja_ahorro_dolar = 0
        self.compra_venta_dolar = 0
        self.retiro_maximo = 10_000
        self.tarjeta_credito = 0
        self.chequera = 0
        self.comision_transaccion = 0.01
        self.limite_transferencia = 150_000
    
    def __str__(self):
        super().__str__()
        print(f"\n\nDATOS DE UN CLIENTE CLASSIC:\nTipo: {self.tipo}\nTarjeta de débito: {self.tarjeta_debito}\nCaja de ahorro en pesos: {self.caja_ahorro_peso}\nCaja de ahorro en dólares: {self.caja_ahorro_dolar}\nCompra/venta dólar: {self.compra_venta_dolar}\nRetiro máximo: {self.retiro_maximo}\
            \nTarjeta de crédito: {self.tarjeta_credito}\nChequera: {self.chequera}\nComisión de transacción: {self.comision_transaccion}\
            \nLímite de transferencia: {self.limite_transferencia}\n\nDATOS DEL CLIENTE CONSULTADO:")
        print(cargar_datos_classic(ruta = '/Users/Note/Documents/full stack/Itbank_homebanking/Sprint5/JSON/eventos_classic.json'))

class Gold(Cliente):
    def __init__(self, nombre, apellido, numero, dni, direccion):
        super().__init__(nombre, apellido, numero, dni, direccion)
        
        self.tipo = "Gold"
        self.tarjeta_debito = 1
        self.cuenta_corriente = 1
        self.caja_ahorro_dolar = 1
        self.compra_venta_dolar = 1
        self.retiro_maximo = 20_000
        self.tarjeta_credito = 1
        self.chequera = 1
        self.comision_transaccion = 0.005
        self.limite_transferencia = 500_000
        self.monto_descubierto = 10_000

    def __str__(self):
        super().__str__()
        print(f"\n\nDATOS DE UN CLIENTE GOLD:\nTipo: {self.tipo}\nTerjeta de débito: {self.tarjeta_debito}\nCuenta corriente: {self.cuenta_corriente}\
            \nCaja de ahorro en dólares: {self.caja_ahorro_dolar}\nCompra/venta en dólares: {self.compra_venta_dolar}\nRetiro máximo: {self.retiro_maximo}\nTarjeta de crédito: {self.tarjeta_credito}\
            \nChequera: {self.chequera}\nComisión de transacción: {self.comision_transaccion}\nLímite de transferencia: {self.limite_transferencia}\nMonto descubierto: {self.monto_descubierto}\n\nDATOS DEL CLIENTE CONSULTADO:")
        print(cargar_datos_gold(ruta = '/Users/Note/Documents/full stack/Itbank_homebanking/Sprint5/JSON/eventos_gold.json'))

class Black(Cliente):
    def __init__(self, nombre, apellido, numero, dni, direccion):
        super().__init__(nombre, apellido, numero, dni, direccion)
        
        self.tipo = "Black"
        self.tarjeta_credito_maximas = 5
        self.caja_ahorro_pesos = 1
        self.cuenta_corriente_pesos = 1
        self.caja_ahorro_dolar = 1
        self.retiro_maximo = 100_000
        self.chequeras_maximas = 2
        self.comision_transaccion = 0
        self.limite_transferencia = "Sin límite"
        self.monto_descubierto = 10_000
    
    def __str__(self):
        super().__str__()
        print(f"\n\nDATOS DE UN CLIENTE BLACK:\nTipo: {self.tipo}\nTarjetas de crédito máximas: {self.tarjeta_credito_maximas}\nCaja de ahorro en pesos: {self.caja_ahorro_pesos}\nCuenta corriente en pesos: {self.cuenta_corriente_pesos}\
            \nCaja de ahorro en dólares: {self.caja_ahorro_dolar}\nRetiro máximo: {self.retiro_maximo}\nChequeras máximas: {self.chequeras_maximas}\nComisión de transacción: {self.comision_transaccion}\
            \nLímite de transferencia: {self.limite_transferencia}\nMonto descubierto: {self.monto_descubierto}\n\nDATOS DEL CLIENTE CONSULTADO:")
        print(cargar_datos_black(ruta = '/Users/Note/Documents/full stack/Itbank_homebanking/Sprint5/JSON/eventos_black.json'))


NicolasClassic = Classic(nombre = "Nicolas", apellido = "Gaston", numero = 100001, dni = 29494777, direccion = "Rivadavia 7900")
NicolasGold = Gold(nombre = "Nicolas", apellido = "Gaston", numero = 100001, dni = 29494777, direccion = "Rivadavia 7900")
NicolasBlack = Black(nombre = "Nicolas", apellido = "Gaston", numero = 100001, dni = 29494777, direccion = "Rivadavia 7900")

if(nombre == 'Nicolas' and nCliente == 100001 and dni == 29494777 and tipoCliente == 'classic'):
    NicolasClassic.__str__()
elif(nombre == 'Nicolas' and nCliente == 100001 and dni == 29494777 and tipoCliente == 'gold'):
    NicolasGold.__str__()
elif(nombre == 'Nicolas' and nCliente == 100001 and dni == 29494777 and tipoCliente == 'black'):
    NicolasBlack.__str__()
else:
    print('Lo sentimos, este cliente no existe:(. Intente de nuevo!')


folder = "/Users/Note/Documents/full stack/Itbank_homebanking/Sprint5/transacciones"
if os.path.exists(folder) == False:
    os.mkdir(folder)


html = open(folder + '\\' + nombre + '.html', 'w')

html.write('<html lang="en" dir="ltr">')
html.write('\n    <head>')
html.write('\n        <title> Datos </title>')
html.write('\n            <style>')
html.write('\n                body {')
html.write('\n                    background-size: 100%; ')
html.write('\n                }')
html.write('\n                table {')
html.write('\n                    with: 350;')
html.write('\n                }')
html.write('\n            </style>')
html.write('\n        <meta charset="UTF-8"')
html.write('\n    </head>')
html.write('\n    <body>')
html.write('\n        <center>')
html.write('\n            <table border=""> ')
html.write('\n                <tr>')
html.write('\n                    <td>Nombre</td>')
#html.write('\n                    <td>' + classic["nombre"] + '</td>')
html.write('\n                </tr>')
html.write('\n                <tr>')
#html.write('\n                    <td>Apellido</td>')
#html.write('\n                    <td>' + classic["apellido"] + '</td>')
html.write('\n                </tr>')
html.write('\n                <tr>')
#html.write('\n                    <td>Número</td>')
#html.write('\n                    <td>' + classic["numero"] + '</td>')
html.write('\n                </tr>')
html.write('\n                <tr>')
#html.write('\n                    <td>DNI</td>')
#html.write('\n                    <td>' + classic["dni"] + '</td>')
html.write('\n                </tr>')
html.write('\n                <tr>')
#html.write('\n                    <td>Dirección</td>')
#html.write('\n                    <td>' + classic["direccion"] + '</td>')
html.write('\n                </tr>')
html.write('\n        </center>')
html.write('\n    </body>')

##Nombre, Apellido, Numero, dni, direccion, TRANSACCIONES: transaccion 1, 2, 3, 4, 5, 6, 7, 8, 9, 10