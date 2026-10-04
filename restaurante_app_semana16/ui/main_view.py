import os
import tkinter as tk
from tkinter import ttk, messagebox


class MainView:

    def __init__(
        self,
        root,
        servicio,
        usuario_actual,
        cerrar_sesion
    ):

        self.root = root
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.cerrar_sesion = cerrar_sesion

        self.usuario_seleccionado_id = None
        self.logo = None

        self.configurar_ventana()
        self.crear_interfaz()

    # =====================================================
    # CONFIGURACIÓN DE LA VENTANA
    # =====================================================

    def configurar_ventana(self):

        self.root.title("Restaurante App")

        self.root.geometry(
            "1150x720"
        )

        self.root.minsize(
            950,
            620
        )

        self.root.configure(
            background="#F5F5F5"
        )

        estilo = ttk.Style()

        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass

        # Notebook
        estilo.configure(
            "TNotebook",
            background="#F5F5F5",
            borderwidth=0
        )

        estilo.configure(
            "TNotebook.Tab",
            padding=(18, 10),
            font=("Arial", 10, "bold")
        )

        # Botones
        estilo.configure(
            "TButton",
            padding=(12, 7),
            font=("Arial", 10, "bold")
        )

        # Etiquetas
        estilo.configure(
            "TLabel",
            font=("Arial", 10)
        )

        # Treeview
        estilo.configure(
            "Treeview",
            rowheight=30,
            font=("Arial", 10)
        )

        estilo.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

        # Combobox
        estilo.configure(
            "TCombobox",
            padding=5
        )

    # =====================================================
    # INTERFAZ PRINCIPAL
    # =====================================================

    def crear_interfaz(self):

        # -------------------------------------------------
        # ENCABEZADO
        # -------------------------------------------------

        encabezado = ttk.Frame(
            self.root,
            padding=(20, 15)
        )

        encabezado.pack(
            fill="x"
        )

        # Logo
        ruta_logo = os.path.join(
            "assets",
            "logo.png"
        )

        if os.path.exists(ruta_logo):

            try:

                self.logo = tk.PhotoImage(
                    file=ruta_logo
                )

                # Reducir el logo si es demasiado grande
                ancho = self.logo.width()
                alto = self.logo.height()

                if ancho > 100 or alto > 100:

                    factor = max(
                        1,
                        max(
                            ancho // 80,
                            alto // 80
                        )
                    )

                    self.logo = self.logo.subsample(
                        factor,
                        factor
                    )

                logo_label = ttk.Label(
                    encabezado,
                    image=self.logo
                )

                logo_label.pack(
                    side="left",
                    padx=(0, 15)
                )

            except tk.TclError:

                self.logo = None

        # Título
        titulo_frame = ttk.Frame(
            encabezado
        )

        titulo_frame.pack(
            side="left"
        )

        titulo = ttk.Label(
            titulo_frame,
            text="🍽️ RESTAURANTE APP",
            font=("Arial", 24, "bold")
        )

        titulo.pack(
            anchor="w"
        )

        subtitulo = ttk.Label(
            titulo_frame,
            text="Sistema de gestión del restaurante",
            font=("Arial", 10)
        )

        subtitulo.pack(
            anchor="w",
            pady=(3, 0)
        )

        # Información del usuario
        informacion_usuario = ttk.Label(
            encabezado,
            text=(
                f"Usuario: {self.usuario_actual.nombre}    "
                f"|    Rol: {self.usuario_actual.rol}"
            ),
            font=("Arial", 10, "bold")
        )

        informacion_usuario.pack(
            side="right"
        )

        # -------------------------------------------------
        # NOTEBOOK
        # -------------------------------------------------

        self.notebook = ttk.Notebook(
            self.root
        )

        self.notebook.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        # Productos
        self.crear_seccion_productos()

        # Ventas
        self.crear_seccion_ventas()

        # Usuarios
        if self.usuario_actual.rol == "Administrador":

            self.crear_seccion_usuarios()

        else:

            self.crear_seccion_usuarios_sin_acceso()

        # -------------------------------------------------
        # CERRAR SESIÓN
        # -------------------------------------------------

        ttk.Button(
            self.root,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        ).pack(
            pady=10
        )

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def crear_seccion_productos(self):

        frame = ttk.Frame(
            self.notebook,
            padding=20
        )

        self.notebook.add(
            frame,
            text="🍽 Productos"
        )

        titulo = ttk.Label(
            frame,
            text="Productos del restaurante",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=10
        )

        # -------------------------------------------------
        # FORMULARIO
        # -------------------------------------------------

        formulario = ttk.LabelFrame(
            frame,
            text="Registrar producto",
            padding=15
        )

        formulario.pack(
            fill="x",
            pady=10
        )

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.producto_nombre = ttk.Entry(
            formulario,
            width=25
        )

        self.producto_nombre.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Categoría:"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        self.producto_categoria = ttk.Entry(
            formulario,
            width=20
        )

        self.producto_categoria.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=0,
            column=4,
            padx=5,
            pady=5
        )

        self.producto_precio = ttk.Entry(
            formulario,
            width=12
        )

        self.producto_precio.grid(
            row=0,
            column=5,
            padx=5,
            pady=5
        )

        ttk.Button(
            formulario,
            text="Registrar",
            command=self.registrar_producto
        ).grid(
            row=0,
            column=6,
            padx=10
        )

        # -------------------------------------------------
        # TREEVIEW
        # -------------------------------------------------

        tabla = ttk.Frame(
            frame
        )

        tabla.pack(
            fill="both",
            expand=True,
            pady=15
        )

        self.tree_productos = ttk.Treeview(
            tabla,
            columns=(
                "id",
                "nombre",
                "categoria",
                "precio"
            ),
            show="headings"
        )

        self.tree_productos.heading(
            "id",
            text="ID"
        )

        self.tree_productos.heading(
            "nombre",
            text="Producto"
        )

        self.tree_productos.heading(
            "categoria",
            text="Categoría"
        )

        self.tree_productos.heading(
            "precio",
            text="Precio"
        )

        self.tree_productos.column(
            "id",
            width=60,
            anchor="center"
        )

        self.tree_productos.column(
            "nombre",
            width=280
        )

        self.tree_productos.column(
            "categoria",
            width=200
        )

        self.tree_productos.column(
            "precio",
            width=100,
            anchor="center"
        )

        self.tree_productos.pack(
            fill="both",
            expand=True
        )

        self.cargar_productos()

    def cargar_productos(self):

        for item in self.tree_productos.get_children():

            self.tree_productos.delete(
                item
            )

        productos = self.servicio.obtener_productos()

        for producto in productos:

            self.tree_productos.insert(
                "",
                "end",
                values=(
                    producto.id_producto,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}"
                )
            )

    def registrar_producto(self):

        correcto, mensaje = self.servicio.registrar_producto(
            self.producto_nombre.get(),
            self.producto_categoria.get(),
            self.producto_precio.get()
        )

        if correcto:

            messagebox.showinfo(
                "Productos",
                mensaje
            )

            self.producto_nombre.delete(
                0,
                tk.END
            )

            self.producto_categoria.delete(
                0,
                tk.END
            )

            self.producto_precio.delete(
                0,
                tk.END
            )

            self.cargar_productos()

        else:

            messagebox.showwarning(
                "Productos",
                mensaje
            )

    # =====================================================
    # VENTAS
    # =====================================================

    def crear_seccion_ventas(self):

        frame = ttk.Frame(
            self.notebook,
            padding=20
        )

        self.notebook.add(
            frame,
            text="🧾 Ventas"
        )

        titulo = ttk.Label(
            frame,
            text="Registro de ventas",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=10
        )

        # -------------------------------------------------
        # FORMULARIO
        # -------------------------------------------------

        formulario = ttk.LabelFrame(
            frame,
            text="Nueva venta",
            padding=15
        )

        formulario.pack(
            fill="x",
            pady=10
        )

        ttk.Label(
            formulario,
            text="Cliente:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.venta_cliente = ttk.Entry(
            formulario,
            width=20
        )

        self.venta_cliente.grid(
            row=0,
            column=1,
            padx=5
        )

        ttk.Label(
            formulario,
            text="Producto:"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        self.venta_producto = ttk.Entry(
            formulario,
            width=20
        )

        self.venta_producto.grid(
            row=0,
            column=3,
            padx=5
        )

        ttk.Label(
            formulario,
            text="Cantidad:"
        ).grid(
            row=0,
            column=4,
            padx=5,
            pady=5
        )

        self.venta_cantidad = ttk.Entry(
            formulario,
            width=10
        )

        self.venta_cantidad.grid(
            row=0,
            column=5,
            padx=5
        )

        ttk.Label(
            formulario,
            text="Total:"
        ).grid(
            row=0,
            column=6,
            padx=5,
            pady=5
        )

        self.venta_total = ttk.Entry(
            formulario,
            width=10
        )

        self.venta_total.grid(
            row=0,
            column=7,
            padx=5
        )

        ttk.Button(
            formulario,
            text="Registrar",
            command=self.registrar_venta
        ).grid(
            row=0,
            column=8,
            padx=10
        )

        # -------------------------------------------------
        # TREEVIEW
        # -------------------------------------------------

        tabla = ttk.Frame(
            frame
        )

        tabla.pack(
            fill="both",
            expand=True,
            pady=15
        )

        self.tree_ventas = ttk.Treeview(
            tabla,
            columns=(
                "id",
                "cliente",
                "producto",
                "cantidad",
                "total"
            ),
            show="headings"
        )

        columnas = {
            "id": "ID",
            "cliente": "Cliente",
            "producto": "Producto",
            "cantidad": "Cantidad",
            "total": "Total"
        }

        for columna, texto in columnas.items():

            self.tree_ventas.heading(
                columna,
                text=texto
            )

        self.tree_ventas.column(
            "id",
            width=60,
            anchor="center"
        )

        self.tree_ventas.column(
            "cliente",
            width=180
        )

        self.tree_ventas.column(
            "producto",
            width=250
        )

        self.tree_ventas.column(
            "cantidad",
            width=100,
            anchor="center"
        )

        self.tree_ventas.column(
            "total",
            width=100,
            anchor="center"
        )

        self.tree_ventas.pack(
            fill="both",
            expand=True
        )

        self.cargar_ventas()

    def cargar_ventas(self):

        for item in self.tree_ventas.get_children():

            self.tree_ventas.delete(
                item
            )

        ventas = self.servicio.obtener_ventas()

        for venta in ventas:

            self.tree_ventas.insert(
                "",
                "end",
                values=(
                    venta.id_venta,
                    venta.cliente,
                    venta.producto,
                    venta.cantidad,
                    f"${venta.total:.2f}"
                )
            )

    def registrar_venta(self):

        correcto, mensaje = self.servicio.registrar_venta(
            self.venta_cliente.get(),
            self.venta_producto.get(),
            self.venta_cantidad.get(),
            self.venta_total.get()
        )

        if correcto:

            messagebox.showinfo(
                "Ventas",
                mensaje
            )

            self.venta_cliente.delete(
                0,
                tk.END
            )

            self.venta_producto.delete(
                0,
                tk.END
            )

            self.venta_cantidad.delete(
                0,
                tk.END
            )

            self.venta_total.delete(
                0,
                tk.END
            )

            self.cargar_ventas()

        else:

            messagebox.showwarning(
                "Ventas",
                mensaje
            )

    # =====================================================
    # USUARIOS SIN ACCESO ADMINISTRATIVO
    # =====================================================

    def crear_seccion_usuarios_sin_acceso(self):

        frame = ttk.Frame(
            self.notebook,
            padding=30
        )

        self.notebook.add(
            frame,
            text="👥 Usuarios"
        )

        ttk.Label(
            frame,
            text="Gestión de usuarios",
            font=("Arial", 18, "bold")
        ).pack(
            pady=30
        )

        ttk.Label(
            frame,
            text=(
                "La gestión administrativa de usuarios "
                "está disponible únicamente para el Administrador."
            ),
            font=("Arial", 11)
        ).pack(
            pady=10
        )

    # =====================================================
    # USUARIOS - ADMINISTRADOR
    # =====================================================

    def crear_seccion_usuarios(self):

        frame = ttk.Frame(
            self.notebook,
            padding=15
        )

        self.notebook.add(
            frame,
            text="👥 Usuarios"
        )

        titulo = ttk.Label(
            frame,
            text="Gestión de usuarios",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=10
        )

        # -------------------------------------------------
        # FORMULARIO
        # -------------------------------------------------

        formulario = ttk.LabelFrame(
            frame,
            text="Información del usuario",
            padding=15
        )

        formulario.pack(
            fill="x",
            pady=5
        )

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.usuario_nombre = ttk.Entry(
            formulario,
            width=25
        )

        self.usuario_nombre.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        self.usuario_usuario = ttk.Entry(
            formulario,
            width=20
        )

        self.usuario_usuario.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Contraseña:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.usuario_password = ttk.Entry(
            formulario,
            width=25,
            show="*"
        )

        self.usuario_password.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Rol:"
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=5
        )

        self.usuario_rol = ttk.Combobox(
            formulario,
            values=[
                "Administrador",
                "Empleado",
                "Cliente"
            ],
            state="readonly",
            width=18
        )

        self.usuario_rol.grid(
            row=1,
            column=3,
            padx=5,
            pady=5
        )

        # =================================================
        # EVENTO COMBOBOX
        # =================================================

        self.usuario_rol.bind(
            "<<ComboboxSelected>>",
            self.cambio_de_rol
        )

        # -------------------------------------------------
        # BOTONES
        # -------------------------------------------------

        botones = ttk.Frame(
            frame
        )

        botones.pack(
            pady=10
        )

        ttk.Button(
            botones,
            text="Registrar",
            command=self.registrar_usuario
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        ttk.Button(
            botones,
            text="Actualizar",
            command=self.actualizar_usuario
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        ttk.Button(
            botones,
            text="Eliminar",
            command=self.eliminar_usuario
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        ttk.Button(
            botones,
            text="Limpiar",
            command=self.limpiar_usuario
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        # -------------------------------------------------
        # TREEVIEW
        # -------------------------------------------------

        tabla = ttk.Frame(
            frame
        )

        tabla.pack(
            fill="both",
            expand=True,
            pady=10
        )

        self.tree_usuarios = ttk.Treeview(
            tabla,
            columns=(
                "id",
                "nombre",
                "usuario",
                "rol"
            ),
            show="headings"
        )

        self.tree_usuarios.heading(
            "id",
            text="ID"
        )

        self.tree_usuarios.heading(
            "nombre",
            text="Nombre"
        )

        self.tree_usuarios.heading(
            "usuario",
            text="Usuario"
        )

        self.tree_usuarios.heading(
            "rol",
            text="Rol"
        )

        self.tree_usuarios.column(
            "id",
            width=60,
            anchor="center"
        )

        self.tree_usuarios.column(
            "nombre",
            width=250
        )

        self.tree_usuarios.column(
            "usuario",
            width=180
        )

        self.tree_usuarios.column(
            "rol",
            width=150,
            anchor="center"
        )

        self.tree_usuarios.pack(
            fill="both",
            expand=True
        )

        # =================================================
        # EVENTO TREEVIEW
        # =================================================

        self.tree_usuarios.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_usuario
        )

        # =================================================
        # EVENTOS DE TECLADO
        # =================================================

        self.root.bind(
            "<Return>",
            self.registrar_con_enter
        )

        self.root.bind(
            "<Escape>",
            self.limpiar_con_escape
        )

        self.cargar_usuarios()

    # =====================================================
    # CARGAR USUARIOS
    # =====================================================

    def cargar_usuarios(self):

        for item in self.tree_usuarios.get_children():

            self.tree_usuarios.delete(
                item
            )

        usuarios = self.servicio.obtener_usuarios()

        for usuario in usuarios:

            self.tree_usuarios.insert(
                "",
                "end",
                values=(
                    usuario.id_usuario,
                    usuario.nombre,
                    usuario.usuario,
                    usuario.rol
                )
            )

    # =====================================================
    # EVENTO <<TreeviewSelect>>
    # =====================================================

    def seleccionar_usuario(self, event):

        seleccion = self.tree_usuarios.selection()

        if not seleccion:
            return

        valores = self.tree_usuarios.item(
            seleccion[0],
            "values"
        )

        if not valores:
            return

        id_usuario = valores[0]

        usuario = self.servicio.buscar_usuario_por_id(
            id_usuario
        )

        if usuario is None:
            return

        self.usuario_seleccionado_id = (
            usuario.id_usuario
        )

        # Nombre
        self.usuario_nombre.delete(
            0,
            tk.END
        )

        self.usuario_nombre.insert(
            0,
            usuario.nombre
        )

        # Usuario
        self.usuario_usuario.delete(
            0,
            tk.END
        )

        self.usuario_usuario.insert(
            0,
            usuario.usuario
        )

        # Contraseña
        self.usuario_password.delete(
            0,
            tk.END
        )

        # Rol
        self.usuario_rol.set(
            usuario.rol
        )

    # =====================================================
    # EVENTO <<ComboboxSelected>>
    # =====================================================

    def cambio_de_rol(self, event):

        rol = self.usuario_rol.get()

        # Se utiliza para evidenciar el evento.
        # No se coloca lógica de negocio aquí.
        print(
            f"Rol seleccionado: {rol}"
        )

    # =====================================================
    # EVENTO <Return>
    # =====================================================

    def registrar_con_enter(self, event):

        # Reutilizamos el método existente.
        self.registrar_usuario()

    # =====================================================
    # EVENTO <Escape>
    # =====================================================

    def limpiar_con_escape(self, event):

        # Reutilizamos el método existente.
        self.limpiar_usuario()

    # =====================================================
    # REGISTRAR USUARIO
    # =====================================================

    def registrar_usuario(self):

        correcto, mensaje = self.servicio.registrar_usuario(
            self.usuario_nombre.get(),
            self.usuario_usuario.get(),
            self.usuario_password.get(),
            self.usuario_rol.get()
        )

        if correcto:

            messagebox.showinfo(
                "Usuarios",
                mensaje
            )

            self.cargar_usuarios()

            self.limpiar_usuario()

        else:

            messagebox.showwarning(
                "Usuarios",
                mensaje
            )

    # =====================================================
    # ACTUALIZAR USUARIO
    # =====================================================

    def actualizar_usuario(self):

        if self.usuario_seleccionado_id is None:

            messagebox.showwarning(
                "Usuarios",
                "Seleccione un usuario para actualizar."
            )

            return

        correcto, mensaje = self.servicio.actualizar_usuario(
            self.usuario_seleccionado_id,
            self.usuario_nombre.get(),
            self.usuario_usuario.get(),
            self.usuario_password.get(),
            self.usuario_rol.get()
        )

        if correcto:

            messagebox.showinfo(
                "Usuarios",
                mensaje
            )

            self.cargar_usuarios()

            self.limpiar_usuario()

        else:

            messagebox.showwarning(
                "Usuarios",
                mensaje
            )

    # =====================================================
    # ELIMINAR USUARIO
    # =====================================================

    def eliminar_usuario(self):

        if self.usuario_seleccionado_id is None:

            messagebox.showwarning(
                "Usuarios",
                "Seleccione un usuario para eliminar."
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Está seguro de eliminar este usuario?"
        )

        if not confirmar:
            return

        correcto, mensaje = self.servicio.eliminar_usuario(
            self.usuario_seleccionado_id,
            self.usuario_actual.id_usuario
        )

        if correcto:

            messagebox.showinfo(
                "Usuarios",
                mensaje
            )

            self.cargar_usuarios()

            self.limpiar_usuario()

        else:

            messagebox.showwarning(
                "Usuarios",
                mensaje
            )

    # =====================================================
    # LIMPIAR FORMULARIO
    # =====================================================

    def limpiar_usuario(self):

        self.usuario_seleccionado_id = None

        self.usuario_nombre.delete(
            0,
            tk.END
        )

        self.usuario_usuario.delete(
            0,
            tk.END
        )

        self.usuario_password.delete(
            0,
            tk.END
        )

        self.usuario_rol.set(
            ""
        )

        seleccion = self.tree_usuarios.selection()

        if seleccion:

            self.tree_usuarios.selection_remove(
                seleccion
            )