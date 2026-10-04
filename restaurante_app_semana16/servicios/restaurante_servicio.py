import os

from modelos.usuario import Usuario
from modelos.producto import Producto
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(self):
        self.ruta_usuarios = os.path.join(
            "datos",
            "usuarios.json"
        )

        self.ruta_productos = os.path.join(
            "datos",
            "productos.json"
        )

        self.ruta_ventas = os.path.join(
            "datos",
            "ventas.json"
        )

        self.crear_archivos_iniciales()

    # =====================================================
    # ARCHIVOS INICIALES
    # =====================================================

    def crear_archivos_iniciales(self):

        if not os.path.exists(self.ruta_usuarios):
            ArchivoServicio.guardar(
                self.ruta_usuarios,
                [
                    {
                        "id": 1,
                        "nombre": "Administrador General",
                        "usuario": "admin",
                        "password": "1234",
                        "rol": "Administrador"
                    }
                ]
            )

        if not os.path.exists(self.ruta_productos):
            ArchivoServicio.guardar(
                self.ruta_productos,
                []
            )

        if not os.path.exists(self.ruta_ventas):
            ArchivoServicio.guardar(
                self.ruta_ventas,
                []
            )

    # =====================================================
    # USUARIOS
    # =====================================================

    def obtener_usuarios(self):

        datos = ArchivoServicio.leer(
            self.ruta_usuarios
        )

        return [
            Usuario.from_dict(usuario)
            for usuario in datos
        ]

    def buscar_usuario_por_id(self, id_usuario):

        usuarios = self.obtener_usuarios()

        for usuario in usuarios:
            if str(usuario.id_usuario) == str(id_usuario):
                return usuario

        return None

    def buscar_usuario_login(self, usuario, password):

        usuarios = self.obtener_usuarios()

        for item in usuarios:

            if (
                item.usuario == usuario
                and item.password == password
            ):
                return item

        return None

    def registrar_usuario(
        self,
        nombre,
        usuario,
        password,
        rol
    ):

        nombre = nombre.strip()
        usuario = usuario.strip()
        password = password.strip()

        if not nombre:
            return False, "Ingrese el nombre del usuario."

        if not usuario:
            return False, "Ingrese el nombre de usuario."

        if not password:
            return False, "Ingrese una contraseña."

        if rol not in [
            "Administrador",
            "Empleado",
            "Cliente"
        ]:
            return False, "Seleccione un rol."

        usuarios = self.obtener_usuarios()

        for item in usuarios:

            if item.usuario.lower() == usuario.lower():
                return False, "El usuario ya existe."

        nuevo_id = 1

        if usuarios:
            nuevo_id = max(
                int(item.id_usuario)
                for item in usuarios
            ) + 1

        nuevo_usuario = Usuario(
            nuevo_id,
            nombre,
            usuario,
            password,
            rol
        )

        usuarios.append(nuevo_usuario)

        ArchivoServicio.guardar(
            self.ruta_usuarios,
            [
                item.to_dict()
                for item in usuarios
            ]
        )

        return True, "Usuario registrado correctamente."

    def actualizar_usuario(
        self,
        id_usuario,
        nombre,
        usuario,
        password,
        rol
    ):

        nombre = nombre.strip()
        usuario = usuario.strip()
        password = password.strip()

        if not nombre:
            return False, "Ingrese el nombre."

        if not usuario:
            return False, "Ingrese el usuario."

        if rol not in [
            "Administrador",
            "Empleado",
            "Cliente"
        ]:
            return False, "Seleccione un rol."

        usuarios = self.obtener_usuarios()

        usuario_encontrado = None

        for item in usuarios:

            if str(item.id_usuario) == str(id_usuario):
                usuario_encontrado = item
                break

        if usuario_encontrado is None:
            return False, "Usuario no encontrado."

        for item in usuarios:

            if (
                str(item.id_usuario) != str(id_usuario)
                and item.usuario.lower() == usuario.lower()
            ):
                return False, "El usuario ya existe."

        usuario_encontrado.nombre = nombre
        usuario_encontrado.usuario = usuario
        usuario_encontrado.rol = rol

        if password:
            usuario_encontrado.password = password

        ArchivoServicio.guardar(
            self.ruta_usuarios,
            [
                item.to_dict()
                for item in usuarios
            ]
        )

        return True, "Usuario actualizado correctamente."

    def eliminar_usuario(
        self,
        id_usuario,
        usuario_actual_id
    ):

        if str(id_usuario) == str(usuario_actual_id):
            return False, (
                "No puede eliminar la cuenta "
                "con la que inició sesión."
            )

        usuarios = self.obtener_usuarios()

        usuario = self.buscar_usuario_por_id(
            id_usuario
        )

        if usuario is None:
            return False, "Usuario no encontrado."

        usuarios = [
            item
            for item in usuarios
            if str(item.id_usuario) != str(id_usuario)
        ]

        ArchivoServicio.guardar(
            self.ruta_usuarios,
            [
                item.to_dict()
                for item in usuarios
            ]
        )

        return True, "Usuario eliminado correctamente."

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def obtener_productos(self):

        datos = ArchivoServicio.leer(
            self.ruta_productos
        )

        return [
            Producto.from_dict(producto)
            for producto in datos
        ]

    def registrar_producto(
        self,
        nombre,
        categoria,
        precio
    ):

        nombre = nombre.strip()
        categoria = categoria.strip()

        if not nombre:
            return False, "Ingrese el nombre del producto."

        if not categoria:
            return False, "Ingrese la categoría."

        try:
            precio = float(precio)

            if precio <= 0:
                return False, "El precio debe ser mayor a cero."

        except ValueError:
            return False, "Ingrese un precio válido."

        productos = self.obtener_productos()

        nuevo_id = 1

        if productos:
            nuevo_id = max(
                int(item.id_producto)
                for item in productos
            ) + 1

        producto = Producto(
            nuevo_id,
            nombre,
            categoria,
            precio
        )

        productos.append(producto)

        ArchivoServicio.guardar(
            self.ruta_productos,
            [
                item.to_dict()
                for item in productos
            ]
        )

        return True, "Producto registrado correctamente."

    # =====================================================
    # VENTAS
    # =====================================================

    def obtener_ventas(self):

        datos = ArchivoServicio.leer(
            self.ruta_ventas
        )

        return [
            Venta.from_dict(venta)
            for venta in datos
        ]

    def registrar_venta(
        self,
        cliente,
        producto,
        cantidad,
        total
    ):

        cliente = cliente.strip()
        producto = producto.strip()

        if not cliente:
            return False, "Ingrese el cliente."

        if not producto:
            return False, "Ingrese el producto."

        try:
            cantidad = int(cantidad)

            if cantidad <= 0:
                return False, "La cantidad debe ser mayor a cero."

            total = float(total)

        except ValueError:
            return False, "Ingrese datos numéricos válidos."

        ventas = self.obtener_ventas()

        nuevo_id = 1

        if ventas:
            nuevo_id = max(
                int(item.id_venta)
                for item in ventas
            ) + 1

        venta = Venta(
            nuevo_id,
            cliente,
            producto,
            cantidad,
            total
        )

        ventas.append(venta)

        ArchivoServicio.guardar(
            self.ruta_ventas,
            [
                item.to_dict()
                for item in ventas
            ]
        )

        return True, "Venta registrada correctamente."