import csv
import os


class Gasto():

    def __init__(self, data, tipo, valor):
        self.data = data
        self.tipo = tipo
        self.valor = valor

    def listaGasto(self):
        gasto_lista = [self.data, self.tipo, self.valor]
        
        return gasto_lista


class SistemaFinanceiro():

    def __init__(self):
        self.caminho_arquivo = os.path.join(
            'C:\\', 'Users', 'kedso', 'Desktop', 'CURSOS',
            'Anotacoes_Cursos_resumos', 'PROJETO PESSOAL', 'DOC.csv'
        )

    def salvaGastoCSV(self):
        data = str(input('Data (dd/mm/aaaa) :'))
        tipo = str(input('Tipo: '))
        valor = float(input('Valor: '))

        gasto = Gasto(data, tipo, valor)

        with open(self.caminho_arquivo, 'a', newline='') as arquivo:
            writer = csv.writer(arquivo, delimiter=';')
            writer.writerow(gasto.listaGasto())

    def deletaGastoCSV(self):

        while True:
            opcao_deletar = int(input("1. Deletar tudo\n2. Deletar registro\nSelecione uma opção: "))

            if opcao_deletar == 1:
                with open(self.caminho_arquivo, 'w', newline='') as arquivo:
                    pass
                print('Todos os registros deletados.')
                break

            elif opcao_deletar == 2:
                with open(self.caminho_arquivo, 'r', newline='') as arquivo:
                    reader = csv.reader(arquivo)
                    gastos_arquivo_lista = []
                    for i in reader:
                        gastos_arquivo_lista.append(i)

                    contador_indices = 0
                    print('Registros atuais:')

                    for z in gastos_arquivo_lista:
                        print(f'{contador_indices} - {z}\n')
                        contador_indices += 1

                    while True:
                        opcao_indice = int(input('Selecione o índice do registro desejado: '))

                        if 0 <= opcao_indice < len(gastos_arquivo_lista):
                            del gastos_arquivo_lista[opcao_indice]

                            with open(self.caminho_arquivo, 'w', newline='') as arquivo:
                                writer = csv.writer(arquivo, delimiter=';')
                                writer.writerows(gastos_arquivo_lista)

                            del gastos_arquivo_lista
                            print('Registro deletado com sucesso.')
                            break
                        else:
                            print("Indice inválido, tente novamente.")
                            continue

                break

            else:
                print('Opçao inválida, tente novamente.')
                continue

    def validaContinuaçaoMenu(self):
        while True:
            opcao_continua = input('Deseja continuar? (S/N)')
            if opcao_continua == 'S':
                return True
            elif opcao_continua == 'N':
                print('Finalizando programa.')
                return False

    def apresentaGastosCSV(self):
        with open(self.caminho_arquivo, 'r', newline='') as arquivo:
            registros = csv.reader(arquivo, delimiter=';')
            for registro in registros:
                print(f"Data: {registro[0]} / Tipo: {registro[1]} / Valor: {float(registro[2])}")


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
        sistema.salvaGastoCSV()
        continua = sistema.validaContinuaçaoMenu()

    elif opcao == 2:
        sistema.deletaGastoCSV()
        continua = sistema.validaContinuaçaoMenu()

    elif opcao == 3:
        sistema.apresentaGastosCSV()
        continua = sistema.validaContinuaçaoMenu()

    elif opcao == 4:
        print('Finalizando programa.')
        break

    else:
        print('Opção inválida, tente novamente.')
        continue