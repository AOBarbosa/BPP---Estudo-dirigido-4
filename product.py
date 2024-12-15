class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Produto(ID: {self.id}, Name: '{self.name}', Price: R${self.price:.2f})"