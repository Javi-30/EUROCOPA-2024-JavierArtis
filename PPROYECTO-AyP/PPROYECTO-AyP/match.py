from team import Team
from stadium import Stadium

class Match():

    def __init__(self, local, visitante, date, estadio, id_partido, vendidos, asistencia, taken_seats):
        self.local = local
        self.visitante = visitante
        self.date = date
        self.estadio = estadio
        self.id_partido = id_partido
        self.vendidos = vendidos
        self.asistentes = asistencia
        self.taken_seats = taken_seats
        pass

    def print_match(self):         
        estadio_str = Stadium.get_name(self.estadio)
        local_str = Team.get_name(self.local)
        visitante_str = Team.get_name(self.visitante)

        print(f"""
        Partido #{self.id_partido}
        Local: {local_str}
        Visitante: {visitante_str}
        Fecha y Hora: {self.date}
        Estadio: {estadio_str}
        """)

    def get_info(self): 
        local_str = Team.get_name(self.local)
        visitante_str = Team.get_name(self.visitante)
        estadio_str = Stadium.get_name(self.estadio)

        info = f"{local_str} vs. {visitante_str} // {estadio_str} // {self.date}"
        return info

    def get_countries(self): 
        local_str = Team.get_name(self.local)
        visitante_str = Team.get_name(self.visitante)
        countries = f"{local_str} vs. {visitante_str}"
        return countries

    def get_stadium(self): 
        return self.estadio

    def get_date(self): 
        return self.date

    def get_id(self): 
        return self.id_partido

    def get_taken_seats(self): 
        return self.taken_seats

    def get_asistentes(self):
        return self.asistentes

    def get_vendido(self):
        return self.vendidos

    def new_venta(self): 
        self.vendidos += 1

    def new_asistente(self):
        self.asistentes += 1

    def new_taken_seat(self, seat): 
        self.taken_seats.append(seat)