def fiboseq(n):
    '''
    Retorna uma lista da sequencia de Fibonacci com n numeros de algarismos.
    '''
    lista = []
    v = 1
    for i in range(n):
        try:
            v = lista[-1] + lista[-2]
        except:
            v = 1
        lista.append(v)
    return(lista)


def fiboseqate(n):
    '''
    Retorna uma lista da sequencia de Fibonacci com numeros menores que n.
    '''
    lista = []
    v = 1
    while (v < n):
        try:
            v = lista[-1] + lista[-2]
        except:
            v = 1
        if v < n:
            lista.append(v)
    return(lista)
