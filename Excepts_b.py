
def es_palindromo(wrd):
    wrd = wrd.lower()
    """ if wrd == wrd[::-1]:
        print("La palabra es un palindromo")
    else:
        print("La palabra no es un palindromo")
    """
    for i in range(len(wrd)):
        if wrd[i] != wrd[-(i+1)]: #  -len(wrd)-1-i es el indice del caracter simetrico al i-esimo caracter
            print("La palabra no es un palindromo")
            return
    print("La palabra es un palindromo")

def main():
    try:
        wrd = input("Ingresa una palabra: ")
        es_palindromo(wrd)
    
    except ValueError as e:
        print("Valor invalido: ", e)

if __name__ == "__main__":
    main()