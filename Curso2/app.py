from Modelos.restaurantes import Restaurante

restaurante_praca = Restaurante("Praca", "Gourmet")
# restaurante_mexicano = Restaurante("Mexican food", "Mexicano")
# restaurante_pizza = Restaurante("Japa", "Japonês")

restaurante_praca.receber_avaliacao("Gui", 10)
restaurante_praca.receber_avaliacao("Giovanan", 8)
restaurante_praca.receber_avaliacao("Carlos", 5)

def main():
    Restaurante.listar_restaurante()

if __name__ == "__main__":
    main()