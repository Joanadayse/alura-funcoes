# Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das 
# quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

# O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de 
# carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios 
# e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

# Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente 
# [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel 
# (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com 
# passeio e alimentação (gasto_passeio).

# Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. 
# Considere a viagem de ida e volta de carro.

# "Com base nos gastos definidos,"
# " uma viagem de [dias] dias para [cidade] "
# "saindo de Recife custaria [gastos] reais"

dias = int(input("Quantas diárias? "))
cidade = input("Qual a cidade? [Salvador, Fortaleza, Natal ou Aracaju]: ")
distancias = [850, 800, 300, 550]
passeio = [200, 400, 250, 300]
km_l = 14
gasolina = 5

def gasto_hotel(dias):
    return 150 * dias

def gasto_gasolina(cidade):
    if cidade == "Salvador":
        return (2 * distancias[0] * gasolina) / km_l
    elif cidade == "Fortaleza":
        return (2 * distancias[1] * gasolina) / km_l
    elif cidade == "Natal":
        return (2 * distancias[2] * gasolina) / km_l
    elif cidade == "Aracaju":
        return (2 * distancias[3] * gasolina) / km_l
    else:
        return 0  # Retorna 0 caso a cidade não seja válida

def gasto_passeio(cidade, dias):
    if cidade == "Salvador":
        return passeio[0] * dias
    elif cidade == "Fortaleza":
        return passeio[1] * dias
    elif cidade == "Natal":
        return passeio[2] * dias
    elif cidade == "Aracaju":
        return passeio[3] * dias
    else:
        return 0  # Retorna 0 caso a cidade não seja válida

gastos = gasto_hotel(dias) + gasto_gasolina(cidade) + gasto_passeio(cidade, dias)
print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {round(gastos, 2)} reais")
