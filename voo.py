class Voo:
    def __init__(self, quantidade_passageiro, data_saida, data_chegada, local_saida, destino, empressa_aerea, numero_voo):
        self.quantidade_passageiro = quantidade_passageiro
        self.local_saida = local_saida
        self.destino = destino
        self.data_chegada = data_chegada
        self.data_saida = data_saida
        self.empressa_aerea = empressa_aerea
        self.numero_voo = numero_voo

    def viajando(self):
        print(f" Quantidade do passageiro: {self.quantidade_passageiro}")
        print(f" Data da viajem: {self.data_saida}")
        print(f" Data da chegada: {self.data_chegada}")
        print(f" Local da saida: {self.local_saida}")
        print(f" Destino: {self.destino}")
        print(f" Empressa Aérea: {self.empressa_aerea}")
        print(f" Numero do voo: {self.numero_voo}")
        print('-' * 172)
        print(f"Os {self.quantidade_passageiro} passageiros do voo de numero {self.numero_voo} irão viajar de {self.local_saida} para {self.destino} no dia {self.data_saida},"
              f"o voo chegara dia {self.data_chegada} no seu destino com a empressa da {self.empressa_aerea}")


class Voo_comercial(Voo):
    def voo1(self, quantidade_passageiro, data_saida, data_chegada):
        self.quantidade_passageiro = quantidade_passageiro
        self.data_saida = data_saida
        self.data_chegada = data_chegada

class Voo_Cargueiro(Voo):
    def voo2(self, tipo_carga, peso_carga, valor_carga, quantidade_carga):
        self.tipo_carga = tipo_carga
        self.peso_carga = peso_carga
        self.valor_carga = valor_carga
        self.quantidade_carga = quantidade_carga




v1 = Voo("620", "06/02/2026", "07/02/2026", "Araçatuba-SP", "Amisterdã", "Gol", "8" )
v1.viajando()
