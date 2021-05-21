def ln(x: float, acc: int):
    q = (x-1)/(x+1)
    return 2 * sum((
        (q**n)/n for n in range(1, acc, 2)
    ))
