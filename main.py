from calculadora import * 

option = input("""
Seleccione una operación
1. Suma 
2. Resta
3. Division
""")

try:
    option = int(option)
except:
    print ("valor no valido")

if option not in [1,2,3]:
    print ("Valor no valido")
    exit()

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if option == 1:
    print("El resultado de la suma es:", suma(num1, num2))
elif option == 2:
    print("El resultado de la resta es:", resta(num1, num2))
elif option == 3:
    if num2 == 0:
        print("No se puede dividir por cero.")
    else:
        print("El resultado de la división es:", division(num1, num2))
