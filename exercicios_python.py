# Dada uma lista de emails, remover todos os duplicados.

#emails: list = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]

#email_unicos: list = list(dict.fromkeys(emails))

#print(email_unicos)

# Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

#idades: list = [22, 15, 30, 17, 18]

#maiores_idade = [idade for idade in idades if idade >= 18]

#print(maiores_idade)

#  Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

#pessoas: list = [
#    {"nome": "Zeus", "idade": 30},
#    {"nome": "Bob", "idade": 25},
#    {"nome": "Carol", "idade": 20}
#]

#pessoas.sort(key=lambda pessoa: pessoa["nome"])

#print(pessoas)


# Dado um conjunto de números, calcular a média.

#numeros: list = [10, 20, 30, 40, 50]

#media: float = sum(numeros) / len(numeros)

#print(media)


# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

#valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#pares: list = [valor for valor in valores if valor % 2 == 0]

#impares: list = [valor for valor in valores if valor % 2 != 0]


# Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

#produtos: list = [
#    {"id": 1, "nome": "Teclado", "preço": 100},
#    {"id": 2, "nome": "Mouse", "preço": 80},
#    {"id": 3, "nome": "Monitor", "preço": 300}
#]


#for produto in produtos:
#    if produto["id"] == 3:
#        produto["preço"] = 450
    
#print(produtos)

# Dados dois dicionários, fundi-los em um único dicionário.

#dicionario1 = {"a": 1, "b": 2}
#dicionario2 = {"c": 3, "d": 4}

#dicionariofinal = {**dicionario1, ** dicionario2}

#print(dicionariofinal)


# Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

#estoque: dict = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

#for produto, quantidade in estoque.items():
#    if quantidade > 0:
#        print(produto)

# Dado um dicionário, criar listas separadas para suas chaves e valores.

#dicionario = {"a": 1, "b": 2, "c": 3}

#chaves: list = list(dicionario.keys())
#valor: list = list(dicionario.values())

#print(f"Chaves: {chaves}")
#print(f"Valores: {valor}")


# Dada uma string, contar a frequência de cada caractere usando um dicionário.

#texto: str = "engenharia de dados"
#frequencia: dict = {}

#for letra in texto:
#    if letra in frequencia:
#        frequencia[letra] += 1
#    else:
#        frequencia[letra] = 1

#print(frequencia)
