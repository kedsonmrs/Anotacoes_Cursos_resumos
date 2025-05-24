import random as r
print('-- BEM VINDO AO JOGO DA FORCA --')
ini = input("Deseja iniciar o jogo? (S/N) ")

if ini == 'S':    
    p = r.choice(['abacaxi','maça','pera','uva','morango','melancia','jaca'])
    lpalavra = [i for i in p]
    ljogo = ['_' for i in lpalavra]
    ltentativas = []
    tentativas = 0

    print(ljogo)

    while True:
        t = input("Escolha uma letra: ")
        if t in lpalavra:
            for i,p in enumerate(lpalavra):
                if p == t:
                    ljogo[i] = t
            print("Letra correta!")
            if lpalavra == ljogo:
                print(f"Fim, de jogo! Vitória!")
                break
            print(ljogo)
        elif t not in lpalavra:
            print("Letra fora da palavra!")
            ltentativas.append(t)
            print(ljogo)
            tentativas += 1
            print(f'Letras ja tentadas: {ltentativas}')
            if tentativas < 6:
                print(f'Voce ainda possui {6 - tentativas} tentativas!')
            if tentativas == 6:
                print("Derrota, fim de jogo!")
                break
            else:
                True
            continue
else:
    print("Encerrando programa. Obrigado!")




        
