from match import Match
from stadium import Stadium

class Purchase: 

    def __init__(self, code, name, id, edad, partido, sector, asiento, amount, consumo):        
        self.code = code
        self.name = name
        self.id = id 
        self.edad = edad 
        self.partido = partido
        self.sector = sector
        self.asiento = asiento
        self.amount = amount
        self.consumo = consumo 
        #Consumo será una lista de objetos Producto
        pass
    
    def print_receipt(self):

        # Al imprimir la factura, necesitamos primero tener el partido como string, porque actualmente lo tenemos como objeto. 

        partido_str = Match.get_info(self.partido)    
        print("""
        -------------------------------------------
        \t\t\t FACTURA #{}
        Nombre: {}
        ID: {}
        Edad: {}
        Partido: {}
        Tipo de entrada: {}
        Asiento: {}
        Monto: {}
        --------------------------------------------
        """.format(self.code, self.name, self.id, self.edad, partido_str, self.sector, self.asiento, self.amount))

    def get_code(self):
        return self.code

    def get_match(self):
        return self.partido

    def get_id(self):
        return self.id

    def get_sector(self):
        return self.sector

    def get_monto(self):
        return self.amount
    
    def get_consumo(self):
        return self.consumo

    def set_consumo(self, carrito):

        # Le damos al usuario lo pedido, su orden. 
        #    Args:
        #        carrito (list): lo pedido por el cliente

        self.consumo = carrito
    
    def sumar_comsumo(self, monto):

        # Ajustamos su gasto total si consumió en restaurantes. 
        # Args:
        #     monto (float): monto adicional por consumo en restaurante

        self.amount += monto
    
    def get_string_all(self):

        partido_info = Match.get_info(self.partido)

        string = """"
            -------------------------------------------
            \t\t\t Compra #{}
            Nombre: {}
            ID: {}
            Edad: {}
            Partido: {}
            Tipo de entrada: {}
            Asiento: {}
            Monto: {}
            Consumo: {}
        --------------------------------------------
        """.format(self.code, self.name, self.id, self.edad, partido_info, self.sector, self.asiento, self.amount, self.consumo)
        return string