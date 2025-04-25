# OPERADORES ARITMETICOS

# SOMA '+' / SUBTRAÇAO '-' / MULTIPLICAÇAO '*' / DIVISAO '/' / POTENCIA '**' / MODULO '%'
# EXEMPLOS
X = 3 + 3 / X = 3 - 3 / X = 3 * 3 / X = 3 / 3 / X = 3**3 / X = 3 % 3

#FUNÇAO 'NOMEFX(PARAMETRO)' 
#EXEMPLO

#FUNÇAO 'TYPE()' RETORNA O TIPO DO DADO
TYPE(5) or TYPE(VAR)

#OPERAÇAO COM DADO DE TIPO FLOAT
#INT com FLOAT da FLOAT (exceto divisao que devolve float entre INT)
#para forçar INT na divisao se usa o '//'

#CONVERSÃO PARA BIN/HEX
bin(129) / hex(129)

#ABS (MODULO, VALOR ABSOLUTO)
#ROUND (ARREDONDA O NUMERO EM CASAS)
#POW (POTENCIA)
abs(-10) 'retorna 10'
round(3.213412,2) 'parametro 1 - numero, parametro 2 - numero de casas'
pow(4,3) 'parametro 1 - base, parametro 2 - potencia'

#VARIAVEIS
#NAO PODE COMEÇAR NOME DA VARIAVEL COM NUMERO
#NAO PODE USAR PALAVRA RESERVADA COMO NOME (COMANDOS)

#ATRIBUINDO VALOR A VARIAVEL '='
VAR = 1

#IMPRIMINDO VARIAVEL
print(VAR) or VAR

#POSSO DECLARAR MAIS DE UMA VARIAVEL EM UMA MESMA LINHA USANDO VIRGULA
var1, var2, var3 = 'BOB', 'MARIA', 'ANA'

#OPERAÇOES ARITMETICAS SAO LIVRES COM VARIAVEIS
var3 = var2 * var1

#STRING

#USAR '\N' NA STRING DA ENTER E QUEBRA LINHA
print('Teste \n Enter1')

#INDEXIZAÇAO (posiçao das letras em uma string) COMEÇA POR 0
#VAR seguido de COLCHETES e o NUMERO DA LETRA imprime ela
var = "teste"
var[0]

#dois pontos ':' determina intervalo no index
#ao omitir apos ou antes os ':' determina tudo
#numero APOS ':' é EXCLUSIVE
var[1:]
var[:3]

#AO UTILIZAR O NEGATIVO LE AO CONTRARIO A STRING
#VAZIO AINDA SIGNIFICA TUDO E O EXCLUSIVE SE MANTEM APOS OS ':'
var[:-1]

# UTILIZANDO '::' , SINTAXE [INICIO:FIM:PASSO]
# PASSO NEGATIVO INVERTE A LEITURA
var[1:2:1]

#NAO SE PODE MODIFICAR O VALOR DE UM CARACTER DA STRING POR FORA

#STRING em python aceita aspas duplas ou simples
#PRINT para string tem que ser entre aspas
print('Teste string')

#FUNÇOES BUILT-IN 

#TUDO PRA MAIUSCULO
var.upper()

#TUDO PRA MINUSCULO
var.lower()

#QUEBRA A LINHA A CADA ESPAÇO
#POR PADRAO QUEBRA A CADA ESPAÇO, PODE ESPECIFICAR QUAL CARACTER DENTRO DO ()
var.split()

#FUNÇOES PARA STRING

#CONVERTE A PRIMEIRA LETRA PRA MAIUSCULO
var.captalize()

#CONTA QUANTAS VEZES TEM O CARACTER DEFINIDO NA STRING
var.count(a)

#RETORNA T/F BOOLEANO CASO SEJA OU NAO TODA DE NUMERO A STRING
var.isalnum()

#RETORNA T/F BOOLEANO CASO SEJA OU NAO TODA DE LETRA MINUSCULA A STRING
var.islower()

#RETORNA T/F BOOLEANO CASO SEJA OU NAO TODA DE ESPAÇO
var.isspace()

#RETORNA T/F BOOLEANO CASO TERMINE OU NAO COM A LETRA DEFINIDA COMO PARAMETRO
var.endswith('a')

#COMPARANDO DUAS STRING RETORNANDO BOOLEANO
print("Python" == "a")
False

#ESTRUTURA DE DADOS EM PYTHON !!!!!

#CRIANDO LISTA
lista = ["arroz","feijao","frango","ovo"]

