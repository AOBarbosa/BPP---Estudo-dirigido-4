import unittest

from catalog import Catalog
from order import Order
from product import Product


class TestSistema(unittest.TestCase):

    def test_adicionar_e_buscar_produto_catalogo(self):
        catalogo = Catalog()
        produto = Product(1, "Camiseta", 50.0)
        catalogo.add_products(produto)

        self.assertIn(produto, catalogo.list_products())
        self.assertEqual(catalogo.find_product_by_id(1), produto)
        self.assertIsNone(catalogo.find_product_by_id(2))

    def test_calculo_total_sem_desconto(self):
        pedido = Order("Cliente A")
        pedido.add_product(Product(1, "Camiseta", 50.0))
        pedido.add_product(Product(2, "Calça", 30.0))

        self.assertEqual(pedido.calculate_total(), 80.0)

    def test_calculo_total_com_desconto(self):
        pedido = Order("Cliente B")
        pedido.add_product(Product(1, "Tênis", 150.0))

        self.assertEqual(pedido.calculate_total(), 135.0)  # 10% de desconto

    def test_cenario_integracao(self):
        catalogo = Catalog()
        catalogo.add_products(Product(1, "Camiseta", 50.0))
        catalogo.add_products(Product(2, "Calça", 80.0))

        pedido = Order("Cliente C")
        pedido.add_product(catalogo.find_product_by_id(1))
        pedido.add_product(catalogo.find_product_by_id(2))

        self.assertEqual(len(pedido.products), 2)
        self.assertEqual(pedido.calculate_total(), 117.0)  # Total com desconto


if __name__ == "__main__":
    # Executando os testes
    unittest.main()
