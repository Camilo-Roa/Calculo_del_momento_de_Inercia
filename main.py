#                                  Epsilon
#       By Camilo Roa

#   Setup: Instalar 'tqdm' en la terminal con: <<pip install tqdm>>

import time
from time import sleep
import sys
from tqdm import tqdm

print('\n Iniciando programa...')       # Primer mensaje de bienvenida

animacion = "|/-\\"  # Spinner
for i in range(44):
    time.sleep(0.085)
    sys.stdout.write("\r" + animacion[i % len(animacion)])
    sys.stdout.flush()
    # Acción ->

retry = True    # Condicion para programa en ciclo(volver a empezar)

while retry == True:
    print("\n Funciones:\n1|Cálculo del momento de inercia de un sólido rígido en su eje simétrico\n2|Cálculo del momento de inercia de un sólido rígido en un eje distinto al de su simetría, mediante el teorema de Steiner-Huygens\n")

    # Definir funciones
    def cargando():                 # Barra de carga
        for i in tqdm(range(100)):
            sleep(0.0090)
        sys.stdout.flush()
        return


    def micmesfera(m, r):                 # Momento de Inercia esfera solida
        rta = 0.4*m*r*r
        rta = str(rta)
        return rta

    def miesfera(m, r, d):                # Momento de inercia esfera por teorema
        rta = (0.4*m*r*r)+m*d*d
        rta = str(rta)
        return rta


    def micmesferah(m, r):                 # Momento de Inercia esfera hueca de pared delgada
        rta = (2*m*r*r)/3
        rta = str(rta)
        return rta

    def miesferah(m, r, d):                 # Momento de Inercia esfera hueca de pared delgada por teorema
        rta = ((2*m*r*r)/3)+m*d*d
        rta = str(rta)
        return rta


    def micmcilindro(m, r):               # Momento de Inercia cilindro solido
        rta = 0.5*m*r*r
        rta = str(rta)
        return rta

    def micilindro(m, r, d):                 # Momento de Inercia cilindro solido por teorema
        rta = (0.5*m*r*r)+m*d*d
        rta = str(rta)
        return rta


    def micmclindroh(m, rg, rp):                 # Momento de Inercia cilindro hueco
        rta = 0.5*m*((rg*rg)+(rp*rp))
        rta = str(rta)
        return rta

    def miclindroh(m, rg, rp, d):                 # Momento de Inercia cilindro hueco por teorema
        rta = (0.5*m*((rg*rg)+(rp*rp)))+m*d*d
        rta = str(rta)
        return rta


    def micmcilindrohpd(m, r):               # Momento de Inercia cilindro hueco pared delgada
        rta = m*r*r
        rta = str(rta)
        return rta

    def micilindrohpd(m, r, d):               # Momento de Inercia cilindro hueco pared delgada por teorema
        rta = (m*r*r)+m*d*d
        rta = str(rta)
        return rta


    def micmvarilla(m, lng):                 # Momento de Inercia varilla
        rta = (m*lng*lng)/12
        rta = str(rta)
        return rta

    def mivarilla(m, lng, d):                 # Momento de Inercia varilla por teorema
        rta = ((m*lng*lng)/12)+m*d*d
        rta = str(rta)
        return rta


    def calcmicm():
        retry1 = True   # Para reintentar la función con otro objeto
        while retry1 == True:
            print("\n Objetos:\n1|Esfera sólida\n2|Esfera hueca de pared delgada\n3|Cilindro sólido\n4|Cilindro hueco\n5|Cilindro hueco de pared delgada\n6|Varilla sólida")
            while True:
                try:
                    obj = input('\nEscriba el número del objeto correspondiente: ')  # Seleccionar número para escoger el objeto
                    obj = float(obj)

                    if obj == 1:  # Para usar la fórmula correspondiente
                        print("\n  Se seleccionó la esfera.")
                        while True:
                            try:
                                masa = float(input("\nMasa de la esfera(kg): "))
                                masa = float(masa)
                                while True:
                                    try:
                                        radio = input("\nRadio de la esfera(m): ")
                                        radio = float(radio)
                                        respuesta = micmesfera(masa, radio)
                                        print("\n  El momento de inercia es: I= " + respuesta + " kg.m²")  # ² = alt+0178
                                    except:
                                        print("  Respuesta no válida, intente de nuevo.")
                                        continue  # Volver a Intentar
                                    else:
                                        break  # Valor Aceptado, romper ciclo
                            except:
                                print("  Respuesta no válida, intente de nuevo.")
                                continue  # Volver a Intentar
                            else:
                                break  # Valor Aceptado, romper ciclo

                    elif obj == 3:
                        print("\n  Se seleccionó el cilindro sólido.")
                        while True:
                            try:
                                masa = input("\nMasa del cilindro(kg): ")
                                masa = float(masa)
                                while True:
                                    try:
                                        radio = input("\nRadio del cilindro(m): ")
                                        radio = float(radio)
                                        respuesta = micmcilindro(masa, radio)
                                        print("\n  El momento de inercia es: I= " + respuesta + " kg.m²")   # ² = alt+0178
                                    except:
                                        print("  Respuesta no válida, intente de nuevo.")
                                        continue  # Volver a Intentar
                                    else:
                                        break  # Valor Aceptado, romper ciclo
                            except:
                                print("  Respuesta no válida, intente de nuevo.")
                                continue  # Volver a Intentar
                            else:
                                break  # Valor Aceptado, romper ciclo

                    elif obj == 4:
                        print("\n  Se seleccionó el cilindro hueco.")
                        while True:
                            try:
                                masa = input("\nMasa del cilindro hueco(kg): ")
                                masa = float(masa)
                                while True:
                                    try:
                                        radio1 = input("\nRadio mayor del cilindro(m): ")
                                        radio1 = float(radio1)
                                        while True:
                                            try:
                                                radio2 = input("\nRadio menor del cilindro(m): ")
                                                radio2 = float(radio2)
                                                respuesta = micmclindroh(masa, radio1, radio2)
                                                print("\n  El momento de inercia es: I= " + respuesta + " kg.m²")  # ² = alt+0178
                                            except:
                                                print("  Respuesta no válida, intente de nuevo.")
                                                continue  # Volver a Intentar
                                            else:
                                                break  # Valor Aceptado, romper ciclo
                                    except:
                                        print("  Respuesta no válida, intente de nuevo.")
                                        continue  # Volver a Intentar
                                    else:
                                        break  # Valor Aceptado, romper ciclo
                            except:
                                print("  Respuesta no válida, intente de nuevo.")
                                continue  # Volver a Intentar
                            else:
                                break  # Valor Aceptado, romper ciclo

                    elif obj == 5:
                        print("\n  Se seleccionó el cilindro hueco de pared delgada.")
                        while True:
                            try:
                                masa = float(input("\nMasa del cilindro(kg): "))
                                masa = float(masa)
                                while True:
                                    try:
                                        radio = input("\nRadio del cilindro(m): ")
                                        radio = float(radio)
                                        respuesta = micmcilindrohpd(masa, radio)
                                        print("\n  El momento de inercia es: I= " + respuesta + " kg.m²")   # ² = alt+0178
                                    except:
                                        print("  Respuesta no válida, intente de nuevo.")
                                        continue  # Volver a Intentar
                                    else:
                                        break  # Valor Aceptado, romper ciclo
                            except:
                                print("  Respuesta no válida, intente de nuevo.")
                                continue  # Volver a Intentar
                            else:
                                break  # Valor Aceptado, romper ciclo

                    elif obj == 6:
                        print("\n  Se seleccionó la varilla sólida.")
                        while True:
                            try:
                                masa = float(input("\nMasa de la varilla(kg): "))
                                masa = float(masa)
                                while True:
                                    try:
                                        lng = input("\nLongitud total de la varilla(m): ")
                                        lng = float(lng)
                                        respuesta = micmvarilla(masa, lng)
                                        print("\n  El momento de inercia es: I= " + respuesta + " kg.m²")   # ² = alt+0178
                                    except:
                                        print("  Respuesta no válida, intente de nuevo.")
                                        continue  # Volver a Intentar
                                    else:
                                        break  # Valor Aceptado, romper ciclo
                            except:
                                print("  Respuesta no válida, intente de nuevo.")
                                continue  # Volver a Intentar
                            else:
                                break  # Valor Aceptado, romper ciclo

                    elif obj == 2:
                        print("\n  Se seleccionó la esfera hueca de pared delgada.")
                        while True:
                            try:
                                masa = float(input("\nMasa de la esfera(kg): "))
                                masa = float(masa)
                                while True:
                                    try:
                                        radio = input("\nRadio de la esfera(m): ")
                                        radio = float(radio)
                                        respuesta = micmesferah(masa, radio)
                                        print(
                                            "\n  El momento de inercia es: I= " + respuesta + " kg.m²")  # ² = alt+0178
                                    except:
                                        print("  Respuesta no válida, intente de nuevo.")
                                        continue  # Volver a Intentar
                                    else:
                                        break  # Valor Aceptado, romper ciclo
                            except:
                                print("  Respuesta no válida, intente de nuevo.")
                                continue  # Volver a Intentar
                            else:
                                break  # Valor Aceptado, romper ciclo
                    else:
                        print("  ¡Ese objeto no está en la lista!")
                        continue  # En caso de que el número de objeto no exista, reintentar el ciclo
                except:
                    print("  Respuesta no válida, intente de nuevo.")
                    continue  # Volver a Intentar
                else:
                    break  # Valor Aceptado, romper ciclo
            while True:
                try:
                    rt1 = input("\n¿Desea calcular con otro objeto?\n  ")
                    rt1 = rt1[0].lower()
                except:
                    print("  Respuesta no válida, intente de nuevo.")
                    continue  # Volver a Intentar
                else:
                    break  # Valor Aceptado, romper ciclo
            if rt1 == "n":
                retry1 = False
                print("\nCerrando función...")
                #       Spinner
                animacion = "|/-\\"
                for i in range(20):
                    time.sleep(0.085)
                    sys.stdout.write("\r" + animacion[i % len(animacion)])
                    sys.stdout.flush()
                    # Acción ->
            else:
                retry1 = True
        return



    def calcmi():
        retry1 = True  # Para reintentar la función con otro objeto
        while retry1 == True:
            print(
                "\n Objetos:\n1|Esfera sólida\n2|Esfera hueca de pared delgada\n3|Cilindro sólido\n4|Cilindro hueco\n5|Cilindro hueco de pared delgada\n6|Varilla sólida")
            while True:
                try:
                    obj = input(
                        '\nEscriba el número del objeto correspondiente: ')  # Seleccionar número para escoger el objeto
                    obj = float(obj)

                    if obj == 1:  # Para usar la fórmula correspondiente
                        print("\n  Se seleccionó la esfera.")
                        while True:
                            try:
                                masa = float(input("\nMasa de la esfera(kg): "))
                                masa = float(masa)
                                while True:
                                    try:
                                        radio = input("\nRadio de la esfera(m): ")
                                        radio = float(radio)
                                        while True:
                                            try:
                                                distancia = input("\nDistancia al centro de masa(m): ")
                                                distancia = float(distancia)
                                                respuesta = miesfera(masa, radio, distancia)
                                                print("\n  El momento de inercia es: I= " + respuesta + " kg.m²")  # ² = alt+0178
                                            except:
                                                print("  Respuesta no válida, intente de nuevo.")
                                                continue  # Volver a Intentar
                                            else:
                                                break  # Valor Aceptado, romper ciclo   # ² = alt+0178
                                    except:
                                        print("  Respuesta no válida, intente de nuevo.")
                                        continue  # Volver a Intentar
                                    else:
                                        break  # Valor Aceptado, romper ciclo
                            except:
                                print("  Respuesta no válida, intente de nuevo.")
                                continue  # Volver a Intentar
                            else:
                                break  # Valor Aceptado, romper ciclo

                    elif obj == 3:
                        print("\n  Se seleccionó el cilindro sólido.")
                        while True:
                            try:
                                masa = input("\nMasa del cilindro(kg): ")
                                masa = float(masa)
                                while True:
                                    try:
                                        radio = input("\nRadio del cilindro(m): ")
                                        radio = float(radio)
                                        while True:
                                            try:
                                                distancia = input("\nDistancia al centro de masa(m): ")
                                                distancia = float(distancia)
                                                respuesta = micilindro(masa, radio, distancia)
                                                print("\n  El momento de inercia es: I= " + respuesta + " kg.m²")  # ² = alt+0178
                                            except:
                                                print("  Respuesta no válida, intente de nuevo.")
                                                continue  # Volver a Intentar
                                            else:
                                                break  # Valor Aceptado, romper ciclo   # ² = alt+0178
                                    except:
                                        print("  Respuesta no válida, intente de nuevo.")
                                        continue  # Volver a Intentar
                                    else:
                                        break  # Valor Aceptado, romper ciclo
                            except:
                                print("  Respuesta no válida, intente de nuevo.")
                                continue  # Volver a Intentar
                            else:
                                break  # Valor Aceptado, romper ciclo

                    elif obj == 4:
                        print("\n  Se seleccionó el cuarto objeto.")
                        while True:
                            try:
                                masa = input("\nMasa del cilindro hueco(kg): ")
                                masa = float(masa)
                                while True:
                                    try:
                                        radio1 = input("\nRadio mayor del cilindro(m): ")
                                        radio1 = float(radio1)
                                        while True:
                                            try:
                                                radio2 = input("\nRadio menor del cilindro(m): ")
                                                radio2 = float(radio2)
                                                while True:
                                                    try:
                                                        distancia = input("\nDistancia al centro de masa(m): ")
                                                        distancia = float(distancia)
                                                        respuesta = miclindroh(masa, radio1, radio2, distancia)
                                                        print("\n  El momento de inercia es: I= " + respuesta + " kg.m²")  # ² = alt+0178
                                                    except:
                                                        print("  Respuesta no válida, intente de nuevo.")
                                                        continue  # Volver a Intentar
                                                    else:
                                                        break  # Valor Aceptado, romper ciclo   # ² = alt+0178
                                            except:
                                                print("  Respuesta no válida, intente de nuevo.")
                                                continue  # Volver a Intentar
                                            else:
                                                break  # Valor Aceptado, romper ciclo
                                    except:
                                        print("  Respuesta no válida, intente de nuevo.")
                                        continue  # Volver a Intentar
                                    else:
                                        break  # Valor Aceptado, romper ciclo
                            except:
                                print("  Respuesta no válida, intente de nuevo.")
                                continue  # Volver a Intentar
                            else:
                                break  # Valor Aceptado, romper ciclo

                    elif obj == 5:
                        print("\n  Se seleccionó el quinto objeto.")
                        while True:
                            try:
                                masa = float(input("\nMasa del cilindro(kg): "))
                                masa = float(masa)
                                while True:
                                    try:
                                        radio = input("\nRadio del cilindro(m): ")
                                        radio = float(radio)
                                        while True:
                                            try:
                                                distancia = input("\nDistancia al centro de masa(m): ")
                                                distancia = float(distancia)
                                                respuesta = micilindrohpd(masa, radio, distancia)
                                                print("\n  El momento de inercia es: I= " + respuesta + " kg.m²")  # ² = alt+0178
                                            except:
                                                print("  Respuesta no válida, intente de nuevo.")
                                                continue  # Volver a Intentar
                                            else:
                                                break  # Valor Aceptado, romper ciclo   # ² = alt+0178
                                    except:
                                        print("  Respuesta no válida, intente de nuevo.")
                                        continue  # Volver a Intentar
                                    else:
                                        break  # Valor Aceptado, romper ciclo
                            except:
                                print("  Respuesta no válida, intente de nuevo.")
                                continue  # Volver a Intentar
                            else:
                                break  # Valor Aceptado, romper ciclo

                    elif obj == 6:
                        print("\n  Se seleccionó el quinto objeto.")
                        while True:
                            try:
                                masa = float(input("\nMasa de la varilla(kg): "))
                                masa = float(masa)
                                while True:
                                    try:
                                        lng = input("\nLongitud total de la varilla(m): ")
                                        lng = float(lng)
                                        while True:
                                            try:
                                                distancia = input("\nDistancia al centro de masa(m): ")
                                                distancia = float(distancia)
                                                respuesta = mivarilla(masa, lng, distancia)
                                                print("\n  El momento de inercia es: I= " + respuesta + " kg.m²")  # ² = alt+0178
                                            except:
                                                print("  Respuesta no válida, intente de nuevo.")
                                                continue  # Volver a Intentar
                                            else:
                                                break  # Valor Aceptado, romper ciclo   # ² = alt+0178
                                    except:
                                        print("  Respuesta no válida, intente de nuevo.")
                                        continue  # Volver a Intentar
                                    else:
                                        break  # Valor Aceptado, romper ciclo
                            except:
                                print("  Respuesta no válida, intente de nuevo.")
                                continue  # Volver a Intentar
                            else:
                                break  # Valor Aceptado, romper ciclo

                    elif obj == 2:
                        print("\n  Se seleccionó el segundo objeto.")
                        while True:
                            try:
                                masa = float(input("\nMasa de la esfera(kg): "))
                                masa = float(masa)
                                while True:
                                    try:
                                        radio = input("\nRadio de la esfera(m): ")
                                        radio = float(radio)
                                        while True:
                                            try:
                                                distancia = input("\nDistancia al centro de masa(m): ")
                                                distancia = float(distancia)
                                                respuesta = miesferah(masa, radio, distancia)
                                                print("\n  El momento de inercia es: I= " + respuesta + " kg.m²")  # ² = alt+0178
                                            except:
                                                print("  Respuesta no válida, intente de nuevo.")
                                                continue  # Volver a Intentar
                                            else:
                                                break  # Valor Aceptado, romper ciclo   # ² = alt+0178
                                    except:
                                        print("  Respuesta no válida, intente de nuevo.")
                                        continue  # Volver a Intentar
                                    else:
                                        break  # Valor Aceptado, romper ciclo
                            except:
                                print("  Respuesta no válida, intente de nuevo.")
                                continue  # Volver a Intentar
                            else:
                                break  # Valor Aceptado, romper ciclo
                    else:
                        print("  ¡Ese objeto no está en la lista!")
                        continue  # En caso de que el número de objeto no exista, reintentar el ciclo
                except:
                    print("  Respuesta no válida, intente de nuevo.")
                    continue  # Volver a Intentar
                else:
                    break  # Valor Aceptado, romper ciclo
            while True:
                try:
                    rt1 = input("\n¿Desea calcular con otro objeto?\n  ")
                    rt1 = rt1[0].lower()
                except:
                    print("  Respuesta no válida, intente de nuevo.")
                    continue  # Volver a Intentar
                else:
                    break  # Valor Aceptado, romper ciclo
            if rt1 == "n":
                retry1 = False
                print("\nCerrando función...")
                #       Spinner
                animacion = "|/-\\"
                for i in range(20):
                    time.sleep(0.085)
                    sys.stdout.write("\r" + animacion[i % len(animacion)])
                    sys.stdout.flush()
                    # Acción ->
            else:
                retry1 = True
        return

    def pendulofisico():
        retry1 = True  # Para reintentar la función con otro objeto
        while retry1 == True:
            print("\n Objetos:\n1|Esfera sólida\n2|Esfera hueca de pared delgada\n3|Cilindro sólido\n4|Cilindro hueco\n5|Cilindro hueco de pared delgada\n6|Varilla sólida")
            # Poner otro while
            while True:
                try:
                    rt1 = input("\n¿Desea calcular con otro objeto?\n  ")
                    rt1 = rt1[0].lower()
                except:
                    print("  Respuesta no válida, intente de nuevo.")
                    continue  # Volver a Intentar
                else:
                    break  # Valor Aceptado, romper ciclo
            if rt1 == "n":
                retry1 = False
                print("\nCerrando función...")
                #       Spinner
                animacion = "|/-\\"
                for i in range(20):
                    time.sleep(0.085)
                    sys.stdout.write("\r" + animacion[i % len(animacion)])
                    sys.stdout.flush()
                    # Acción ->
            else:
                retry1 = True
        return


    # Inicio del ciclo secundario (main)
    while True:
        try:
            fncn = input('\nEscriba el número de la función: ')  # Seleccionar número para lamar función
            fncn = float(fncn)
            if fncn == 1:                                        # Para seleccionar la función a ejecutar
                print("\n  Se seleccionó la primer función.")
                cargando()  # Barra de carga
                calcmicm()  #Llamar función principal
            elif fncn == 2:
                print("\n  Se seleccionó la segunda función.")

                cargando()  # Barra de carga
                calcmi() #Llamar función principal
            elif fncn == 3:
                print("\n  Se seleccionó la tercera función.")

                cargando()  # Barra de carga
                pendulofisico()  #Llamar función principal
            else:
                print("  ¡Esa función no está en la lista!")
                continue                                       # En caso de que el número de función no exista, reintentar el ciclo
        except:
            print("  Respuesta no válida, intente de nuevo.")
            continue    # Volver a Intentar
        else:
            break   # Valor Aceptado, romper ciclo


    # Re-Try?
    while True:
        try:
            rt = input("\n\n¿Desea usar otra función?\n  ")
            rt = rt[0].lower()
        except:
            print("  Respuesta no válida, intente de nuevo.")
            continue    # Volver a Intentar
        else:
            break   # Valor Aceptado, romper ciclo
    if rt == "n":
        retry = False
        print("\nFinalizando programa...")
        #       Spinner
        animacion = "|/-\\"
        for i in range(20):
            time.sleep(0.085)
            sys.stdout.write("\r" + animacion[i % len(animacion)])
            sys.stdout.flush()
            # Acción ->
    else:
        retry = True

