from Modelos.avaliacao import Avaliacao

class Restaurante:
  restaurantes = []
  def __init__(self, nome, categoria): ##Construtor / Self == This
      self._nome = nome.title()
      self._categoria = categoria
      self._ativo = False                   ##_ativo similar ao private
      self._avaliacao = []
      Restaurante.restaurantes.append(self) ##Adicionando restaurante a lista sempre que criar

  def __str__(self):  ##ToString
      return f"{self._nome} | {self._categoria}"

  @classmethod
  def listar_restaurante(cls):
      print(f'{"Nome do restaurante".ljust(25)} | {"Categoria do restaurante".ljust(25)} | {"Avaliação do restaurante".ljust(25)} | {"Status do restaurante"}')
    
      for restaurante in cls.restaurantes:
          print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.media_avaliacoes().ljust(25)}| {restaurante._ativo}")

  @property
  def ativo(self):        ##Modificando o _ativo
      return "✅" if self._ativo else "❌"

  def alternar_estado(self):
      self._ativo = not self._ativo

  def receber_avaliacao(self, cliente, nota):
      avaliacao = Avaliacao(cliente, nota)
      self._avaliacao.append(avaliacao) 

  @property
  def media_avaliacoes(self):
      if not self._avaliacao:
          return 0
      soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) ##Faz a soma de todas notas de avaliação
      quantidade_de_notas = len(self._avaliacao)
      media = round(soma_das_notas / quantidade_de_notas, 1) ##Round arredonda
      return media
