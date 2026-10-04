class Usuario:
    def __init__(self, id_usuario, nombre, usuario, password, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.usuario = usuario
        self.password = password
        self.rol = rol

    def to_dict(self):
        return {
            "id": self.id_usuario,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "password": self.password,
            "rol": self.rol
        }

    @staticmethod
    def from_dict(data):
        return Usuario(
            data["id"],
            data["nombre"],
            data["usuario"],
            data["password"],
            data["rol"]
        )