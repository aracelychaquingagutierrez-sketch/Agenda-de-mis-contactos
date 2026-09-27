# Agenda personal-Aracely Chaquiga
contactos = {
    "Aracely Chaquinga": "0993641772",
    "celso Cuchan": "0958830449"
}

def menu():
    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Guardar o actualizar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar un contacto")
    print("4. Eliminar un contacto")
    print("5. Salir")

# Bucle principal del programa
while True:
    menu()
    opcion = input("\nElige una opción (1-5): ").strip()

    if opcion == "1":
        # Insertar / Agregar datos
        nombre = input("Nombre de la persona: ").strip().title()
        if not nombre:
            print("Debes ingresar un nombre válido.")
            continue
        telefono = input("Número de teléfono: ").strip()
        
        contactos[nombre] = telefono
        print(f"Listo, se guardó el contacto de {nombre}.")

    elif opcion == "2":
        # Mostrar la información
        print("\n--- MIS CONTACTOS ---")
        if len(contactos) == 0:
            print("No hay contactos guardados todavía.")
        else:
            for nombre, telefono in contactos.items():
                print(f"- {nombre}: {telefono}")

    elif opcion == "3":
        # Buscar contacto
        nombre = input("¿A quién quieres buscar?: ").strip().title()
        if nombre in contactos:
            print(f"Teléfono de {nombre}: {contactos[nombre]}")
        else:
            print(f"No encontré a '{nombre}' en la agenda.")

    elif opcion == "4":
        # Eliminar contacto
        nombre = input("¿A quién deseas borrar?: ").strip().title()
        if nombre in contactos:
            del contactos[nombre]
            print(f"Se eliminó a {nombre} de tus contactos.")
        else:
            print(f"No se pudo eliminar, '{nombre}' no existe.")

    elif opcion == "5":
        print("Saliendo del programa... ¡Hasta luego!")
        break

    else:
        print("Opción no válida, intenta de nuevo.")