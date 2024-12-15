import logging

from product import Product


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

class Catalog:
    def __init__(self):
        self.products = []

    def add_products(self, product: Product):
        self.products.append(product)
        logger.info(f"Produto adicionado ao catálogo: {product}")

    def list_products(self):
        return self.products

    def find_product_by_id(self, id: int):
        for product in self.products:
            if product.id == id:
                return product
        return None