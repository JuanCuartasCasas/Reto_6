def main():
    lista = []
    try:
        long = int(input("Ingresa la longitud de la lista: "))
    except ValueError:
        print("Por favor, ingresa un numero valido.")
        return
    
    for i in range(long):
        flag = True

        while flag:
            try:
                valor = (input(f"Ingresa el elemento {i+1}: "))
                valor = int(valor)
                flag = False
            except ValueError:
                print("Por favor, ingresa un numero valido.")
                
        lista.append(valor)
    print("La lista es:", lista)

    resultado =  factores_primos(lista)
    
    print(f"Los números primos son: {resultado}")


def factores_primos(lista)-> list:
    primos = []
    for num in lista: 
        if num <= 1:
            continue
        es_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False
                break    
        if es_primo:
            primos.append(num)
    return primos

if __name__ == "__main__":
    main()