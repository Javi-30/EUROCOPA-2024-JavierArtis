from stadium import Stadium
from match import Match

class Search: 

    def __init__(self, partidos, estadios):
        self.partidos = partidos
        self.estadios = estadios
        pass

    def search_by_country(self): 

        while True: 
            try: 
                country = str(input("\n\nNombre de País:     "))

                if not "".join(country.split()).isalpha():
                    raise Exception 

                break 

            except: 
                print("\nIntente de nuevo.\n")

        country = country.title()

        found = []

        for match in self.partidos:

            if country in Match.get_countries(match): 
                found.append(match)

        self.print_found(found)

    def search_by_stadium(self): 
        for stadium in self.estadios: 
            Stadium.print_stadium(stadium)

        while True: 
            try: 
                selection = int(input("ID del estadio a buscar:     "))

                if selection not in range(1, 9): 
                    raise Exception

                break 

            except: 
                print("\nError. ID de estadio inválido.\n")

        selected_obj = self.estadios[selection-1]
        found = []

        for match in self.partidos:
            if selected_obj == Match.get_stadium(match):
                found.append(match)

        self.print_found(found)

    def search_by_date(self): 
        print("\nBuscando por fecha:\n")

        while True: 
            try: 
                day = input("Día a buscar: ")
                month = input("Mes a buscar (número): ")
           
                if int(day) in range(1,32) and int(month) in range(1,13):
                    break

            except: 
                print("\n La información específicada no es correcta. \n")

        date = month + "/" + day + "/2022"

        found = []
        for partido in self.partidos: 
            if date in Match.get_date(partido):
                found.append(partido)
        self.print_found(found)
        
    def print_found(self, found): 
        print("RESULTADOS DE BÚSQUEDA")
        for p in found: 
            Match.print_match(p)