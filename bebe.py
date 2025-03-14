from pessoa import Pessoa

class Bebe(Pessoa): # Herda da classe Pessoa
    def __init__(self, nome, data_nascimento, registro,
                 estudando=False, trabalhando=False):
        super().__init__(nome, data_nascimento, registro, estudando, trabalhando)
        self.fome = True
        self._chorando = True
        self.dormindo = False

    def is_chorando(self):
        """
        Checa o status de chorando do objeto.

        :return: Boolean value
        :rtype: bool
        """
        return self._chorando

    def is_fome(self):
        return self.fome

    def is_dormindo(self):
        return self.dormindo

    def set_mamar(self):
        """
        Ação para p/ o bebe mamar
        :return: None
        """
        if self.fome:  # Só mama se estiver com fome
            self.fome = False
            self.chorando = False  # O bebê para de chorar após mamar
            print(f"{self.get_nome()} mamou e está satisfeito.")
        else:
            print(f"{self.get_nome()} não está com fome e não quer mamar.")

    def set_dormir(self):
        """

        """
        if not self.dormindo:
            if self.fome:  # Não pode dormir com fome
                print(f"{self.get_nome()} está com fome e não consegue dormir.")
            else:
                self.dormindo = True
                print(f"{self.get_nome()} foi dormir. Shhh, não faça barulho!")
        else:
            print(f"{self.get_nome()} já está dormindo.")

    def set_acordar(self):
        if self.dormindo:
            self.dormindo = False
            self.fome = True  # Ao acordar, o bebê fica com fome
            self.chorando = True # Quando esta com fome ele chora
            print(f"{self.get_nome()} acordou, está chorando e com fome!")
        else:
            print(f"{self.get_nome()} já está acordado.")

    def set_trabalhar(self):
        print(f"{self.get_nome()} ainda não pode trabalhar")

    def set_estudar(self):
        print(f"{self.get_nome()} ainda não pode estudar")

    def apresentar(self):  # Sobrescrevendo o metodo apresentar()
        super().apresentar()  # super-representa a classe PAI e chama o metodo apresentar() da classe Pessoa
        print(f"Fome: {'Sim' if self.fome else 'Não'}")
        print(f"Chorando: {'Sim' if self.chorando else 'Não'}")
        print(f"Dormindo: {'Sim' if self.dormindo else 'Não'}")
        print("-" * 20)
