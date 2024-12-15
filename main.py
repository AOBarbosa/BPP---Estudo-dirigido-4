from catalog import Catalog
from order import Order
from product import Product


if __name__ == "__main__":
    # Criando o catálogo
    catalogo = Catalog()

    # Adicionando produtos ao catálogo
    catalogo.add_products(Product(1, "Camiseta", 50.0))
    catalogo.add_products(Product(2, "Calça", 80.0))
    catalogo.add_products(Product(3, "Tênis", 150.0))

    # Listando produtos disponíveis
    print("Catálogo de Produtos:")
    for produto in catalogo.list_products():
        print(produto)

    # Buscando um produto pelo ID
    produto_buscado = catalogo.find_product_by_id(2)
    if produto_buscado:
        print("\nProduto encontrado:", produto_buscado)
    else:
        print("\nProduto não encontrado.")

    # Criando um pedido
    pedido = Order("João Silva")
    pedido.add_product(catalogo.find_product_by_id(1))  # Camiseta
    pedido.add_product(catalogo.find_product_by_id(2))  # Calça

    # Exibindo detalhes do pedido
    print("\nDetalhes do Pedido:")
    print(pedido)
