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
            p = r.choice(palavras).strip()
            lpalavra = [i for i in p]
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
                        print(f"A palavra correta era {p}.")
                        break
                    else:
                        True
                    continue
            break
    elif ini != 'S' or ini != 'N':
        print('Opção inválida! Tente novamente.')