#DA PRA ARMAZENAR MAIS DE UM TIPO DE DADO NA LISTA
lista = ["arroz",2,"feijao",2.1,"frango"]

#INDEXIZAÇAO EM LISTA FUNCIONA COMO NA DE STRING, MAS AO INVES DE LETRA POR LETRA É ITEM POR ITEM
#TAMBEM COMEÇA POR ZERO!!
item1 = lista[0]
item2 = lista[1]

#DIFERENTE DA STRING, PODE MODIFICAR O VALOR DE UM ITEM DENTRO DA LISTA
lista = ["arroz","feijao","frango","ovo"]
item[0] = "carne"
lista = ["carne","feijao","frango","ovo"]

#TAMBEM POSSO DELETAR UM ITEM DENTRO DA LISTA
#AO DELETAR UM ITEM A LISTA SE REORGANIZA E NAO FICA NULO O ITEM DELETADO
del lista[0]

#LISTA DENTRO DE LISTA
#ATRAVES DE VARIAVEIS DA PRA IR QUEBRANDO AS LISTAS
#EXEMPLO
lista1[[1,2,3],[4,5,6],[7,8,9,10]]
a = lista1[1]
b = a[0]

#AGORA SENDO DIRETO E MELHOR
#CADA CHAVE VAI ENTRANDO NOS SUBGRUPOS
print(lista1[1][0])

#SOMAR DUAS LISTAS MESMO NUMERICAS APENAS CONCATENA

lista = [1,3,4,5]
lista1 = [5,4,7,8,9]
x = lista + lista2 
print(x)
[1, 3, 4, 5, 5, 4, 7, 8, 9]

#TESTANDO PRA VER SE HA O ELEMENTO NA LISTA (BOOLEANO)
print(10 in lista)
false

#FUNÇOES BUILT-IN EM LISTAS

#RETORNANDO TAMANHO DA LISTA
len(lista)

#RETORNANDO VALOR MAXIMO DA LISTA
max(lista)

#RETORNANDO MENOR VALOR DA LISTA
min(lista)

#ADICIONANDO VALOR COM APPEND
#AO ADICIONAR MAIS DE UM ELE INSERE O CONJUNTO DE DADOS EM FORMA DE LISTA SEM DESEMPACOTAR
lista.append(23)

#ADICIONANDO VALORES COM EXTEND
#ADICIONAO UNITARIAMENTE
lista.extend(2,3,4)

#ADICIONANDO VALOR EM UM INDEX ESPECIFICO (EMPURRA OS DA FRENTE 1 CASA PRA FRENTE)
lista.insert(2,10) #(INDEX,VALOR)

#DELETANDO VALOR NUMA LISTA (LISTA SE REORGANIZA APOS, NAO DEIXA INDEX VAZIO)
lista.remove(10) #VALOR

#INVERTENDO ORDEM DOS INDEX
lista.reverse()

#ORDENANDO A LISTA (ASC)
lista.sort()

#CONTANDO NUMERO DE ELEMENTOS IGUAIS NA LISTA
lista.count(10)

#DESCOBRINDO INDEX DE UM VALOR EM UMA LISTA
#SOMENTE RETORNA VALOR UNITARIO
lista.index(2)

#DICIONARIO
#PODE TER CHAVE E VALOR IGUAL (EM PARES DIFERENTES)
#FUNCIONA COMO PARES, CADA VALOR TEM UMA CHAVE, AMBOS PODEM SER STRING OU VALOR NUMERICO, O SEGUNDO PERTENCE AO PRIMEIRO (CHAVE)
aluno_idade = {"Pedro":22,"Ana":28,"Carlos":32}

#PARA SELECIONAR APENAS USAR PRINT E COLOCAR 'nome do dicionario'[CHAVE]
print(aluno_idade["Pedro"])

#PARA ADICIONAR VALOR BASTA COLOCAR 'nome do dicionario'[CHAVE] = valor
aluno_idade["Marcos"] = 21

#LIMPANDO O DICIONARIO POR COMPLETO
aluno_idade.clear()

#DELETANDO O DICIONARIO
del aluno_idade

#A FUNÇAO LEN TRAZ O NUMERO DE PARES (VALORES COM RESPECTIVAS CHAVES)
len(aluno_idade)

#TRAZENDO SOMENTE AS CHAVES
aluno_idade.keys()

#TRAZENDO SOMENTE OS VALORES 
aluno_idade.values()

#TRAZENDO OS PARES EM FORMA DE ITEM UNITARIO
aluno_idade.items()

