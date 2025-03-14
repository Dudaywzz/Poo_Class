class Voo:
    def __init__(self, quantidade_passageiro, data_saida, data_chegada, local_saida, destino, empressa_aerea, numero_voo):
        self._quantidade_passageiro = quantidade_passageiro
        self._local_saida = local_saida
        self._destino = destino
        self._data_chegada = data_chegada
        self._data_saida = data_saida
        self._empressa_aerea = empressa_aerea
        self._numero_voo = numero_voo



    def viajando(self):
        print(f" Quantidade do passageiro: {self._quantidade_passageiro}")
        print(f" Data da viajem: {self._data_saida}")
        print(f" Data da chegada: {self._data_chegada}")
        print(f" Local da saida: {self._local_saida}")
        print(f" Destino: {self._destino}")
        print(f" Empressa Aérea: {self._empressa_aerea}")
        print(f" Numero do voo: {self._numero_voo}")
        print('-' * 172)
        print(f"Os {self._quantidade_passageiro} passageiros do voo de numero {self._numero_voo} irão viajar de {self._local_saida} para {self._destino} no dia {self._data_saida},"
              f"o voo chegara dia {self._data_chegada} no seu destino com a empressa da {self._empressa_aerea}")


    def get_quantidade_passageiro(self):
        return self._quantidade_passageiro

    def get_local_saida(self):
         return self._local_saida

    def get_destino(self):
        return self._destino

    def get_data_chegada(self):
        return self._data_chegada

    def get_data_saida(self):
        return self._data_saida

    def get_empressa_aerea(self):
        return self._empressa_aerea

    def get_numero_voo(self):
        return self._numero_voo


class Voo_comercial(Voo):
    def voo1(self, quantidade_passageiro, data_saida, data_chegada):
        self._quantidade_passageiro = quantidade_passageiro
        self._data_saida = data_saida
        self._data_chegada = data_chegada

class Voo_Cargueiro(Voo):
    def voo2(self, tipo_carga, peso_carga, valor_carga, quantidade_carga):
        self.__tipo_carga = tipo_carga
        self.__peso_carga = peso_carga
        self.__valor_carga = valor_carga
        self.__quantidade_carga = quantidade_carga




v1 = Voo("620", "06/02/2026", "07/02/2026", "Araçatuba-SP", "Amisterdã", "Gol", "8" )
v1.viajando()

voo1 = Voo_comercial()
voo1.viajando()

voo2 = Voo_Cargueiro()
voo2.viajando()
