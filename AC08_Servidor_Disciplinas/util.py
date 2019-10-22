from flask import jsonify


class NotFoundError(Exception):
    pass

database = dict()
database['ALUNO'] = []
database['PROFESSOR'] = []
database['DISCIPLINA'] = []

def erro(texto):
    return jsonify({'erro':texto})

#essa funcao nao esta em uso para professor e aluno, mas
#fica interessante para disciplina
def verifica_campos(dicionario,campos_inteiros=[], campos_texto=[], campos_data=[],campos_opcionais=[]):
    for campo in campos_inteiros+campos_texto+campos_data:
        if campo not in dicionario and campo not in campos_opcionais:
            return False,jsonify({'erro':campo+' faltando'})
    for campo in campos_inteiros:
        try:
            if campo in dicionario:
                int(dicionario[campo])
        except ValueError:
            return False, erro(campo+' deve ser inteiro')
    return True,''


def localiza(id_item,nome_lista):
    lista = database[nome_lista]
    for el in lista:
        if el['id'] == id_item:
            return el
    raise NotFoundError

def remove(elemento, database_name):
    database[database_name].remove(elemento)
    dic = {}
    dic['removido'] = True
    dic[database_name.lower()] = elemento
    return dic

def adiciona(elemento, database_name):
    database[database_name].append(elemento)

def all_for_database(database_name):
    return database[database_name]

def reseta():
    for chave in database:
        database[chave] = []
