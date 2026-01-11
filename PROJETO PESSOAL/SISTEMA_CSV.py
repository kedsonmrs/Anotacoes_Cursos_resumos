import csv
import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

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
        self.caminhoArquivo = ''

    def iniciaSistema(self):

        print('==== FINANCEIRO MARIO ====') 
        print('Selecione o arquivo CSV:')
        arq = Arquivo()
        self.caminhoArquivo = arq.selecionaArquivo()


        continua = True
        while continua:
            
            print('==========================')
            print('========== MENU ==========')
            print('==========================')

            print('1 - Adicionar gasto')
            print('2 - Remover gasto')
            print('3 - Ver gastos')
            print('4 - Modificar arquivo')
            print('5 - Mostrar arquivo')
            print('6 - Sair')
            try:
                opcao = int(input('Selecione uma opção:'))
                match opcao:
                
                    case 1:
                        self.salvaGastoCSV()
                        continua = self.validaContinuaçaoMenu()

                    case 2:
                        self.deletaGastoCSV()
                        continua = self.validaContinuaçaoMenu()

                    case 3:
                        self.apresentaGastosCSV()
                        continua = self.validaContinuaçaoMenu()
                    
                    case 4:
                        self.caminhoArquivo = arq.selecionaArquivo()
                        continua = self.validaContinuaçaoMenu()

                    case 5:
                        arq.mostraArquivo(self.caminhoArquivo)
                        continua = self.validaContinuaçaoMenu()

                    case 6:
                        print('Finalizando programa.')
                        break
                    
                    case _:
                        print('Opção inválida, tente novamente.')
                        continue
            except ValueError:
                print("Opção inválida, digite um número.")
                continue
    def salvaGastoCSV(self):
        
        with open(self.caminhoArquivo, 'r', newline='') as arquivo:
            reader = csv.reader(arquivo,delimiter=';')
            registros = list(reader)
            
            if not registros:
                with open(self.caminhoArquivo, 'a', newline='') as arquivo:
                    writer = csv.writer(arquivo, delimiter=';')
                    writer.writerow(['Data','Tipo','Valor'])
        
        data = str(input('Data (dd/mm/aaaa) :'))
        tipo = str(input('Tipo: '))
        valor = float(input('Valor: '))

        gasto = Gasto(data, tipo, valor)

        with open(self.caminhoArquivo, 'a', newline='') as arquivo:
            writer = csv.writer(arquivo, delimiter=';')
            writer.writerow(gasto.listaGasto())

    def deletaGastoCSV(self):

        while True:
            opcao_deletar = int(input("1. Deletar tudo\n2. Deletar registro\nSelecione uma opção: "))
            match opcao_deletar:

                case 1:
                    with open(self.caminhoArquivo, 'w', newline='') as arquivo:
                        pass
                    print('Todos os registros deletados.')
                    break

                case 2:
                    with open(self.caminhoArquivo, 'r', newline='') as arquivo:
                        reader = csv.reader(arquivo,delimiter=';')
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

                                with open(self.caminhoArquivo, 'w', newline='') as arquivo:
                                    writer = csv.writer(arquivo, delimiter=';')
                                    writer.writerows(gastos_arquivo_lista)

                                del gastos_arquivo_lista
                                print('Registro deletado com sucesso.')
                                break
                            else:
                                print("Indice inválido, tente novamente.")
                                continue

                case _:    
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
        
        tabelapd = pd.read_csv(self.caminhoArquivo,sep=';',encoding='latin-1')
        print (tabelapd)

class Arquivo():
    
    def __init__(self):
        pass
    
    def selecionaArquivo(self):        
        root = tk.Tk()
        root.withdraw()
        return filedialog.askopenfilename(title="Selecione o arquivo:",filetypes=[("Arquivo CSV","*.csv")])
    
    def mostraArquivo(self,caminho):
        print(caminho)

sistema = SistemaFinanceiro()

sistema.iniciaSistema()


