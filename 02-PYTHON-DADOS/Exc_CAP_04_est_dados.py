# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

num = [1,2,3,4,5,6,7,8,9,10]
print(num)
# output 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela

lista = ["Cachorro","Gato","Papagaio","Aranha","Camelo"]
print(lista)
#output
['Cachorro', 'Gato', 'Papagaio', 'Aranha', 'Camelo']

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
 
string1 = "Amo "
string2 = "Cachorro!"
string3 = string1 + string2
print(string3)
#output
Amo Cachorro!

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

tupla = (1,2,2,3,4,4,4,5)
tupla.count(4)
#output
3

# Exercício 5 - Crie um dicionário vazio e imprima na tela

dicionario = {}
print(dicionario)
#output
{}

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela

dicionario = {"Carlos":22,"Vitor":20,"Luana":19}
print(dicionario)
#output
{'Carlos': 22, 'Vitor': 20, 'Luana': 19}

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela

dicionario = {"Carlos":22,"Vitor":20,"Luana":19}
dicionario["Lucas"] = 18
print(dicionario)
#output
{'Carlos': 22, 'Vitor': 20, 'Luana': 19, 'Lucas': 18}

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dicionario = {"Val1":4,"Val2":[1,3,4,5],"Val3":5}
print(dicionario)
#output
{'Val1': 4, 'Val2': [1, 3, 4, 5], 'Val3': 5}

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.

lista = ["String",(1,2),{"Lucas":18,"Carlos":20},1.22]
print(lista)
#output
['String', (1, 2), {'Lucas': 18, 'Carlos': 20}, 1.22]

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.

frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print (frase[0:19])
#output
Cientista de Dados 