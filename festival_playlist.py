nombres = []
artistas = []
duraciones = []
popularidades = []

def agregar_canciones():
    try:
        cantidad = int(input("¿Cuantas canciones quieres agregar? "))
    except ValueError:
        print("Ingresa un número valido")
        return

    for i in range(cantidad):
        print(f"\n--- Cancion {i+1} ---")
        nombre = input("Nombre: ")
        artista = input("Artista: ")

        while True:
            try:
                duracion = float(input("Duracion en minutos: "))
                break
            except ValueError:
                print("Ingresa un numero valido.")

        while True:
            try:
                popularidad = int(input("Popularidad (1-100): "))
                if 1 <= popularidad <= 100:
                    break
                else:
                    print("Debe estar entre 1 y 100")
            except ValueError:
                print("Ingresa un número válido.")

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

    print("\nCanciones agregadas correctamente.\n")


def ver_reportes():
    if not nombres:
        print("Aún no hay canciones registradas.")
        return

    total = len(nombres)
    duracion_total = sum(duraciones)
    mas_popular = max(popularidades)
    menos_popular = min(popularidades)
    promedio = sum(popularidades) / total

    indice_mas = popularidades.index(mas_popular)
    indice_menos = popularidades.index(menos_popular)

    print("\nREPORTES DEL FESTIVAL")
    print(f"Total de canciones: {total}")
    print(f"Duración total: {duracion_total:.2f} minutos")
    print(f"Canción más popular: {nombres[indice_mas]} ({mas_popular})")
    print(f"Canción menos popular: {nombres[indice_menos]} ({menos_popular})")
    print(f"Promedio de popularidad: {promedio:.2f}\n")


def buscar_canciones():
    if not nombres:
        print("No hay canciones registradas.")
        return

    print("\nBuscar canciones")
    print("1. Por artista")
    print("2. Por rango de popularidad")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        artista_buscar = input("Ingresa el nombre del artista: ").lower()
        print("\nResultados:")
        encontrado = False
        for i in range(len(nombres)):
            if artistas[i].lower() == artista_buscar:
                print(f"- {nombres[i]} ({popularidades[i]})")
                encontrado = True
        if not encontrado:
            print("No se encontraron canciones.")

    elif opcion == "2":
        try:
            minimo = int(input("Popularidad mínima: "))
            maximo = int(input("Popularidad máxima: "))
        except ValueError:
            print("Ingresa números válidos.")
            return

        print("\nResultados:")
        encontrado = False
        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                print(f"- {nombres[i]} ({popularidades[i]})")
                encontrado = True
        if not encontrado:
            print("No se encontraron canciones.")

    else:
        print("Opción inválida.")


def playlist_recomendada():
    if not nombres:
        print("No hay canciones registradas.")
        return

    promedio = sum(popularidades) / len(popularidades)

    print("\nPLAYLIST RECOMENDADA")
    print(f"Popularidad mayor al promedio ({promedio:.2f})")

    recomendadas = False
    for i in range(len(nombres)):
        if popularidades[i] > promedio:
            print(f"- {nombres[i]} ({popularidades[i]})")
            recomendadas = True

    if not recomendadas:
        print("No hay canciones que superen el promedio.")


while True:
    print("\nFESTIVAL PLAYLIST")
    print("1. Agregar canciones")
    print("2. Ver reportes")
    print("3. Buscar canciones")
    print("4. Playlist recomendada")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_canciones()
    elif opcion == "2":
        ver_reportes()
    elif opcion == "3":
        buscar_canciones()
    elif opcion == "4":
        playlist_recomendada()
    elif opcion == "5":
        print("\nGracias por usar Festival Playlist.")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
