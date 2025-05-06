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
print(VAR)

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
#TRANSFORMANDO EM UMA LISTA DE STRINGS
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
for item in dict:
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

#VARIAVEL GLOBAL/LOCAL
#POR PADRAO FOCA NA VARIAVEL DO ESCOPO (FUNÇAO OU FORA DA FUNÇAO)
#TEM COMO USAR O MESMO NOME EM AMBAS AS VARIAVEIS
var_global = 10 #VARIAVEL ESCOPO GLOBAL, FORA DA FUNÇAO, NO BLOCO PRINCIPAL

def multiplica_numeros(num1,num2):
    var_global = num1 * num2 #VARIAVEL LOCAL, DENTRO DA FUNÇAO, SUBBLOCO
    print(var_global)

#FUNÇOES BUILT-IN - JA INCLUSAS NA PROPRIA LINGUAGEM PYTHON

#VALOR ABSOLUTO (MODULO)
abs(-10)

#ZEROU OU UM TRASFORMADO EM BOOLEANO T/F
bool(0) / bool(1)

#SOMENTE O VALOR INTEIRO
int(10.2)

#CONVERTE EM STRING
str(10)

#TRANSFORMANDO EM FLOAT
float(5)

#INPUT - PEDE DADO AO USUARIO COM UMA MENSAGEM E ARMAZENA EM VARIAVEL
#POR PADRAO TRAZ VALOR COMO STRING
x = input('Digite seu nome: ')

#CONVERTENDO
x = int(input('Digite sua idade: '))

#PYPI.ORG - SITE COM PACOTES (CONJ DE FUNÇOES) PYTHON
#RETURN EM UMA FUNÇAO DEVOLVE O VALOR PARA USO EM VARIAVEIS

#FUNCAO LAMBDA
#RETORNA AUTOMATICO SEM RETURN
#FUNÇAO SIMPLIFICADA / FUNÇOES MAIS RAPIDAS
NOME_FUNC = lambda 'parametros': 'operaçao'
NOME_FUNC()

#LIST COMPREHETION
#LOOP COM CONDICIONAL DENTRO DE UMA LISTA (FOR E IF)
lista = [x for x in range(11) if x >=4 ] #PRIMEIRO X É O QUE ARMAZENA
print(lista)                   #SEGUNDO X É O PONTEIRO, ITERADOR

#MANIPULANDO VALOR ARMAZENADO
lista = [('me5' if x < 5 else 'ma=5') for x in range(11)] 
print(lista) #O FILTRO APOS TUDO FILTRA O QUE VAI SER ARMAZENADO        
             #O ANTERIOR MODIFICA O DADO BASEADO NA CONDIÇAO DO DADO ARMAZENADO

#AGORA COM DICIONARIO
#UTILIZA A FUNÇAO .items() PARA TRAZER CHAVE E VALOR DO DICT
dic_aluno_st = {k:v for k, v in dic_aluno_nota.items()}
print(dic_aluno_st)

#PARA RETORNAR DADO BASEADO NOS VALORES DO DICIONARIO
dic_aluno = {k:("Aprovado" if v >= 6 else "Reprovado") for k, v in dic_aluno_nota.items()}
print (dic_aluno_st)

#MANIPULAÇAO DE ARQUIVOS

#ABRINDO ARQUIVO .TXT PARA LEITURA
#PRIMEIRO SOMENTE ABRE ELE, NAO FAZ NADA
var = open('caminho do arquivo','r' leitura) #leitura nao manipula o arquivo

#AGORA LENDO O ARQUIVO
#AO LER O ARQUIVO ELE PARA O CURSOR NO FINAL DO TEXTO, AO IMPRIMIR NOVAMENTE VEM VAZIO
#SEM PARAMETRO LE TUDO, PARAMETRO INT PARA LER ATE X CARACTER, EXCLUSIVE
print(var.read())

#VOLTANDO O CURSOR PARA O INICIO
#DIFERENTE DO INDEX, INICIA NO 1 MESMO
var.seek(0,0) #coordenada do caracter para andar

#CONTANDO O NUMERO DE CARACTERES
print(var.tell())

#ABRINDO COM 'W' WRITE
#ELE CRIA O ARQUIVO, SE JA TIVER ELE SOPREPÕE O ARQUIVO JA CRIADO !!!!!!!!
#NAO DA PARA LER NESSA FUNÇAO
#TERIA QUE FECHAR O ARQUIVO E REABRIR NO MODO 'R' READ
var = open('caminho do arquivo','w' escrita)
var.close()
var = open('caminho do arquivo','r')

