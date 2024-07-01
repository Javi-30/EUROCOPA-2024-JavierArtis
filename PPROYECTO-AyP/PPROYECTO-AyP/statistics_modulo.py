from purchase import Purchase
from match import Match
from product import Product

def estadisticas_gral(lista_partidos, lista_purchases):

# Es la main de las estadísticas
#     Args:
#         lista_partidos: lista de objetos Partido.
#         lista_purchases: lista de objetos Purchase

    print("""\n
                    ESTADÍSTICAS 

    Opciones Disponibles
    1.- Promedio de gasto de un VIP.
    2.- Tabla asistencia. 
    3.- Partido con mayor asistencia.
    4.- Partido con mayor venta.
    5.- Top 3 más vendidos en restaurantes. 
    6.- Top 3 clientes. 
    """)

    while True:
        
        try: 
            stat = int(input("\n\n\tEstadística a ver:    "))
            if stat in range(1, 7):
                break
            else:
                raise Exception

        except: 
            print("Ingrese un valor válido.")

    #Distribuimos el programa. 
    if stat == 1:  vip_prom(lista_purchases)
    elif stat == 2:  tablita(lista_partidos)
    elif stat == 3:  mayor_asistencia(lista_partidos)
    elif stat == 4:  mayor_venta(lista_partidos)
    elif stat == 5:  products_mas_vendido(lista_purchases)
    elif stat == 6:  top_clientes(lista_purchases) 
    else: print("")

def vip_prom(lista_purchases):
    cliente_vip = 0
    amount = 0
    for a in lista_purchases: 
        if Purchase.get_sector(a) == "VIP":
            cliente_vip += 1
            amount += float(Purchase.get_monto(a))
            
    if cliente_vip == 0: 
        print("Aún no hay clientes VIP registrados.")
        return

    promedio = amount/cliente_vip

    print("El promedio de un cliente VIP es:    " + str(promedio) + "\n\n")

def tablita(lista_partidos): 

# Agarramos la lista de asistencia ordenada y formamos una tabla yendo secuencialmente preguntando qué asistencia tiene cada juego. 

    asistencia_ordenada = ordenar_por_asistencia(lista_partidos)

    print("\n\n Tabla de Asistencia: ")
    for n in asistencia_ordenada:
        print("Asistencia de " + str(n))
        for match in lista_partidos: 
            if Match.get_asistentes(match)==n:
                print("     -" +Match.get_info(match))

def mayor_asistencia(lista_partidos):
    # Nos guiamos por el primer elemento de la asistencia_ordenada, como lista. 

    print("Entré")
    asistencia_ordenada = ordenar_por_asistencia(lista_partidos)

    for match in lista_partidos: 
        if asistencia_ordenada[0]== Match.get_asistentes(match):
            found = match

    print("\n\n\tEl partido con mayor asistencia fue {} con una asistencia de {} personas.".format(Match.get_info(found), asistencia_ordenada[0]))

def mayor_venta(lista_partidos):

    ventas_ordenadas = ordenar_por_ventas(lista_partidos)

    for match in lista_partidos: 
        if ventas_ordenadas[0]== Match.get_vendido(match):
            found = match

    print("\n\n\tEl partido con mayores ventas fue {} con un de {} boletos vendidos.".format(Match.get_info(found), ventas_ordenadas[0]))

def products_mas_vendido(lista_purchases):

    vendidos = {}

    for x in lista_purchases:
        consumo = Purchase.get_consumo(x)
        if len(consumo) == 0: continue
        for product in consumo: 
            if product in vendidos: 
                vendidos[product] = vendidos[product]+1
            else: 
                vendidos[product] = 1

    sorted_vendidos = sorted(vendidos.items(), key=lambda x:x[1]) #De menor a mayor, lista de tuplas. 
    
    if len(sorted_vendidos) == 0:
        print("Aún no se ha vendido nada.")
        return

    #Ordenamos diccionario.
    if len(sorted_vendidos) >= 3: 
        for i in range(1, 4):
            top_vendidos_tuplas = [sorted_vendidos[-i]]
    else: 
        for i in range(1, len(sorted_vendidos)+1):
            top_vendidos_tuplas = [sorted_vendidos[-i]]

    top_vendidos_dict =  dict(top_vendidos_tuplas)

    for key, value in top_vendidos_dict.items(): 
        print("Los productos más vendidos son: ")
        print(Product.get_name(key) + " vendido " + str(value) + " veces.")

def top_clientes(lista_purchases): 
    clientes_id = {} #ID y cantidad de veces que sale.
    
    for purchase in lista_purchases: 
        id = Purchase.get_id(purchase)
        if id in clientes_id: 
            clientes_id[id] += 1
        else: 
            clientes_id[id] = 1

    #Ordenamos diccionario.
    clientes_ordenado = sorted(clientes_id.items(), key=lambda x:x[1]) #De menor a mayor, lista de tuplas. 
    
    if len(clientes_ordenado) == 0:
        print("Aún no se ha vendido nada.")
        return

    if len(clientes_ordenado) >= 3: 
        for i in range(1, 4):
            top_clientes_list = [clientes_ordenado[-i]]

    else: 
        for i in range(1, len(clientes_ordenado)+1):
            top_clientes_list = [clientes_ordenado[-i]]

    top_clients_dict =  dict(top_clientes_list)

    for key, value in top_clients_dict.items(): 
        print("Los clientes con más boletos son: ")
        print("El cliente ID: " + str(key) + " con un total de " + str(value) + " boletos.")

def ordenar_por_ventas(lista_partidos):
    # Tomo todas las ventas, borro las repetidas y devuelvo las listas ordenadas. 

    all_ventas = []
    for p in lista_partidos: 
        all_ventas.append(Match.get_vendido(p))

    vendidos_n = list(set(all_ventas))

    vendidos_ordenados = sorted(vendidos_n, reverse=True)

    return vendidos_ordenados

def ordenar_por_asistencia(lista_partidos):
    # Primero, tenemos todas la asistencias a todos los partidos, luego, eliminamos los valores repetidos y ordenamos la lista.
    
    all_asistencias = []
    for p in lista_partidos: 
        all_asistencias.append(Match.get_asistentes(p))

    asistencias_valores = list(set(all_asistencias))

    asistentes_ordenados = sorted(asistencias_valores, reverse=True)

    return asistentes_ordenados