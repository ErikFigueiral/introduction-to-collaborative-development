def sum_up(*lista):
    if not isinstance(lista,tuple):
        raise TypeError("The argument isn't a list")
    return sum(lista)*2
