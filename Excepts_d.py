

def mayor_suma(lista)-> int:
    for i in range(len(lista)-1):
        if lista[i] + lista[i+1] > lista[i-1] + lista[i]:
            suma = lista[i] + lista[i+1]

    return suma
    



def main():
    lista = []
    long = int(input("Ingresa la longitud de la lista: "))
    for i in range(long):
        valor = (input(f"Ingresa el elemento {i+1}: "))
        while valor == "" or not valor.isdigit():
            print("Valor no valido, ingresa un numero entero")
        try:
            valor = int(input(f"Ingresa el elemento {i+1}: "))
        except ValueError:
            print("Por favor, ingresa un numero valido.")
            return
            
        lista.append(valor)
    resultado = mayor_suma(lista)
    print(f"La mayor suma es: {resultado}")

    
if __name__ == "__main__":
    main()