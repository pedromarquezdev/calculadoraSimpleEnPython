def main():
    suma = 0
    resta = 0
    multiplicacion = 0
    division = 0
    
    while True :
        print("Calculadora simple!")
               
        print("1)Suma.")
        print("2)Resta.")
        print("3)Multiplicación.")
        print("4)División.")
        print("5)Salir del programa.")
        
        opcion = input("Elija la operación que desea hacer: ")
        
        if opcion.strip() == "" or not opcion.isdigit():
            print("Opción no válida. Ingrese una de las opciones de la 1 a la 5.\n")
            continue 
        
        opcion = int(opcion)    
            
        if(opcion) == 1:
            num1 = int(input("Escriba el primer número: "))
            num2 = int(input("Escriba el segundo número: "))
            suma = num1 + num2
            print(f"Resultado de {num1} + {num2} = {suma}\n")
        elif opcion == 2:
            num1 = int(input("Escriba el primer número: "))
            num2 = int(input("Escriba el segundo número: "))
            resta = num1 - num2
            print(f"Resultado de {num1} - {num2} = {resta}\n")
        elif opcion == 3:
            num1 = int(input("Escriba el primer número: "))
            num2 = int(input("Escriba el segundo número: "))
            multiplicacion = num1 * num2
            print(f"Resultado de {num1} * {num2} = {multiplicacion}\n")
        elif opcion == 4:
            num1 = int(input("Escriba el primer número: "))
            num2 = int(input("Escriba el segundo número: "))
            if num2 != 0:
                division = num1 / num2
                print(f"Resultado de {num1} / {num2} = {division}\n")
            else:
                print("No es posible dividir por cero.\n")
            
        elif opcion == 5:
            print("Saliendo del programa. . .\n")
            break
        else:
             print("Opción no válida. Intente de nuevo.\n")
main()