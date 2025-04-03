def calculo_dias(semana, dias):
    if dias == 0:
        return "chega hoje!"
    calc_dias = 0
    if semana == "domingo":
        calc_dias = 0
    elif semana == "segunda":
        calc_dias = 1
    elif semana == "terca":
        calc_dias = 2
    elif semana == "quarta":
        calc_dias = 3
    elif semana == "quinta":
        calc_dias = 4
    elif semana == "sexta":
        calc_dias = 5
    elif semana == "sabado":
        calc_dias = 6
    chegada = (calc_dias + dias) % 7
    if chegada == 0:
        return "sera entregue domingo"
    elif chegada == 1:
        return "sera entregue segunda"
    elif chegada == 2:
        return "sera entregue terca"
    elif chegada == 3:
        return "sera entregue quarta"
    elif chegada == 4:
        return "sera entregue quinta"
    elif chegada == 5:
        return "sera entregue sexta"
    elif chegada == 6:
        return "sera entregue sabado"
    
semana = input()
dias = int(input())
dia_da_semana = calculo_dias(semana, dias)
print(f"{dia_da_semana}")
