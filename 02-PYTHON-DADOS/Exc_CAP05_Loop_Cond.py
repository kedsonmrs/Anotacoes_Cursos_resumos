# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

p = input("Qual o dia da semana: ")
if p == "Domingo" or p == "Sábado":
    print("Dia de descanso!")
else:
    print("Vá trabalhar")

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

#FORMA 1 CONDICIONANDO PARA PRINTAR APENAS NO ULTIMO INDEX
frutas = ["Maçã","Pera","Morango","Abacaxi"]
for i in frutas:
    if "Morango" not in frutas and i == frutas[-1]:
        print("Não há morango na lista!")
    elif "Morango" in frutas and i == frutas[-1]:
        print("Há morango na lista!")

#FORMA 2 (RANGE(LEN(FRUTAS)))
frutas = ["Maçã","Pera","Morango","Abacaxi"]
for i in range(len(frutas)):
    if frutas[i] == "Morango":
        print(f"Há morango na lista na posição {i} da lista ")

#FORMA 3 (ENUMERATE) 
frutas = ["Maçã","Pera","Morango","Abacaxi"]
for i, v in enumerate(frutas):
    if v == "Morango":
        print(f"Há morango na lista na posição de índice {i}")

# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista
lista_res = []
tupla_val = (2,4,6,8)

for i in tupla_val:
    res = i * 2
    lista_res.append(res)

print(f"Resultados {lista_res}!")

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for i in range(100,151,2):
    print(i)

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela
temp = 40
while temp >= 35:
    print(f"Temperatura atual de {temp}ºC")
    temp -= 1

# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
cont = 0
while cont <= 100:
    if cont != 23:
        print(cont)
    elif cont == 23:
        print(f"Número {cont} encontrado, encerrando...")
        break
    cont += 1

# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
lista = []
num = 4
while num <= 20:
    if num % 2 == 0:
        lista.append(num)
    num += 1
print(lista)

# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
lista = []
for i in range(5,45,2):
    lista.append(i)
print(lista)

# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.” 

frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão." 
count = 0
for i in frase:
    if i == "r":
        count +=1
print(f"A letra R aparece {count} vezes na frase!")
