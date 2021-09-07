def imprimir_numero_recursivo(num: int):
    if num < 5:
        print(num)
        imprimir_numero_recursivo(num + 1)


imprimir_numero_recursivo(0)


def imprimir_numero_recursivo2(num: int):
    if num < 5:
        imprimir_numero_recursivo2(num + 1)
        print(num)


imprimir_numero_recursivo2(0)


def soma(m: int, n: int) -> int:
    if m == n:
        return m
    else:
        return m + soma(m + 1, n)


soma(1, 5)


def fib_rec(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_ite(n: int) -> int:
    i: int = 1
    fib: int = 1
    anterior: int = 0
    while i < n:
        temp = fib
        fib = fib + anterior
        anterior = temp
        i += 1
    return fib
