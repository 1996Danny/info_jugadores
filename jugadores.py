from PIL import Image # Descargar pillow (pip install pillow) para el manejo de imagenes
import json

def cargar_desde_json():
    try:
        with open('jugadoresBD.json', 'r') as file:
            return json.load(file) #nos retorna un dict a partir del jugadoresBD.json
    except FileNotFoundError:
        return {}

jugadores = cargar_desde_json() #asignamos el dict obtenido en la variable jugadores

def buscar_jugador():
    nombre = input("Introduce el nombre del jugador que quieres buscar: ")
    for id, jugador in jugadores.items():
        if jugador["nombre"].lower() == nombre.lower():
            print(f"Nombre: {jugador['nombre']}")
            print(f"Equipo: {jugador['equipo']}")
            print(f"Posición: {jugador['posicion']}")
            print(f"Edad: {jugador['edad']} años")

            # Abrimos la imagen del jugadoir y la mostramos
            imagen = Image.open(jugador["imagen"])
            imagen.show()

            # Para veo o modificar el jugador encontrado
            # Opciones para modificar o ver la información
            while True:
                print()
                print("1. Modificar información")
                print("2. Volver al menú principal")
                opcion = input("Selecciona una opción:\n")

                if opcion == "1":
                    # solicitamos la nueva informacion del jugador a modificar
                    jugador["nombre"] = input("Nuevo nombre: ")
                    jugador["equipo"] = input("Nuevo equipo: ")
                    jugador["posicion"] = input("Nueva posición: ")
                    jugador["edad"] = int(input("Nueva edad: "))
                    jugador["imagen"] = input("Nuevo nombre de imagen: ")
                    print("Información modificada con éxito.")
                elif opcion == "2":
                    return menu()
                else:
                    print("Opción no válida. Introduce 1 o 2.")
    print("Jugador no encontrado.")


def agregar_jugador():

    nombre = input("Nombre del jugador: ")
    equipo = input("Equipo del jugador: ")
    posicion = input("Posición del jugador: ")
    edad = input("Edad del jugador: ")
    imagen = input("ingrese el nombre de la imagen con su extensión: ")

    #Generamos el un uevo id para los nuevos datos cargados
    nuevo_id = str(len(jugadores) + 1)
    jugadores[nuevo_id] = {
        "nombre": nombre,
        "equipo": equipo,
        "posicion": posicion,
        "edad": int(edad),
        "imagen": "./img/" + imagen
    }
    print(f"{nombre} ha sido agregado a jugadores.")

# No olvidad de ejecutar la func siempre que modificamos o cargamos datos de nuevos jugadores
def guardar_en_json():
    with open('jugadoresBD.json', 'w') as file:
        json.dump(jugadores, file) #nos crea y retorna un json con los datos guardados en el dict jugadores

def menu():
    while True:
        print("\nBienvenidos")
        print("1. Buscar jugador")
        print("2. Agregar jugador")
        print("3. Guardar en JSON")
        print("4. Salir")
        opcion = input("Seleccionar una opción: ")

        if opcion == "1":
            buscar_jugador()
        elif opcion == "2":
            agregar_jugador()
        elif opcion == "3":
            guardar_en_json()
            print("Datos guardados")
        elif opcion == "4":
            print("¡Hasta la próxima!")
            break
        else:
            print("Opción invalida. Introduce 1, 2 o 3.")

menu()


