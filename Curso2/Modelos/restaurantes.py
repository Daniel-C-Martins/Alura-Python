class Restaurante:
  restaurantes = []
  def __init__(self, nome, categoria): ##Construtor / Self == This
    self._nome = nome.title()
    self.categoria = categoria
    self._ativo = False                   ##_ativo similar ao private
    Restaurante.restaurantes.append(self) ##Adicionando restaurante a lista sempre que criar

  def __str__(self):  ##ToString
    return f"{self.nome} | {self.categoria}"

  @classmethod
  def listar_restaurante(cls):
    print(f'{"Nome do restaurante".ljust(25)} | {"Categoria do restaurante".ljust(25)} | {"Status do restaurante"}')
    
    for restaurante in cls.restaurantes:
      print(f"{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}")

  @property
  def ativo(self):        ##Modificando o _ativo
    return "✅" if self._ativo else "❌"

  def alternar_estado(self):
    self._ativo = not self._ativo

restaurante_praca = Restaurante("Praca", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiana")

Restaurante.listar_restaurante()
restaurante_praca.alternar_estado()
Restaurante.listar_restaurante()
## print(dir(restaurante_praca)) mostra tudo sobre a classe