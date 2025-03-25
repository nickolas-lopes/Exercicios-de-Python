a, b = input().split()
a = int(a)
b = int(b)
resto1 = a % b
resto2 = b % a
if resto1 == 0 or resto2 == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

 
