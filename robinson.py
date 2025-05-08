students = {
    1097238530: {
        "Name": "Jeison David Olaya Ariza",
        "Age": 28,
        "Grade": 4.8
    },
    1097230473: {
        "Name": "Cristian Andres Martinez",
        "Age": 22,
        "Grade": 4.4        
    },
    123456789: {
        "Name": "Marcos Julian Lopez",
        "Age": 20,
        "Grade": 2.5       
    },
    987654321: {
        "Name": "Juliana Martinez",
        "Age": 23,
        "Grade": 2.0
    },
    1096219307: {
        "Name": "Keyla Kahterine Murallas",
        "Age": 30,
        "Grade": 4.6
    }
}

DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"

def menu() : 
    print("MENU DE OPCIONES")
    print("1) Agregar estudiante")
    print("2) Buscar estudiante")
    print("3) Actualizar estudiante")
    print("4) Eliminar estudiante")
    print("5) Calcular promedio")
    print("6) Mostrar estudiante con notas inferiores")
    return int(input("seleccionar una opcion"))

def case1():
     while True:
                nombre = input("Dame tu nombre: ")
                apellido = input("Dame tu apellido: ")
                edad = int(input("Dame tu edad: "))
                identificacion = int(input("Dame tu identificacion: "))
                nota = float(input("Dame la nota (0.0): "))
                if identificacion in students:
                    print("Ese numero ya existe")
                else:    
                    students[identificacion] = {
                        "Name": nombre + " " +apellido,
                        "Age": edad,
                        "Grade": nota    
                    }
                    print("El usuario se ha registrado correctamente.")
                    break        
                print(students)
menu1 = True

while menu1:
    respuesta = menu()
     
    match respuesta:
        case 1:
           case1()
        case 4: 
             print("\033[91m Estas a punto de eliminar un usuario :O \033[0m")   
             identificacion = int(input("Ingresa la identificacion de la persona a eliminar: "))
             
             existe = students.get(identificacion)
             if existe: 
                students.pop(identificacion)
                print("Se ha eliminado correctamente..")
             else: 
                 print("Eyyy no existe :(")   
        case 5:   
            counter = 0
            promedio = 0.0
            for student in students.values():
                counter = counter + 1
                print(student["Grade"])
                promedio = promedio + student["Grade"]
            
            total = promedio/counter    
            print(f"el promedio de tu grupo es de: {total} ")
                
        case 6:
            for student in students.values():
                if  float(student["Grade"]) < 3.0 : 
                    print(f"Este personaje va perdiendo :( {student['Name']} --- {student['Grade']}")
                
            
            