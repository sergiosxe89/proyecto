import sys

from criptomonedas import Wallet, criptomoneda


 
class Menu(object):
    '''Muestra un menu y responde a elecciones cuando se ejecuta.'''
    def __init__(self):
        self.criptomonedas = Wallet()
        self.elecciones = {
             "1" : self.mostrar_historico,
             "2" : self.recibir_cant,
             "3" : self.transferir_monto,
             "4" : self.mostrar_balancecripto,
             "5" : self.mostrar_balancegeneral,
             "6" : self.quit
                               
                 } 

    def mostrar_menu(self):
        print("""
Menu 

1 Mostrar historico de transacciones
2 Recibir cantidad
3 Transferir monto
4 Mostrar balance una moneda
5 Mostrar balance general
6 Salir
""")

    def run(self):
