from team import Team
from product import Product

class Stadium:  

    def __init__(self, id, name, capacidad, location, restaurants):
        self.id = id
        self.name = name
        self.capacidad = capacidad
        self.location = location 
        self.restaurants = restaurants
        pass

    def print_stadium(self): 
        print("""
        ID: {}
        Nombre: {}
        Capacidad: 
            VIP:{}   
            General:{}
        Locación: {}
        """.format(self.id, self.name, self.capacidad[1], self.capacidad[0], self.location))

    def print_stadium_all(self):
        print("""
        ID: {}
        Nombre: {}
        Capacidad: 
            VIP:{}   
            General:{}
        Locación: {}
        """.format(self.id, self.name, self.capacidad[1], self.capacidad[0], self.location))
        self.print_restaurants()

    def get_restaurants(self):
        return self.restaurants

    def print_restaurants(self):
        for rest in self.restaurants: 
            print(rest["name"])
            print(" -Productos:")
            for p in rest["products"]:
                Product.print_product_all(p)

    def get_capacidad(self):
        return self.capacidad

    def get_name(self): 
        return self.name