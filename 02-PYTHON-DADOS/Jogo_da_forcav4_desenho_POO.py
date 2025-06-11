import random

class jogoForca:

    def __init__(self):
        
        self.palavra = self.escolheP()
        self.palavraV = ['_' for i in self.palavra]
        self.cont = 0
        self.estagio = ['''  +========+
  |        |
           |
           |
           |
           |
           |\n''',
           '''  +========+
  |        |
  O        |
           |
           |
           |
           |\n''',
           '''  +========+
  |        |
  O        |
  |        |
           |
           |
           |\n''',
           '''  +========+
  |        |
  O        |
  |/       |
           |
           |
           |\n''',
           '''  +========+
  |        |
  O        |
 \\|/       |
           |
           |
           |\n''',
           '''  +========+
  |        |
  O        |
 \\|/       |
 /         |
           |
           |\n''',
           '''  +========+
  |        |
  O        |
 \\|/       |
 / \\       |
           |
           |\n''']

    def iniJogo(self):
        print("-- JOGO DA FORCA --")
        print("-------------------")
        while True:
            x = int(input("1 - Iniciar jogo\n2 - Fechar jogo\n"))
            if x == 1:
                return True
                break
            elif x == 2:
                return False
                break
            else:
                print ("Opção inválida, tente novamente.")
                continue
    
    def escolheP(self):
        with open ('C:\\Users\\kedso\\Desktop\\forca\\palavras.txt') as arq:
            palavras = arq.read().split()
            escolha = random.choice(palavras)
            p = [x.upper() for x in escolha]
            return p
        
    def atualizaP(self):
        
        print (self.estagio[self.cont])
        letra = input("Escolha uma letra:").upper()
        if letra in self.palavra:
            for i, l in enumerate(self.palavra):
                if l == letra:
                    self.palavraV[i] = l
        elif letra not in self.palavra:
            self.cont += 1
        print ("\n",''.join(self.palavraV),"\n")
        
    def encJogo(self):
        if self.palavraV == self.palavra:
            print ("Fim de jogo. Vitória!")
            return False
        
        elif self.cont == 6:
            print (self.estagio[self.cont])
            print ("Derrota. Chances esgotadas!")
            return False
        return True
        
    def main (self):
        jogo = jogoForca()
        if jogo.iniJogo():
            while jogo.encJogo():
                jogo.atualizaP()


game = jogoForca()
game.main()



        


