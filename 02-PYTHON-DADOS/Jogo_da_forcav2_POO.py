class Jogos():

    empresa = 'KedGames'

    def __init__(self):
        pass
    
    def creditsJogo(self):
        print(f"Jogo de {Jogos.empresa}")
     
    def iniJogo(self):
        pass
    
    def specsJogo(self):
        pass

class jogoForca(Jogos):

    def specsJogo(self):
        print('Jogo_forca_V2')

    def iniJogo(self):
        import random as r
        print('-- BEM VINDO AO JOGO DA FORCA --')
        while True:
            ini = input("Deseja iniciar o jogo? (S/N) ")

            if ini == 'S' or ini == 'N':
                if ini == 'N':
                    print("Encerrando programa, obrigado!")
                    break
                elif ini == 'S':    
                    with open ('C:\\Users\\kedso\\Desktop\\forca\\palavras.txt','r') as arq:
                        palavras = arq.readlines()
                    pa = r.choice(palavras).strip()
                    lpalavra = [i for i in pa]
                    ljogo = ['_' for i in lpalavra]
                    ltentativas = []
                    tentativas = 0

                    print(' '.join(ljogo))

                    while True:
                        t = input("Escolha uma letra: ")
                        if t in lpalavra:
                            for i,p in enumerate(lpalavra):
                                if p == t:
                                    ljogo[i] = t
                            if lpalavra == ljogo:
                                v = ''.join(ljogo)
                                print(f"Parabéns, a palavra era {v}.")
                                break
                            print(' '.join(ljogo))
                            print(f'Tenativas: {ltentativas} \n')
                        elif t not in lpalavra:
                            print(' '.join(ljogo))
                            ltentativas.append(t)
                            tentativas += 1
                            print(f'Tentativas: {ltentativas} \n')
                            if tentativas < 6:
                                print(f'Voce ainda possui {6 - tentativas} tentativas! \n')
                            if tentativas == 6:
                                print("Derrota, fim de jogo!\n")
                                print(f"A palavra correta era {pa}.")
                                break
                            else:
                                True
                            continue
                    break
            elif ini != 'S' or ini != 'N':
                print('Opção inválida! Tente novamente.')

class jogoCorrida(Jogos):

    def specsJogo(self):
        print("jogo_corrida_v0")
    
    def iniJogo(self):
        print("Jogo em construção!")

jogos = [jogoCorrida(),jogoForca()]

for jogo in jogos:
    jogo.specsJogo()
    jogo.creditsJogo()