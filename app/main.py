from random import random
import pymysql


class Produto():
    def __init__(self, nome, espaco, valor):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor


class Individuo():
    def __init__(self, espacos, valores, limite_espacos, geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos
        self.nota_avaliacao = 0
        self.espaco_usado = 0
        self.geracao = geracao
        self.cromossomo = []

        for i in range(len(espacos)):
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")

    def avaliacao(self):
        nota = 0
        soma_espacos = 0
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == '1':
                nota += self.valores[i]
                soma_espacos += self.espacos[i]
        if soma_espacos > self.limite_espacos:
            nota = 1
        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos



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