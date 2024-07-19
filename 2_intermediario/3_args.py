def somador(*args):
    somador = 0
    for arg in args:
        print(arg)
        somador += arg
    
    print(somador)


somador(1, 2, 3)