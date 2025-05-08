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
        "Grade": 5.0
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

menu_active = True
while menu_active:
    print("MENU DE OPCIONES")
    print("1) Agregar estudiante")
    print("2) Buscar estudiante")
    print("3) Actualizar estudiante")
    print("4) Eliminar estudiante")
    print("5) Calcular promedio")
    print("6) Mostrar estudiante con notas inferiores")
    
    access = int(input("Por favor ingresa la opcion que deseas: "))
    
    if access ==1:
        print("\n--- AGREGAR ESTUDIANTE ---\n")
        
        fullname= input("Por favor ingresa nombre y apellido: ")
        print(SUCCESS +"Guardado con exito"+ RESET)
        while True:
            student_id = int(input("Por favor ingresa la Identificación (ID): "))            
            if student_id in students:
                print(WARNING + "Error: Este ID ya está registrado" + RESET)
            else:
                break
        print(SUCCESS +"Guardado con exito"+ RESET) 
                            
        while True:
            agestudent= int(input("Por favor ingresa la edad: "))            
            if agestudent<0:
                print(WARNING +"Error. Debes de ingresar una edad correcta" + RESET)
            else:
                break
        print(SUCCESS +"Guardado con exito"+ RESET)   
            
        while True:       
            try:
                gradestudent = float(input("Por favor ingresa la nota (0.0 - 5.0): "))                
                if 0.0 <= gradestudent <= 5.0:
                    break
                print(WARNING +"Error: La nota debe estar entre 0.0 y 5.0" + RESET)
            except ValueError:
                print("Error: Debe ingresar un número válido")
        print(SUCCESS +"Guardado con exito"+ RESET)
        
        
        students[student_id]={
            "Name": fullname,
            "Age": agestudent,
            "Grade": gradestudent
        }
        
    if access == 2:
        print("\n--- BUSCAR ESTUDIANTE ---")
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
        print(SUCCESS +"Busqueda con exito"+ RESET)
            
    
    
        
