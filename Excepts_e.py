def mismos_caracteres(lista):
    lista_ordenada = []
    for i in range(len(lista)-1):
        if sorted(str(lista[i])) == sorted(str(lista[i+1])):
            lista_ordenada.extend((lista[i], lista[i+1]))
    return lista_ordenada

def main():
    lista = []
    long = int(input("Ingresa la longitud de la lista: "))
    for i in range(long):
        flag = True
        while flag:
            try:
                valor = int(input(f"Ingresa el elemento {i+1}: "))
                lista.append(valor)
                flag = False
            except ValueError:
                print("Por favor, ingresa un numero valido.")
    lista_final  = mismos_caracteres(lista)
    print(f" la lista final es: {lista_final}")


if __name__ == "__main__":
    main()