import pymysql
from random import random


class Produto():
    def __init__(self, nome, espaco, valor):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor

class Individuo():
    def __init__(self, espacos, valores, limite_espacos, geracao=0)
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos
        self.nota_avaliacao = 0
        self.geracao = geracao
        self.cromossomo = []

        # seleciona qual produto sera carregado
        for i in range(len(espacos)):
            if random() < 0.5:   # 0.5 significa que ha 50% de chance de dar 0 e 50% de chance de dar 1
                self.cromossomo.append('0')
            else:
                self.cromossomo.append('1')



if __name__ == '__main__':
    lista_produtos = []
    conexao = pymysql.connect(host='localhost', user='root', password='@Regi371227', database='produtos')
    cursor = conexao.cursor()
    cursor.execute('SELECT nome, espaco, valor, quantidade FROM produtos')
    for produto in cursor:
        for i in range(produto[3]):
            lista_produtos.append(Produto(produto[0], produto[1], produto[2]))

    cursor.close()
    conexao.close()
