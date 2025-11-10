import csv

class Gasto():
    
    def __init__(self,data,tipo,valor):
        self.data = data
        self.tipo = tipo
        self.valor = valor
    
class SistemaFinanceiro():

    def __init__(self):
        self.gastos = []
    
    def salvaGasto(self):
        
        data = str(input('Data (dd/mm/aaaa) :'))
        tipo = str(input('Tipo: '))
        valor = float(input('Valor: '))

        novo_gasto = Gasto(data,tipo,valor)
        self.gastos.append(novo_gasto.data)
        self.gastos.append(novo_gasto.tipo)
        self.gastos.append(novo_gasto.valor)

        with open("C:\\Users\\Kedson\\Desktop\\Anotacoes_Cursos_resumos\\PROJETO PESSOAL\\DOC.csv",'a',newline='') as arquivo:
            writer = csv.writer(arquivo,delimiter=';')
            writer.writerow(self.gasto)

    def deletaGasto(self):
        
        while True:
            opcao_deletar = int(input("1. Deletar tudo\n2. Deletar registro\nSelecione uma opção: "))
            
            if opcao_deletar == 1:
                with open("C:\\Users\\Kedson\\Desktop\\Anotacoes_Cursos_resumos\\PROJETO PESSOAL\\DOC.csv",'w',newline='') as arquivo:
                    pass
                print('Todos os registros deletados.')
                break
            
            elif opcao_deletar == 2:
                with open("C:\\Users\\Kedson\\Desktop\\Anotacoes_Cursos_resumos\\PROJETO PESSOAL\\DOC.csv",'r',newline='') as arquivo:
                    reader = csv.reader(arquivo)
                    for i in reader:
                        self.gastos.append(i)
                    print(self.gastos)
                break
            
            else:
                print('Opçao inválida, tente novamente.')
                continue

    def verGastos(self):
        
        with open("C:\\Users\\Kedson\\Desktop\\Anotacoes_Cursos_resumos\\PROJETO PESSOAL\\DOC.csv",'r',newline='') as arquivo:
            reader = csv.reader(arquivo)
            for i in reader:
                print(i)
                    
    def validaContinuaçao(self):
    
        while True:
            opcao_continua = input('Deseja continuar? (S/N)')
            if opcao_continua == 'S':
                return True
            elif opcao_continua == 'N':
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

    opcao = int(input('Selecione uma opção:'))
    if opcao == 1:
        sistema.salvaGasto()
        continua = sistema.validaContinuaçao()
    
    elif opcao == 2:
        sistema.deletaGasto()
        continua = sistema.validaContinuaçao()
    
    elif opcao == 3:
        sistema.verGastos()
        continua = sistema.validaContinuaçao()
    
    elif opcao == 4:
        print('Finalizando programa.')
        break
    
    else:
        print('Opção inválida, tente novamente.')
        continue