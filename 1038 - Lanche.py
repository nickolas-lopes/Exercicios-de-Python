def calculalanche(a, b):
    '''Calcula valor do lanche'''
    lanche = 0
    if a == 1:
        lanche = 4
    elif a == 2:
        lanche = 4.5
    elif a == 3:
        lanche =  5
    elif a == 4:
        lanche = 2
    else:
        lanche = 1.5
    return lanche * b
x, y = input().split()
x = int(x)
y = int(y)
total = calculalanche(x, y)
print(f"Total: R$ {total:.2f}")
