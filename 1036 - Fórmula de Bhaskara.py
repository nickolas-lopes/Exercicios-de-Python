a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
def calc_delta(a, b, c):
    delta = b**2 - 4 * a * c
    return delta
delta = calc_delta(a, b, c)
if a == 0:
    print('Impossivel calcular')
else:
    r1 = (-b + delta ** (1 / 2)) / (2 * a)
    r2 = (-b - delta ** (1 / 2)) / (2 * a)
    if delta < 0:
        print('Impossivel calcular')
    elif delta > 0:
        print(f'R1 = {r1:.5f}')
        print(f'R2 = {r2:.5f}')

