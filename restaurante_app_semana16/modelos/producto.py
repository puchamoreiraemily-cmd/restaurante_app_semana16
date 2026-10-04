class Producto:
    def __init__(self, id_producto, nombre, categoria, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def to_dict(self):
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            data["id"],
            data["nombre"],
            data["categoria"],
            data["precio"]
        )