#FUNÇAO PARA PEGAR OS ITENS(PARES) DE UM DICIONARIO E ADICIONANDO EM OUTRA
aluno_idade.update(lista2)

#PODE ATRIBUIR VALORES DE DICIONARIOS EM VARIAVEIS ATRAVES DAS CHAVES
val = aluno_idade["Pedro"]
print(val)

#UMA CHAVE EM UM DICIONARIO PODE RECEBER UMA LISTA COMO VALOR
dic_lista = {'chave1':[1,2,3,4,5],'chave2':[7,8,9,10]}

#BUSCANDO VALOR DENTRO DE UMA LISTA Q ESTA DENTRO DE UM DICIONARIO
print(dic_lista['chave1'][0])

#APLICANDO FUNÇAO EM UM VALOR DENTRO DA LISTA OU REALIZANDO OPERAÇAO, DENTRO DO DICIONARIO
dic_lista['chave1'][0].upper()
x = dic_lista['chave1'][0] - 2

#BONUS - OPERANDO SOBRE UM VALOR E JA ADICIONANDO O RESULTADO NO LUGAR DO VALOR OPERADO
dic_lista['chave1'][0] -= 2

#DA PRA COLOCAR DICIONARIO DENTRO DE DICIONARIO, APESAR DE NAO SER RECOMENDADO - ANINHADO 
dic1{"dic1.1":{"dic1.2":1000}}

#BUSCANDO VALOR DENTRO DOS DICIONARIOS, MESMO QUE A LISTA, CHAVES ATE IR NO VALOR DO SUBGRUPO SO QUE NESSE POR CHAVE AO INVES DE INDEX
print(dic1["dic1.1"]["dic1.2"])

#TUPLAS
#FEITA ENTRE PARENTESES
#NAO IMUTAVEIS, CRIADAS PARA ESTE FIM
tupla = ("Chocolate","Laranja")

#CONVERTENDO TUPLA PARA LISTA, CRIA-SE OUTRO ELEMENTO
list('nome da copia')

#LISTA PARA TUPLA, APOS MODIFICAÇAO SE USAR O MESMO NOME DE VAR ELE SOBREPOE
tuple('nome da copia')

#CAP05 - ESTRUTURAS DE PROGRAMAÇAO PYTHON

#CONDICIONAL IF/ELSE , CASO  NAO SATISFAÇA CAI PARA O ELSE E EXECUTA
#IDENTAÇAO É PARTE DA SINTAXE DO PYTHON
if 5 > 2:
    print("É verdade")
else:
    print("Náo é verdadeira")

#COM VARIAVEL AGORA
x = "Segunda"
if x == "Segunda":
    print("É segunda-feira")
else:
    print("Não é segunda-feira")

#UTILIZANDO ELIF PARA CRIAR MAIS SITUAÇOES
x = "Segunda"
if x == "Segunda":
    print("É segunda-feira")
elif x == "Terça":
    print("Hoje é terça-feira")
else:
    print("Não é segunda e nem terça")

#IF'S ANINHADOS
nome = "Bob"
idade = 14
if idade > 13:
    if nome == "Bob":
        print("Não esta autorizado")
    else:
        print("Esta autorizado")
else:
    print("Nao esta autorizado")

#SIMPLIFICANDO O CASO ACIMA COM OPERADOR LOGICO
nome = "Bob"
idade = 12
if (idade > 13) and (nome == "Bob"):
    print("Não esta autorizado")
elif idade > 13:
    print("Esta autorizado")
else:
    print("Não esta autorizado, menor de idade")
    
#SINAL DE DIFERENTE '!='

#LOOPS
#FOR IN X - COM UM GRUPO DE DADOS JA DEFINIDOS EM UMA LISTA/TUPLA
tp = (2,3,4) 
for i in tp: #PARA CADA NUMERO NESSA LISTA, FAÇA
    print(i)
    
#FOR IN RANGE - COM UM GRUPO DEFINIDO NA HORA - O ULTIMO VALOR É EXCLUSIVE 
for i in range(0,5,'CADENCIA'): #PARA CADA NUMERO NESSA LISTA FAÇA
    print(i)

#LOOP DENTRO DO LOOP
tp1 = (1,2,3,4,5)
tp2 = (1,2,3)

for i in tp1:
    for z in tp2:
        print(i*z)
    print('----')

#LOOP COM DUAS LISTAS - ELE FAZ UMA DE CADA VEZ SEPARADAMENTE
lista1 = [10,16,24,39]
lista2 = [32,89,47,76,12]
soma = 0

