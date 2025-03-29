
dias = int(input())
anos = dias // 365 
meses = dias // -30 
dias_vida = dias - 365 * anos - 30 * meses
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias_vida} dia(s)")