#PARA MANIPULAR UM JA EXISTENTE SE USA O PARAMETRO DE PERMISSAO 'a'
var = open('caminho do arquivo','a')

#FUNÇAO PARA GRAVAR ALGO
#FUNCIONA O 'W' e no 'A' (ADICIONA NO FIM)
var.write("str")

#ABRINDO ARQUIVO .CSV e TRANSFORMANDO PARA MANIPULAÇAO EM PYTHON
#PARA READ É A MESMA FORMA PARA ABRIR

#DIVIDINDO AS LINHAS - SOMENTE SEPARA CADA LINHA EM ITENS DE UMA LISTA
arq = open('caminho','r') #parametro NEWLINE, quebra a linha com o caracter definido (apenas LE OQ JA EXISTE)
tab = arq.read()
linhas = linha.split('\n') #aqui separa em uma lista cada ENTER, transformando em valores
                           #NAO FUNCIONA EM LISTAS

#AGORA EM COLUNAS PARA VIABILIZAR LOCALIZAÇAO VIA INDEX DE CADA VALOR NA TABELA
full_tab = []
for linha in linhas:
    split_linha = linhas.split(,)
    full_tab.append(split_linha)
print(full_tab)

#COM ISSO CADA LINHA SEPARADA POR LISTAS , E CADA VALOR (COLUNAS) POR ITENS DENTRO DESSAS LISTAS
#EXEMPLO
full_tab[1][2] #linha 1 e coluna 2

#PARA CONTAR QUANTAS LINHAS HA NA TABELA
count = 0
for row in full_tab:
    count += 1
print(count)

#PARA CONTAR COLUNAS - APENAS USAR FOR PARA A PRIMEIRA LINHA (COLUNA SEPARADA POR VIRGULA)
row1 = full_tab[0]
count = 0
for columns in row1
    count += 1
print(count)

#FUNÇAO QUE JA TRAS LINHA A LINHA COMO LISTA, SEPARADO POR \N
arq.readlines()

#CODIGO ESCRITO POR MIM PRATICA
#MANIPULANDO O CSV PARA LINHAS E COLUNAS, CONTANDO O NUMERO DE COLUNAS e LINHAS
arq = open('C:\\Users\\kedso\\Desktop\\CURSOS\\Business_Owners_20250427.csv','r')
tab = arq.read()            #em paralelo pode usar arq.readlines() pois ja le quebrando as linhas direntamente
tab_rows = tab.split('\n')  
tab_full =[]
countR = 0
for row in tab_rows:
    r = row.split(',')
    tab_full.append(r)
    countR += 1
countC = 0
column = tab_full[0]
for coluna in column:
    countC += 1
print(f"O arquivo contem {countC} colunas e {countR} linhas!")

#PANDAS - PACOTE PARA TABELAS MUITO MELHOR, TRATA CSV
import pandas as pd

#PARA ABRIR ARQUIVO
#E IMPRIMIR A TABELA JA FEITA, O PANDAS JA FORMATA TUDO AUTOMATICO UM CSV
arquivo = ("C:\\Users\\kedso\\Desktop\\CURSOS\\Business_Owners_20250427.csv")
print(arquivo)
tabela = pd.read_csv(arquivo)
print(tabela.head)

#PARA FILTRAR POR UMA COLUNA E CONTAR QUANTOS REGISTROS TEM DE CADA VALOR
print(tabela["Title"].value_counts())

#ARQUIVO TXT COM PACOTE 'OS'
#JOIN PERMITE ARMAZENAR O CAMINHO SEPARADO POR VIRGULAS, EM UMA VARIVEL, PORTATIL
import os as os
os.path.join('caminho separado por vigula')

#USANDO O WITH
#ELE DIFERENTE DO OPEN PURO, NAO PRECISA USAR O CLOSE APOS USO, FAZ AUTOMATICO
with open('C:\\Users\\kedso\\Desktop\\CURSOS\\teste.csv','w') as arquivo
    conteudo = arquivo.read()

#PACOTE CSV NO PYTHON
#USADO PARA GRAVAR LINHAS NO ARQUIVO NO FORMATO CSV ATRAVES DA FUNÇAO WRITER e WRITEROW
#NEWLINE = '' RECOMENDADO PARA NAO OCORRER REDUNDANCIA POIS O PYTHON JA QUEBRA E A BIBLIOTECA CSV TAMBEM
import csv as csv
writer = csv.writer(arquivo)
writer.writerow(('nota1','nota2','nota3')) #cabeçalho
writer.writerow((6,8,9))
writer.writerow((7,9,10))