for lista in [lista1,lista2]:
    for num in lista:
        if num % 2 == 0:
            soma += num #mesma coisa que soma = soma + num

print ('A soma dos numeros pares das duas listas é igual a', soma)

#LISTA DE LISTA = MATRIZES

matriz = [[42,23,34], [100,215,114], [10.1,98.7,12.3]]
maior_numero = 0

for linha in matriz:
    for num in linha:
        if num > maior_numero:
            maior_numero = num

print("O mario numero dessa matriz é: ",maior_numero)
            
#LOOP COM DICIONARIO

dict = {'k1':'Marcos', 'k2':'Lucas', 'k3':'Mario'}
for item ind dict:
    print (item) #POR PADRAO RETORNA A CHAVE

#PARA RETORNAR OS DOIS

dict = {'k1':'Marcos', 'k2':'Lucas', 'k3':'Mario'}
for K,V in dict.items(): #ESSA FUNÇAO RETORNA OS 2, NECESSARIO 2 VAR PARA RECEBER
    print (K,V)
    
#LOOP AGORA COM WHILE
#TEM QUE GARANTIR QUE VAI SAIR DO LOOP SE NAO TRAVA TUDO
valor = 0
while valor < 10:
    print(valor)
    valor += 1

#TAMBEM POSSUI O ELSE, APOS SAIR DO LOOP EXECUTA O COMANDO DO ELSE
#INDEPENDENTE SE ENTRAR OU NAO NO LOOP, EXECUTA O ELSE APOS
valor = 20
while valor < 10:
    print(valor)
    valor += 1
else:
    print('Concluido') #OUTPUT 'Concluido'

#BREAK FORÇA A INTERRUPÇAO DO LOOP
valor = 0
while valor < 10:
    print(valor)
    valor += 1
    if valor == 5:
        break #OUTPUT '0 1 2 3 4'
        
#PASS APENAS FORÇA A CONTINUAÇAO, DESCONSIDERANDO O CODIGO INCOMPLETO

for i in range(10):
    pass

#CONTINUE APENAS IGNORA ALGUM ELEMENTO NO LOOP E CONTINUA NORMALMENTE (SOMENTE NO LOOP FOR)
for i in range(10):
    if i == 2:
        continue
    print(i)

#WHILE E FOR JUNTOS PARA SABER QUAIS N DE 2 A 30 SAO PRIMOS

primos = []

for i in range(2,31):
    primo = true
    t = 2
    while t <= i//2: #TESTA TODAS AS DIVISOES ENTRE 2 E METADO DE NUMERO (PRIMO)
        if i % t == 0 #CASO SEJA DIVISIVEL POR ALGUM NUMERO NESSE INTERVALO (NAO E PRIMO)
        primo = false #LOGO ATRIBUI FALSO, QUE E NECESSARIO PARA INSERIR NA LISTA
        break
    i += 1 
    if primo:
        primos.append(num)
print (primos)

#TENTANDO
for i in range (2,31): #METODO MENOS PERFOMATICO POIS IMPRIME MULTIPLAS MENSAGENS
    t = 2              #E TESTA TODOS OS VALORES SEM NECESSIDADE (MATEMATICA)
    t2 = 1
    
    while t < i:
        if i % t == 0:
            t2 = 0
            t += 1
        else:
            t += 1
    
    if t2 == 1:
        print(f'O número {i} é primo')

#FUNÇAO RANGE - range ('inicio','fim','passo') - VALOR FINAL EXCLUSIVE
for i in range (0,20,2):
    print(i) #OUTPUT 2, 4, 6, 8, 10, 12, 14, 16, 18

#UTILIZANDO RANGE COM LISTA DE VALORES
lista = ['Morango', 'Abacaxi', 'Mamao']
x = len(lista) #PEGA QUANTOS VALORES TEM NO CONJUNTO
for i in range(0,x): #ASSIM CONSEGUINDO O INDEX (CORRESPONDENCIA DE CADA VALOR)
    print(lista[i]) #PRINTANDO CADA VALOR BASEADO NO INDEX

#FUNÇOES EM PYTHON
#CRIANDO UMA FUNÇÃO
#SE CRIAR OUTRA FUNÇAO COM O MESMO NOME, SOBREPOE
def funcaoteste():
    print('Testando')

#COM PARAMETRO AGORA
def funcaoteste(nome):
    x = nome
    print(f'Alo {x}')

#COM NUMERO INDETERMIADO DE PARAMETROS
def funcaoteste(x, *y):
    print(x)
    for i in y:
        print(i)

funcaoteste(1,2,3,4,5,7,8)







