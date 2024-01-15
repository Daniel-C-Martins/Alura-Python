from Modelos.restaurantes import Restaurante
from Modelos.Cardapio.bebida import Bebida
from Modelos.Cardapio.prato import Prato

restaurante_praca = Restaurante("Praca", "Gourmet")

bebida_suco = Bebida("Suco de melancia", 5.0, "Grande")
prato_paozinho = Prato("Paozinho", 2.0, "O melhor pão da cidade")

bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)


def main():
    restaurante_praca.exibir_cardapio
    

if __name__ == "__main__":
    main()