from pymongo import collection

def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://nunescode:802573aO@cluster0.zcak6kf.mongodb.net/?retryWrites=true&w=majority"

    client = MongoClient(CONNECTION_STRING)

    print("Conectado com sucesso!")
    return client['soul_code_data']

'''
dbname = get_database()
collection_name = dbname["itens_soulcode"]

item_1 = {
    "_id":"SC001",
    "nome_item":"livro",
    "desconto_maximo":"10%",
    "REF":"RG2392912X",
    "preco": 250,
    "categoria":"Físico"
}

item_2 = {
    "_id": "SC002",
    "nome_item":"Camera",
    "desconto_maximo":"15%",
    "REF":"RG210023X",
    "preco": 600,
    "categoria":"Físico"
}

item_3 = {
    "_id":"SC003",
    "nome_item":"Curso",
    "desconto_maximo":"20%",
    "REF":"RG390293X",
    "preco": 100,
    "categoria":"Digital"
}

item_4 = {
    "_id": "SC004",
    "nome_item":"Aula Remota",
    "desconto_maximo":"25%",
    "REF":"RG8374621X",
    "preco": 440,
    "categoria":"Físico"
}

item_5 = {
    "_id": "SC005",
    "nome_item":"Carregador",
    "desconto_maximo":"5%",
    "REF":"RG1100293X",
    "preco": 330,
    "categoria":"Físico"
}
'''

# // # 
# inserir itens
# collection_name.insert_many([item_1, item_2, item_3])
# collection_name.insert_one(item_4)
# collection_name.insert_one(item_5)
# print("Dados inseridos!")


# Crie uma base de dados MongoDB contendo as seguintes coleções e suas respectivas quantidades de documentos:

#Coleções
#Livros: 20 documentos.
#Revistas: 15 documentos.
#Jornais: 15 documentos.
#Mangás: 10 documentos.

#Todos os documentos devem ter pelo menos 4 campos.
#Deverá haver documentos com mais e menos campos que os demais.
#Deverá haver _id do tipo Object e declarados pelo usuário.
#Devem haver campos dos tipos: Int, Double, String, ObjectId.

dbname = get_database()
collection_name = dbname["livros"]

item1 = {
    "_id":"CN001",
    "nome_item":"Curso Nutrição",
    "desconto":"20%",
    "preco": 399,
    "categoria":"Digital",
    "avaliacao": 4.2
}

item2 = {
    "_id":"CN002",
    "nome_item":"A Culpa É Das Estrelas",
    "desconto":"10%",
    "preco": 100,
    "categoria":"Físico",
    "avaliacao": 4.8
}

item3 = {
    "_id":"CN003",
    "nome_item":"E-Book",
    "desconto":"5%",
    "preco": 20,
    "categoria":"Digital",
    "avaliacao": 3.2
}

item4 = {
    "_id":"CN004",
    "nome_item":"JooJ",
    "desconto":"12%",
    "preco": 99,
    "categoria":"Físico",
    "avaliacao": 2.4
}

item5 = {
    "_id":"CN005",
    "nome_item":"Minha Profissão",
    "desconto":"50%",
    "preco": 287,
    "categoria":"Digital",
    "avaliacao": 3.8
}

item6 = {
    "_id":"CN006",
    "nome_item":"This Life",
    "desconto":"20%",
    "preco": 129,
    "categoria":"Físico",
    "avaliacao": 4.4
}

item7 = {
    "_id":"CN007",
    "nome_item":"Nature Things",
    "desconto":"15%",
    "preco": 65,
    "categoria":"Físico",
    "avaliacao": 4.6
}

item8 = {
    "_id":"CN008",
    "nome_item":"O Amor",
    "desconto":"25%",
    "preco": 145,
    "categoria":"Digital",
    "avaliacao": 4.3
}

item9 = {
    "_id":"CN009",
    "nome_item":"The Best",
    "desconto":"5%",
    "preco": 30,
    "categoria":"Digital",
    "avaliacao": 3.5
}

item10 = {
    "_id":"CN010",
    "nome_item":"Ruby On Rails",
    "desconto":"11%",
    "preco": 299,
    "categoria":"Físico",
    "avaliacao": 4.9
}
