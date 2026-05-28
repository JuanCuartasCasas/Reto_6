##Reto 1 Clase 3 Programación Estrucutrada Feedback
class OperacionNoValida(Exception):
    def __init__(self, mensaje):
        super().__init__(self.mensaje)

def opera_basicas(num1,num2,operacion) :
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        return num1 / num2     

def selecciona_operacion():
    print("Selecciona la operacion a realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    opcion = input("Ingresa el numero de la operacion: ")
    if opcion == "1":
        return "+"
    elif opcion == "2":
        return "-"
    elif opcion == "3":
        return "*"
    elif opcion == "4":
        return "/"
    else:
        raise OperacionNoValida("Operacion no valida, por favor selecciona una opcion del 1 al 4")


def main():
   while True:
        try:
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
            break
        except ValueError:
            print("Por favor, ingresa un numero valido.")


   while num2 <0 or num1 <0:
        if num1 <0:
            print("El primer numero debe ser positivo")
            num1 = float(input("Ingresa el primer numero: "))
        elif num2 <0:
            print("El segundo numero debe ser positivo")
            num2 = float(input("Ingresa el segundo numero: "))        
        try:
            operacion = selecciona_operacion()
            resultado = opera_basicas(num1,num2,operacion)
            print(f"El resultado de la operacion es: {resultado}")
    
        except OperacionNoValida as e:
            print(e)

    
if __name__ == "__main__":
    main()

