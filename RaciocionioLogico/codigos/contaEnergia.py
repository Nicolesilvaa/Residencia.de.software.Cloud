def calculaContaEnegia(kw):
    consumo = kw * 0.56
    acrescimoBandeira = kw * 0.015
    geracaoEnergia = consumo * (41/100)
    imposto = consumo * (21.52/100)

    valorFinal = consumo + acrescimoBandeira + geracaoEnergia + imposto
    return valorFinal

kw = int(input("Olá, usuário. Digite o número de KW/h que você consome de energia\n"))
print("O valor da sua conta de energia é: {:,.2f}".format(calculaContaEnegia(kw)),"$")
