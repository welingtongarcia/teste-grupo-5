"""Exemplo didatico: calcula o valor de uma compra."""


def calcular_total(preco, quantidade):
    if preco < 0:
        raise ValueError("Preco nao pode ser negativo")
    if quantidade < 0:
        raise ValueError("Quantidade nao pode ser negativa")
    return round(preco * quantidade, 2)
