import datetime
from menu import Menu

monedas=()
monedas_dict={}

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'



# Almacena todas las ids disponibles para las nuevas transacciones
ultima_transaccion = 0

class criptomoneda:
    '''Representa una moneda. Se compara con un String
    en las búsquedas y las etiquetas para cada moneda '''
    def __init__(self, cripto = "", cantidad = "", cotizacion = ""):
        '''inicializa una moneda con cantidad y cotizacion. Automáticamente configura la fecha
        de creación de la moneda y una única id'''
        self.cripto = cripto
        self.cantidad = cantidad
        self.cotizacion = cotizacion
        self.creation_date = datetime.date.today()
        global ultima_transaccion
        ultima_transaccion += 1
        self.transaccion = ultima_transaccion
    def match(self, filter):
        '''Determina si esta transaccion concuerda con el filtro
        de texto. Devuelve True si concuerda, en otro caso False.
        Búsqueda es case sensitive y compara tanto con text como
        con tags.'''
        return filter in self.cantidad or filter in self.cotizacion

class Wallet:
    '''Representa una colección de transacciones que pueden ser etiquetadas,
    modificadas, y se pueden buscar.'''

    def __init__(self):
        self.transacciones = {}


    def nueva_transaccion( self, cripto, cantidad, cotizacion):
        '''Crea una nueva transaccion y la añade a la lista.'''
        cripto= (self.Menu.recibir_cant(cripto))
        cantidad= self.Menu.recibir_cant(cantidad)
        cotizacion= self.Menu.recibir_cant(cotizacion)

        self.transacciones.setdefault(cripto(cantidad,cotizacion))

    def _encontrar_transaccion(self, ultima_transaccion):
        '''Localiza la transaccion con la id dada.'''
        for transaccion in self.transacciones:
            if str (transaccion.id) == str(ultima_transaccion):
                return transaccion 
        return None
    

    def transferir_cantidad(self, cripto, cantidad):
        '''Encuentra la moneda con la id dada y cambia su
        memo al valor dado.'''
        transaccion = self._encontrar_transaccion(cripto)
        if transaccion:
            transaccion.cantidad = cantidad
            return True
        return False

    def search(self, filter):
        '''Encuentra todas las notas que concuerdan con
        el filtro string dado.'''
        return [transaccion for transaccion in self.transacciones if
                transaccion.match(filter)]


    
 
 