#AGORA PRA LER OS CSV E ARMAZENAR
#csv.reader(arq) ARMAZENADA EM UMA VARIAVEL ASSOCIADA A UM LOOP LE LINHA POR LINHA DO ARQUIVO
with open('C:\\Users\\kedso\\Desktop\\CURSOS\\teste.csv','r') as arq:
    reader = csv.reader(arq) #RETORNA AS LINHAS EM UM ITERAVEL (LISTAS)
    for x in reader:
        print(x)
    dados = list(reader)#TRANSFORMANDO O CONJUNTO DE LISTAS LIDAS EM UMA LISTA DE LISTAS
    for i in dados[1:]: #AGORA IMPRIMINDO LINHA POR LINHA (LISTA)
        print(i)
 
#TRANSFORMANDO UM DICIONARIO PYTHON EM JSON (JSON NATURALMENTE É UM DICIONARIO)
#E EXPORTANDO ELE PARA UM ARQUIVO EM DISCO
import json as js
dict_guido = {'nome':'Guido van Rossun',
              'linguagem':'Python',
              'similar':['c','Modula-3','lisp']
              'users':1000000}

json1 = js.dumps(dict_guido) #ESSA FUNÇAO TRANSFORMA UM DICT PYTHON EM JSON
with open('Arquivo.json','w') as arq:
    arq.write(json1)

#AGORA LENDO UM ARQUIVO JSON
with open('Arquivo.json','r') as arq:
    texto = arq.read()
    dados = json.loads(texto) #apos isso se consulta como dicionario normal
    print(dados['nome'])

#PEGANDO ARQUIVO JSON DA WEB
#UTILIZA BIBLIOTECA EXTERNA
from urlib.request import urlopen #aqui esta sendo importado apenas uma funçao do pacote
var = urlopen('endereço do arquivo').read().decode('utf8')
#apos manipula igual ao normal
dados = var.loads(var)[0]
print('titulo: ',dados['title'])
print('URL: ',dados['url'])

#SIMPLIFICANDO
#GRAVANDO CONTEUDO DE UM ARQUIVO EM OUTRO
open('arq','w').write(open('arq2','r').read())

#todos os metodos e atributos do pacote
dir(numpy)

#o que a funçao faz
help(sqrt) #por exemplo do numpy

#PACOTE PARA TRATAR ALETORIEDADE
import random

random.choice([1,2,3,4,5]) #retorna um valor aleatorio
random.sample(range(100),10) #retorna 10 valores do range 

#ESTATISTICA
import statistics
dados[1,2,3,4,5,6,7,8,9,10]

statistics.mean(dados) #retorna media
statistics.median(dados) #mediana

#MAIS FUNÇOES BUILT IN

#FUNÇAO MAP() - RETORNA ITERADOR
#APLICA EM QUALQUER ITERAVEL EXECUTANDO DETERMINADA FUNÇAO EM CADA VALOR
#PODE USAR EM CONJUNTO COM LIST() PARA CRIRAR OUTRA LISTA

lista = list(map('funçao','iteravel'))
print(lista)

#UTILIZANDO EM CONJUNTO COM LAMBDA - PUXA OS VALORES DA LISTA PARA A OPERAÇAO
lista1 = (lambda x:x+1,'lista')
print(lista1)

#MAP TRATA MAIS DE UMA LISTA SE NECESSARIO
lista1 = (lambda x,y:x+y,'lista','lista2')
print(lista1)
 
#FUNÇAO REDUCE() - REDUZ UMA LISTA A UM UNICO VALOR, SOMA, MAIOR, MENOR - FUNÇAO COM 2 PARAMETROS
#RETORNA SEMPRE O X - ACUMULADOR
res = reduce(lambda x, y:a + y,numeros,'inicial se necessario')
print(res) #nesse caso retorna a soma de todos os numeros da lista

#AGORA PARA VER MAIOR VALOR
maior = reduce(lambda x, y:x if (x > y) else y,numeros)
print(maior) #aqui retorna o maior valor por comparaçao

#FUNÇAO FILTER() - RETORNA ITERAVEL APOS FILTRO - aplica a cada item do iteravel
#COM O ITERAVEL SE FAZ O LOOP OU CRIA UMA LISTA
filter('funçao retornando booleano, filtro','iteravel')
filter(lambda x:x % 2 == 0,numeros) #retornara apenas os que satisfazerem ao filtro (par)

