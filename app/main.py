import pymysql

class Produto():
    def __init__(self, nome, espaco, valor):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor

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
