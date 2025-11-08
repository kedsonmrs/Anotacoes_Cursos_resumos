import csv

class Gasto():
    
    def __init__(self,data,tipo,valor):
        self.data = data
        self.tipo = tipo
        self.valor = valor
    
class SistemaFinanceiro():

    def __init__(self):
        self.gasto = []
    
    def salvaGasto(self):
        
        data = str(input('Data (dd/mm/aaaa) :'))
        tipo = str(input('Tipo: '))
        valor = float(input('Valor: '))

        novo_gasto = Gasto(data,tipo,valor)
        self.gasto.append(novo_gasto.data)
        self.gasto.append(novo_gasto.tipo)
        self.gasto.append(novo_gasto.valor)

        with open("C:\\Users\\Kedson\\Desktop\\Anotacoes_Cursos_resumos\\PROJETO PESSOAL\\DOC.csv",'a',newline='') as arquivo:
            writer = csv.writer(arquivo,delimiter=';')
            writer.writerow(self.gasto)

    def deletaGasto():
        pass

    def verGastos():
        pass
        
    def validaContinuaçao(self):
    
        while True:
            op2 = input('Deseja continuar? (S/N)')
            if op2 == 'S':
                return True
            elif op2 == 'N':
                print('Finalizando programa.')
                return False

sistema = SistemaFinanceiro()

print('==== FINANCEIRO MARIO ====')

continua = True
while continua:

    print('==========================')
    print('========== MENU ==========')
    print('==========================')

    print('1 - Adicionar gasto')
    print('2 - Remover gasto')
    print('3 - Ver gastos')
    print('4 - Sair')

    op = int(input('Selecione uma opção:'))
    if op == 1:
        sistema.salvaGasto()
        continua = sistema.validaContinuaçao()
    elif op == 2:
        pass
    elif op == 3:
        pass
    elif op == 4:
        print('Finalizando programa.')
        break
    
    else:
        print('Opção inválida, tente novamente.')
        continue