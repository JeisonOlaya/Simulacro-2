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
    return int(input("seleccionar una opcion: "))

def case1():
     while True:
                print("\n--- AGREGAR ESTUDIANTE ---\n")
                nombre = input("Ingresa tu nombre: ")
                apellido = input("Ingresa tu apellido: ")
                print(SUCCESS +"Nombre y Apellido guardado con exito"+ RESET)
                while True:
                    agestudent = int(input("Ingresa tu edad: "))
                    if agestudent<0:
                        print(WARNING +"Error. Debes de ingresar una edad correcta" + RESET)
                    else:
                        print(SUCCESS +"Guardado con exito"+ RESET)
                        break
                while True:
                    try:
                        gradestudent = float(input("Por favor ingresa la nota (0.0 - 5.0): "))                
                        if 0.0 <= gradestudent <= 5.0:
                            break
                        print(WARNING +"Error: La nota debe estar entre 0.0 y 5.0" + RESET)
                    except ValueError:
                        print("Error: Debe ingresar un número válido")
                print(SUCCESS +"Guardado con exito"+ RESET)
                        
                identificacion = int(input("Ingresa tu identificacion: "))
                if identificacion in students:
                    print(WARNING + "Error: Este ID ya está registrado" + RESET)
                else:    
                    students[identificacion] = {
                        "Name": nombre + " " +apellido,
                        "Age": agestudent,
                        "Grade": gradestudent    
                    }
                    print(SUCCESS +"El usuario se ha registrado correctamente."+ RESET)
                    break        
                print(students)
def case2():
    print("\n--- BUSCAR ESTUDIANTE ---")
    while True:
        try:
            search_id = int(input("Ingrese el ID del estudiante: "))
            if search_id in students:
                print("\nInformación del estudiante:")
                print(f"ID: {search_id}")
                print(f"Nombre: {students[search_id]['Name']}")
                print(f"Edad: {students[search_id]['Age']}")
                print(f"Nota: {students[search_id]['Grade']}")
            else:
                print(WARNING +"No se encontró ningún estudiante con ese ID"+ RESET)
        except ValueError:
                print(WARNING +"Error: El ID debe ser un número"+ RESET)
                break
        print(SUCCESS +"Busqueda con exito"+ RESET)
             
def case3():
        print("\n--- ACTUALIZAR ESTUDIANTE ---")
        identity=input("Por favor ingresa el ID del estudiante a actualizar: ")
        actu=int(input("1) actualizar edad\n2) actualizar nota: \n"))

        if actu==1:
            while True:
                Age=int(input("Por favor ingresa la nueva edad: "))
                if Age<0:
                    print(WARNING +"Error. Debes de ingresar una edad correcta" + RESET)
                else:
                    students[int(identity)].update({"Age": Age})
                    print(SUCCESS +"Dato actualizado con exito"+ RESET)

                    student= students.get(int(identity),{})
                    print(f"Nombre: {student.get('Name')}")
                    print(f"Edad: {student.get('Age')}")
                    print(f"Nota: {student.get('Grade')}")
                    break
        if actu==2:
            while True:             
                grade=float(input("Por favor ingresa la nota nueva: "))
                if 0.0 <= grade >= 5.0:
                    print(WARNING +"Error. Debes de ingresar una nota correcta" + RESET)
                else: 
                    students[float(identity)].update({"Grade":grade})
                    print(SUCCESS +"Dato actualizado con exito"+ RESET)

                    student=students.get(float(identity),{})
                    print(f"Nombre: {student.get('Name')}")
                    print(f"Edad: {student.get('Age')}")
                    print(f"Nota: {student.get('Grade')}")
                    break          
                    
def case4():
        print(WARNING +" Estas a punto de eliminar un usuario :O "+ RESET)   
        identificacion = int(input("Ingresa la identificacion de la persona a eliminar: "))
             
        existe = students.get(identificacion)
        if existe: 
            students.pop(identificacion)
            print("Se ha eliminado correctamente..")
        else: 
            print("Eyyy no existe :(")
                
def case5():
    counter = 0
    promedio = 0.0
    for student in students.values():
        counter = counter + 1
        print(student["Grade"])
        promedio = promedio + student["Grade"]
            
        total = promedio/counter    
        print(f"el promedio de tu grupo es de: {total} ")
         
def case6():
    for student in students.values():
        if  float(student["Grade"]) < 3.0 : 
            print(f"Este personaje va perdiendo :( {student['Name']} --- {student['Grade']}")
               
menu1 = True

while menu1:
    answer = menu()
     
    match answer:
        case 1:
           case1()
        case 2:
            case2()
        case 3:
            case3()
        case 4: 
            case4()  
        case 5:   
           case5()
                
        case 6:
            case6()
                
            
            