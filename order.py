import logging

from product import Product


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


class Order:
    def __init__(self, client: str):
        self.client = client
        self.products = []
        logger.info(f"Pedido criado para o cliente: {client}")

    def add_product(self, product: Product):
        self.products.append(product)
        logger.info(f"Produto adicionado ao pedido: {product}")


    def calculate_total(self):
        total = sum(product.price for product in self.products)
        if total > 100:
            logger.info("Desconto aplicado de 10% no pedido.")
            total *= 0.9
        return total

    def __repr__(self):
        listed_porducts = "\n".join([str(product) for product in self.products])
        return (
            f"Pedido do client '{self.client}':\n"
            f"Products:\n{listed_porducts}\n"
            f"Total: R${self.calculate_total():.2f}"
        )