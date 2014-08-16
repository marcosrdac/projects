def primosAte(valorMaximo, show=None):
    '''
    retorna uma lista de primos
    '''
    listaDePrimos = []
    numero = 1
    while numero <= valorMaximo:
        if all(numero % primo != 0 for primo in listaDePrimos):
            if not(numero == 1):
                listaDePrimos.append(numero)
                if show:
                    print(numero)
        numero += 1
    return(listaDePrimos)


if __name__ == '__main__':
    valorMaximo = raw_input('Digite o valor maximo de busca: ')
    primosAte(valorMaximo, True)
