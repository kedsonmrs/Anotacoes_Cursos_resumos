import csv as csv

def recebeDados():
    print('Preencha na seguinte ordem: data, tipo, valor')

    dadosf = []
    x = str(input('Data (dd/mm/aaaa) :'))
    y = str(input('Tipo: '))
    z = float(input('Valor: '))

    dadosf.append(x)
    dadosf.append(y)
    dadosf.append(z)
    return dadosf

def insere(dataf,tipof,valorf):
    writer = csv.writer(arquivo)
    with open('C:\\Users\\kedso\\Desktop\\PROJETO_PESSOAL\\DOC.csv','a') as arquivo:
        writer.writerow(dataf,tipof,valorf)

    print('Gasto adicionado.')

def deleta():
    print('Gasto removido.')

def mostra():
    print('Mostrando gasto.')

def validaContinuaçao():
    
    while True:
        op2 = input('Deseja continuar? (S/N)')
        valiC = 0
        if op2 == 'S':
            break
        elif op2 == 'N':
            print('Finalizando programa.')
            return valiC
            break
        else:
            continue

print('==== FINANCEIRO MARIO ====')

vali = 1
while vali == 1:

    print('==========================')
    print('========== MENU ==========')
    print('==========================')

    print('1 - Adicionar gasto')
    print('2 - Remover gasto')
    print('3 - Ver gastos')
    print('4 - Sair')

    op = int(input('Selecione uma opção:'))
    if op == 1:
        
        dados = recebeDados()
        insere(dados)
        print('Operação realizada com sucesso!')
        vali = validaContinuaçao()
    
    elif op == 2:
        deleta()
        print('Operação realizada com sucesso!')
        vali = validaContinuaçao()

    elif op == 3:
        mostra()
        print('Operação realizada com sucesso!')
        vali = validaContinuaçao()

    elif op == 4:
        print('Finalizando programa.')
        break
    
    else:
        print('Opção inválida, tente novamente.')
        continue

