

class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, salario=100,estudando=True, trabalhando=False):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__codigo = codigo
        self._estudando = estudando
        self._trabalhando = trabalhando
        self._salario = salario

    def set_salario(self, valor):
        if valor >= 0:
            self._salario = valor
        else:
            print("salario invalido")

    def set_estudar(self, status):
        self.__estudando = status
        if status:
            self.set_salario(self.get_salario() + 400)

    def get_nome(self):
        return self.__nome
    def get_data_nascimento(self):
        return self.__data_nascimento
    def get_codigo(self):
        return self.__codigo
    def get_salario(self):
        return self._salario

    def is_trabalhando(self):
        return self._trabalhando
    def is_estudando(self):
        return self._estudando

    def set_trabalhar(self, status):
        if self._trabalhando and status:
            print("ja esta trabalhando")
        elif not self._trabalhando and not status:
            print("que vida boa!")
        elif not self._trabalhando and status: 
            self._trabalhando = status
            self.set_salario(100)
        else:
            self._trabalhando = status
            self.set_salario(0)

    def apresentar(self):
        print(f'ola eu sou o  {self.__nome} \n'
              f' minha data de nascimento é {self.__data_nascimento} \n'
              f'meu codigo é {self.__codigo}')

        if self._trabalhando:
            print('trabalhando')
        else:
            print('não esta trabalhando')

        if self._estudando:
            print('estudado')
        else:
            print('não esta estudando')

    def estudar(self):
        if self._trabalhando and self._trabalhando:
            aumento = (self._salario + 5)
            print(f'Seu salario aumentou 5 reais {aumento} ')

        elif self._estudando:
            print(f'Estudando')
        else:
            print(f'N esta estudando')

    def trabalhar(self):
        if self._trabalhando:
            print('voce esta Trabalhando')
        else:
            print('voce nao esta trablhando')

class  Bebe(Pessoa):  # Herda da classe Pessoa
    def __init__(self, nome, data_nascimento, registro,
                 estudando=True, trabalhando=False):
        super().__init__(nome, data_nascimento, registro, estudando, trabalhando)
        self.fome = True
        self.chorando = True
        self.dormindo = False

    def mamar(self):
        if self.fome: #Só mama se estiver com fome
            self.fome=False
            self.chorando=False # O bebê para de chorar após mamar
            print(f'{self.__nome} mamou e está satisfeito.')
        else:
            print(f'{self.__nome} não está com fome e não quer mamar.')

    def chorar(self):
        if self.chorando:
            print(f"{self.__nome} esta chorando!")
        else:
            print(f"{self.__nome} não esta chorando!")

    def dormir(self):
        if not self.dormindo:
            if self.fome: #Não pode dormir com fome
                print(f"{self.__nome} está com fome e não consegue dormir.")
            else:
                self.dormindo = True
                print(f"{self.__nome} foi dormir. Shhh, não faça barulho!")
        else:
            print(f"{self.__nome} ja está dormindo.")

p1 = Pessoa("Lucas","23/09/1990","aghs", estudando=True, trabalhando=False)
p1.apresentar()
p1.trabalhar()
p1.estudar()
print("-" * 20)

p2 = Pessoa("Luciano","04/10/1991","agde", estudando=False, trabalhando=True)
p2.apresentar()
p2.trabalhar()
p2.estudar()
print("-" * 20)

p3 = Pessoa("Calleri","19/08/1992","agew", estudando=True, trabalhando=False)
p3.apresentar()
p3.trabalhar()
p3.estudar()
print("-" * 20)

p4 = Pessoa("Oscar","10/03/1993","agwr", estudando=False, trabalhando=True)
p4.apresentar()
p4.trabalhar()
p4.estudar()
print("-" * 20)

p5 = Pessoa("Ferreirinha","06/02/1994","agek", salario=100, estudando=True, trabalhando=False)
p5.apresentar()
p5.trabalhar()
p5.estudar()
print("-" * 20)



















