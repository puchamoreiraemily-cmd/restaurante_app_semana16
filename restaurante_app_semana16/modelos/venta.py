class Venta:
    def __init__(self, id_venta, cliente, producto, cantidad, total):
        self.id_venta = id_venta
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.total = total

    def to_dict(self):
        return {
            "id": self.id_venta,
            "cliente": self.cliente,
            "producto": self.producto,
            "cantidad": self.cantidad,
            "total": self.total
        }

    @staticmethod
    def from_dict(data):
        return Venta(
            data["id"],
            data["cliente"],
            data["producto"],
            data["cantidad"],
            data["total"]
        )