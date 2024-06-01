def agregar_alumno(datos_escuela, nombre, apellido, dni, fecha_nacimiento, tutor):
    alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }
    datos_escuela["Alumnos"].append(alumno)

def mostrar_datos_alumno(alumno):
    print("Nombre:", alumno["Nombre"])
    print("Apellido:", alumno["Apellido"])
    print("DNI:", alumno["DNI"])
    print("Fecha de nacimiento:", alumno["Fecha de nacimiento"])
    print("Tutor:", alumno["Tutor"])
    print("Notas:", alumno["Notas"])
    print("Faltas:", alumno["Faltas"])
    print("Amonestaciones:", alumno["Amonestaciones"])

def modificar_datos_alumno(alumno, nombre=None, apellido=None, dni=None, fecha_nacimiento=None, tutor=None):
    if nombre:
        alumno["Nombre"] = nombre
    if apellido:
        alumno["Apellido"] = apellido
    if dni:
        alumno["DNI"] = dni
    if fecha_nacimiento:
        alumno["Fecha de nacimiento"] = fecha_nacimiento
    if tutor:
        alumno["Tutor"] = tutor

def expulsar_alumno(datos_escuela, dni):
    for alumno in datos_escuela["Alumnos"]:
        if alumno["DNI"] == dni:
            datos_escuela["Alumnos"].remove(alumno)
            print("Alumno expulsado correctamente.")
            return
    print("No se encontró ningún alumno con ese DNI.")

# Ejemplo de uso
datos_escuela = {"Alumnos": []}

while True:
    comando = input("Ingrese el comando (agregar, mostrar, modificar, expulsar, salir): ").lower()

    if comando == "agregar":
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        dni = input("Ingrese el DNI del alumno: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (YYYY-MM-DD): ")
        tutor = input("Ingrese el nombre del tutor del alumno: ")
        agregar_alumno(datos_escuela, nombre, apellido, dni, fecha_nacimiento, tutor)
        print("Alumno agregado correctamente.")
    
    elif comando == "mostrar":
        dni = input("Ingrese el DNI del alumno a mostrar: ")
        for alumno in datos_escuela["Alumnos"]:
            if alumno["DNI"] == dni:
                print("Datos del alumno:")
                mostrar_datos_alumno(alumno)
                break
        else:
            print("No se encontró ningún alumno con ese DNI.")

    elif comando == "modificar":
        dni = input("Ingrese el DNI del alumno a modificar: ")
        for alumno in datos_escuela["Alumnos"]:
            if alumno["DNI"] == dni:
                print("Datos actuales del alumno:")
                mostrar_datos_alumno(alumno)
                nombre = input("Ingrese el nuevo nombre del alumno (deje en blanco para mantener el actual): ")
                apellido = input("Ingrese el nuevo apellido del alumno (deje en blanco para mantener el actual): ")
                nuevo_dni = input("Ingrese el nuevo DNI del alumno (deje en blanco para mantener el actual): ")
                fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del alumno (YYYY-MM-DD) (deje en blanco para mantener la actual): ")
                tutor = input("Ingrese el nuevo tutor del alumno (deje en blanco para mantener el actual): ")
                modificar_datos_alumno(alumno, nombre, apellido, nuevo_dni, fecha_nacimiento, tutor)
                print("Datos del alumno modificados correctamente.")
                break
        else:
            print("No se encontró ningún alumno con ese DNI.")

    elif comando == "expulsar":
        dni = input("Ingrese el DNI del alumno a expulsar: ")
        expulsar_alumno(datos_escuela, dni)

    elif comando == "salir":
        print("¡Hasta luego!")
        break

    else:
        print("Comando no válido.")
    