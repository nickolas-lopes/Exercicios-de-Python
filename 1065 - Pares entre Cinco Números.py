a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
quant_pares = 0
if a % 2 == 0:
    quant_pares += 1
if b % 2 == 0:
    quant_pares += 1
if c % 2 == 0:
    quant_pares += 1
if d % 2 == 0:
    quant_pares += 1
if e % 2 == 0:
    quant_pares += 1
print(f"{quant_pares} valores pares")
