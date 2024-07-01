import inicio

from compra import main_compra
from purchase import Purchase
from match import Match
import autenticar
from statistics_modulo import estadisticas_gral

from restaurantes import start_restaurante

def main(): 

# Inicio y menú principal. Aquí se regresa después de ejecutar cada función. 
#     lista_equipos(list): lista de objetos Team
#     lista_estadios(list): lista de objetos Stadium
#     lista_partidos(list): lista de objetos Match
#     lista_purchases(list): lista de objetos Purchase
#     boletos_validados(list): guarda los IDs que ya fueron validados. De manera que si se dice un ID que ya está aquí, se invalida ese boleto. 
#     given_purchase_ids(list): códigos de factura previamente dados, para que toda factura tenga un código único. 
#     Raises:
#         Exception: Las excepciones tanto en este caso como en el resto del programa serán utilizdas para las validaciones únicamente. En caso de que el cliente ingrese datos que causarían error en el programa.    

    lista_equipos = inicio.setting_equipos_all()
    lista_estadios = inicio.setting_stadiums_all()
    lista_partidos = inicio.setting_matches_all(lista_equipos, lista_estadios)
    lista_purchases = [] 

    given_purchase_ids = []
    boletos_validados = [] 

    print("\t P R O Y E C T O    A L G O R I T M O S  -  J A V I E R    A R T I S")
    print("\t\t\t\t EUROCOPA 2024")

    while True: 
       
        print("""
        Menú: 
        1.- Comprar boleto. 
        2.- Autentificación de Boletos. 
        3.- Restaurantes. 
        4.- Estadísticas. 
        5.- Imprimir todo y guardar.
        6.- Salir
        """)

        while True:
            try: 
                accion = int(input("\nIngrese el número de su selección:    "))

                if accion not in range(1, 7):
                    raise Exception

                break

            except: 
                print("\nOpción Inválida.\n")

        
        if accion == 1: 

            main_compra(lista_estadios, lista_partidos, lista_purchases, given_purchase_ids)

            pass

        elif accion == 2: 

            #Pedimos el código a autenticar. 
            receipt_id = autenticar.get_receipt_id()

            #Recibimos el True si es válido.
            validado = autenticar.validacion(lista_purchases, receipt_id, boletos_validados)

            if validado: 

                print("\n\tAUTENTIFICACIÓN EXITOSA\n")
                for p in lista_purchases:
                    if receipt_id == Purchase.get_code(p):
                        recibo = p

                partido = Purchase.get_match(recibo)

                boletos_validados.append(receipt_id)

                #Le subimos el valor a los asistentes. 
                Match.new_asistente(partido) 
            
            else: 
                print("\n\n El boleto no pudo ser validado por el sistema. Es falso.\n\n")

            pass
        
        elif accion == 3:
            start_restaurante(lista_purchases)
  
        elif accion == 4: 
            estadisticas_gral(lista_partidos, lista_purchases)

        elif accion == 5: 
            guardar = ""
            for purchase in lista_purchases:
                str_compra = Purchase.get_string_all(purchase)
                guardar += str_compra + "\n"
                print("------------------------") 
                Purchase.print_receipt(purchase)
                print("------------------------") 

          
            with open("COMPRAS.txt", "a") as a:
                    a.write("CLIENTES:\n")
                    a.write(guardar)
                    a.write("")
            break

        else: 
            print("\nCERRANDO")
            break
            

    
main()