#ZIP(), RETORNA A JUNÇAO DE 2 LISTAS - ITEM POR ITEM TRAZ PARES ENTRE ELAS EM FORMA DE TUPLAS
#RETORNA ITERADOR, UMA LISTA DE TUPLAS
x = [1,2,3,4]
y = [5,6,7,8]
print(list(zip(x,y)))

#EM DICIONARIO ELE RETORNA A CHAVE, PARA VOLTAR VALOR DEVE ESPECIFICAR O .values()
zip(x,y.values())

#ENUMERATE - TRAZ INDICE DOS VALORES E OS VALORES EM PARES NAS TUPLAS DE FORMA DE ITERAVEL (PARECIDO COM ZIP)
enumerate(lista)

#TRATAMENTO DE ERRO

try:  #TENTE FAZER - PARECE BASTANTE O IF, MAS PODE USAR COM ERRO ESPECIFICO
    'linhas de programa normal'
except IOError: #SE DER ERRO EMITA ESSA MENSAGEM
    print('mensagem')
else: #SE DER CERTO EMITA ESSA
    print('executado com sucesso')
finally: #ESSA SERA EMITIDA DE QUALQUER FORMA
    print('sempre printa')
    
#EXPRESSOES REGULARES - PADROES USADOS PARA COMBINAR OU ENCONTRAR OCORRENCIAS DE SEQUENCIAS DE CARACTERES EM UMA STRING
#TABELA COM OS CORRESPONDENTES
🔤 Caracteres e Classes de Caracteres
Símbolo	    Significado	                                    Exemplo
.	        Qualquer caractere (exceto \n)	                a.b → casa: acb, arb
\w	        Letra, número ou _ (equivale a [A-Za-z0-9_])	\w+ → joao123, a_b
\W	        Tudo que não é \w	                            Espaço, @, #, etc.
\d	        Qualquer dígito (0–9)	                        \d+ → 12345
\D	        Tudo que não é dígito	                        abc, @, etc.
\s	        Espaço em branco (espaço, tab, quebra de linha)	
\S	        Qualquer coisa que não seja espaço

Quantificadores
Símbolo	    Significado	            Exemplo
+	        1 ou mais vezes	        a+ → a, aa, aaa
*	        0 ou mais vezes	        a* → ``, a, aaaa
?	        0 ou 1 vez	            a? → ``, a
{n}	        Exatamente n vezes	    \d{2} → 22, 08
{n,}	    Pelo menos n vezes	    \d{3,} → 123, 5678
{n,m}	    Entre n e m vezes	    \d{2,4} → 12, 345, 6789

🔘 Âncoras e Fronteiras
Símbolo	        Significado	                    Exemplo
^	            Início da string	            ^Olá → só se começar com Olá
$	            Fim da string	                fim$ → só se terminar com fim
\b	            Fronteira de palavra	        \babc\b → só abc isolado
\B	            Não é fronteira de palavra	    \Babc → parte de outra palavra

import re

#ACHANDO NUMERO DE VEZES QUE APARECE UM CARACTER NUMA STRING - RETORNA INT COM LEN() 
txt = "Meu email é kkkkkkkk@gmail.com e voce pode me contatar em outro_kkkk@gmail.com"
rst = len(re.findall('@',txt))
print (rst)

#PALAVRAS QUE VEM APOS UMA ESPECIFICAR - lista com as string
rst1 = re.findall(r'voce (\w+)', txt) #CONSIDERA ESPAÇO 
print(rst1[0])

#BASICAMENTE SE MONTA A PALAVRA DA BUSCA
#POR EXEMPLO QUERO EMAIL
re.findall(r'\w+@\w+\.[a-zA-Z]+',txt)
#MAIS EXEMPLOS
len(re.findall(r'a',txt) #quantos A tem no texto
len(re.findall(r'\btempo\b',txt) #quantos TEMPO tem na palavra
re.findall(r'\w+!',txt) #palavras seguidas por '!'
re.findall(r'esse\s(\w+)\samargo',txt) #palavra entre 'esse' e 'amargo 
                                       #uso de intervalo dever dar match EXATO
                                       #O PARENTESES SERVE PRA DEFINIR O QUE VOCER QUER PEGAR, FORA FICA O "INTERVALO"
re.findall(r'\w+[á-úÁ-Ú]\b',txt)#\b MINUSCULO POIS ACENTUADO = \W e letra normal \w
