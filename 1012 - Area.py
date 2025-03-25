a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
tri = a * c / 2
circ = 3.14159 * c**2
trap = (a + b) * c / 2
quad = b ** 2
ret = a * b
print(f"TRIANGULO: {tri:.3f}\nCIRCULO: {circ:.3f}\nTRAPEZIO: {trap:.3f}\nQUADRADO: {quad:.3f}\nRETANGULO: {ret:.3f}")
