print("Hola, buenas esta es una calculadora, se pedirá al principio si quiere realizar alguna operación, tendrá que responder con si/yes como quiera o decir no para cerrar el programa\n")
print("==========================================================")
funciones = {'11':'SUMA','21':'RESTA','31':'MULTIPLICACIÓN','41':'DIVISIÓN','51':'EXPONENCIACIÓN'}
print("AVISO! Esta calculadora solo realiza las funciones de:", funciones['11'],",",funciones['21'],",",funciones['31'],",",funciones['41'],"y",funciones['51'],"por lo que otras funciones no irán o las rechazará")
def sumar():
    suma = num1 + num2
    print(suma)
def restar():
    resta = num1 - num2
    print(resta)
def multiplicacion():
    mult = num1 * num2
    print(mult)
def division():
    div = num1 / num2
    print(div)
def exponenciacion():
    exp = num1 ** num2
    print(exp)

while True:
    try:
        x=input("\nQuiere realizar una operacion con esta calculadora? :")
        if x == 'no' or x == 'NO' or x == 'No' or x == 'n' or x == 'N' or x == 'nO':
            break
        elif x == 'yes' or x == 'y' or x == 'Yes' or x == 'ye' or x == 'YES' or x == 'Y' or x == 'si' or x == 's' or x == 'Si' or x == 'sI' or x == 'SI':
            num1=int(input("\nIntroduzca el primer numero: "))
            num2=int(input("Introduzca el segundo numero: "))
            print("\nSe van a realizar diferentes tipos de funciones entre ellas estan: \n","1. Suma\n","2. Resta\n","3. Multiplicación\n","4. División\n","5. Exponenciación\n")  
            opc=input("Elija la función que quiere realizar: ")
            if opc=="1":
                print("\nLa función que ha elegido ha sido la suma, el resultado es: ")
                sumar()
            elif opc=="2":
                print("\nLa función que ha elegido ha sido la resta, el resultado es: ")
                restar()
            elif opc=="3":
                print("\nLa función que ha elegido ha sido la multiplicación, el resultado es: ")
                multiplicacion()
            elif opc=="4":
                print("\nLa función que ha elegido ha sido la división, el resultado es: ")
                division()
            elif opc=="5":
                print("\nLa función que ha elegido ha sido la exponenciación, el resultado es: ")
                exponenciacion()
            else:
                print("Has puesto una número que no esta entre los mencionados anteriormente")
        else:
            print("\nHas introducido mal si/no")
    except ValueError:
        print("Algo ocurrió mal.")

    
        
