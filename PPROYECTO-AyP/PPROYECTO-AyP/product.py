class Product: 

    def __init__(self, name, quantity, price, type, adicional):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.type = type
        self.adicional = adicional 
        pass

    def print_product_all(self):
        print("""
        Nombre:{}
        Cantidad: {}
        Precio: {}$
        Tipo: {}
        Adicional: {}
        """.format(self.name, self.quantity, self.price, self.type, self.adicional))

    def print_product_in_menu(self): 
        print("""
        Nombre:{}
        Precio: {}$
        Tipo: {}
        """.format(self.name, self.price, self.adicional))
    
    def get_price(self):
        return self.price

    def lower_quantity(self):
        self.quantity -= 1
    
    def get_quantity(self):
        return self.quantity

    def get_name(self):
        return self.name