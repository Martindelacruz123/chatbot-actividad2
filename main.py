print("Bienvenido. ¿En qué te puedo ayudarte?")

print("Cuento con estas funciones: \n")
print("1. Menú")
print("2. Promociones")
print("3. Horario \n")
print("¿Qué opción deseas? (Escribe el numero)")

option = int(input())

menu = ["Quesadillas", "Torta de Jamón", "Hot Cakes", "Huevo con chorizo", "Spaguetti"]

promociones = ["Martes 2x1", "Viernes de HotCakes", "Lunes de 3x2"]

horario = {

    "Lunes": "9am a 1pm",
    "Martes": "9am a 12pm",
    "Miercoles": "9am a 2pm",
    "Jueves": "9am a 3pm",
    "Viernes": "9am a 1pm",

}

def mostrar_lista(lista):
    contador =1
    for dato in lista:
        print (f"{contador} - {dato}")
        contador+=1

    print("¿necesitas ayuda con algo mas?")
    print("1. Si")
    print("2. No")
    repetir = int(input())
    if repetir == 2:
        print("tenga buen dia")
    elif repetir == 1:
        while repetir <= 1 or repetir >= 1:
            print("Cuento con estas funciones: \n")
            print("1. Menú")
            print("2. Promociones")
            print("3. Horario \n")
            print("¿Qué opción deseas? (Escribe el numero)")

            option = int(input())


if option == 1:
    print("Elegiste el servicio de Menú")
    mostrar_lista(menu)

elif option == 2:
    print("Elegiste el servicio de promociones")
    mostrar_lista(promociones)

elif option == 3:
    print("Elegiste el servicio de horarios")
    print('Nuestro horario es')

    for dia, horario in horario.items():
        print(f'{dia} - {horario}')


else:
    print("No elegiste una opción, vuelve a elegirlo.")

#no me funciono bien el while :(