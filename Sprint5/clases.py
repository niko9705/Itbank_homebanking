import json

def cargar_datos_classic(ruta):
    with open(ruta) as contenido:
        classic = json.load(contenido)
        print(classic)
        
if __name__ == '__main__':
    ruta ='JSON/eventos_classic.json' ##no me sale bien la dirección:(((
    cargar_datos_classic(ruta)

class Cliente():
    def __init__(self, nombre, apellido, numero, dni, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni
        self.direccion = direccion
    
    def __str__(self):
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\
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
        print(f"Tipo: {self.tipo}\nTarjeta de débito: {self.tarjeta_debito}\nCaja de ahorro en pesos: {self.caja_ahorro_peso}\nCaja de ahorro en dólares: {self.caja_ahorro_dolar}\nCompra/venta dólar: {self.compra_venta_dolar}\nRetiro máximo: {self.retiro_maximo}\
            \nTarjeta de crédito: {self.tarjeta_credito}\nChequera: {self.chequera}\nComisión de transacción: {self.comision_transaccion}\
            \nLímite de transferencia: {self.limite_transferencia}")

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
        print(f"Tipo: {self.tipo}\nTerjeta de débito: {self.tarjeta_debito}\nCuenta corriente: {self.cuenta_corriente}\
            \nCaja de ahorro en dólares: {self.caja_ahorro_dolar}\nCompra/venta en dólares: {self.compra_venta_dolar}\nRetiro máximo: {self.retiro_maximo}\nTarjeta de crédito: {self.tarjeta_credito}\
            \nChequera: {self.chequera}\nComisión de transacción: {self.comision_transaccion}\nLímite de transferencia: {self.limite_transferencia}\nMonto descubierto: {self.monto_descubierto}")

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


#Juancito = Classic(nombre = "Juan", apellido = "Perez", numero = 123123123, dni = 12345678, direccion = "Calle falsa 123")

#Juancito.__str__()

numero = input('Ingrese el número de cliente: ')