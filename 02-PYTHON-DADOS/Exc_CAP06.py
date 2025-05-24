# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
lista = [2,3,4]
lista = [pow(i,3) for i in lista]
print(lista)

# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)
#
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()
res = (map(lambda x:[x.upper(), x.lower(), len(x)],palavras))
for i in res:
    print(i)

# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],
          [3,4],
          [5,6],
          [7,8]]
transp = [list(linha) for linha in zip(*matrix)]
print(transp)

# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]

listaf = [[i**2,i**3] for i in lista]
print(listaf)

#UTILIZANDO LISTA DE FUNÇAO
lista = [0, 1, 2, 3, 4]

def square(x):
        return (x**2)
    
def cube(x):
        return (x**3)

funcs = [square, cube]

for i in lista:
    valor = map(lambda x: x(i), funcs)
    print(list((valor)))

# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]

res = list(map(lambda x,y:pow(x,y),listaA,listaB))
print(res)

# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar 
# apenas os valores negativos.
l = range(-5, 5)

res = list(filter(lambda x:x <=0,l))
print(res)

# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

res = list(filter(lambda x:x in b,a))
print(res)

# Exercício 8 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

dictf = dict(zip(dict1,dict2.values()))
print(dictf)

# Exercício 9 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

res = [lista[i] for i in range(len(lista)) if i > 5]
print(res)

# Exercício 10 - Crie um regex em Python para extrair a palavra que aparece depois das palavras 
# Data e Science na frase: 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'
import re
texto = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'

res = re.findall(r'Data Science\s(\w+)',texto)
print(res[0])

