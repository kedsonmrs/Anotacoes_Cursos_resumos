import random as r
print('-- BEM VINDO AO JOGO DA FORCA --')
ini = input("Deseja iniciar o jogo? (S/N) ")

if ini == 'S':    
    p = r.choice(['abacaxi','maça','pera','uva','morango','melancia','jaca'])
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
                print("Derrota, fim de jogo!")
                break
            else:
                True
            continue
else:
    print("Encerrando programa. Obrigado!")




        
