from Modelos.avaliacao import Avaliacao

class Restaurante:
    """Representa um restaurante e suas características."""
    restaurantes = []

    def __init__(self, nome, categoria): ##Construtor / Self == This
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False                   ##_ativo similar ao private
        self._avaliacao = []
        Restaurante.restaurantes.append(self) ##Adicionando restaurante a lista sempre que criar

    def __str__(self):  ##ToString
        """Retorna uma representação em string do restaurante."""
        return f"{self._nome} | {self._categoria}"

    @classmethod
    def listar_restaurantes(cls):
            """Exibe uma lista formatada de todos os restaurantes."""
            print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} |{"Status"}')
            for restaurante in cls.restaurantes:
                print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self):        ##Modificando o _ativo
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return "✅" if self._ativo else "❌"

    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if nota > 0 and nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao) 

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return "."
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) ##Faz a soma de todas notas de avaliação
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1) ##Round arredonda
        return media
