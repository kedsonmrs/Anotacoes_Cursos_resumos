# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, 
# passando 2 parâmetros e depois faça uma chamada aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)

roc1 = Rocket()

roc1.move_rocket(1,1)
roc1.print_rocket()


# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa():

    especie = 'Humano'

    def __init__(self,nome,cidade,telefone,email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
    
    def apresenta_pessoa(self):
        print(f"Ola me chamo {self.nome} sou de {self.cidade} meu contato é {self.telefone} e meu email é {self.email}. ")

    def muda_nome(self,nomenovo):
        setattr(self,'nome',nomenovo)
    
    def muda_email(self,emailnovo):
        setattr(self,'email',emailnovo)

    def mostraespecie(Pessoa):
        print(f'Sou {Pessoa.especie}!')

p1 = Pessoa('Carlos','Brasilia','61982703350','calrao@gmail.com')
p1.mostraespecie()

# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Aparelho():

    def __init__(self,tamanho,interface):
        self.tamanho = tamanho
        self.interface = interface
    
    def apresenta_aparelho(self):
        self.apre = (f'Sou um aparelho {self.tamanho} com interface {self.interface}.')
        return self.apre

class MP3(Aparelho):

    def __init__(self, tamanho, interface, capacidade):
        super().__init__(tamanho, interface)
        self.capacidade = capacidade
    
    def mp3teste(self):
        print((self.apresenta_aparelho() + f' E sou um MP3 com capacidade de {self.capacidade}!'))

mp3 = MP3('grande' , 'padrão' , '128gb')
mp3.mp3teste()