import tkinter as tk
from tkinter import ttk, messagebox


class LoginView:

    def __init__(self, root, servicio, abrir_principal):

        self.root = root
        self.servicio = servicio
        self.abrir_principal = abrir_principal

        self.root.title(
            "Sabor & Arte - Inicio de sesión"
        )

        self.root.geometry("450x380")
        self.root.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):

        contenedor = ttk.Frame(
            self.root,
            padding=30
        )

        contenedor.pack(
            fill="both",
            expand=True
        )

        titulo = ttk.Label(
            contenedor,
            text="SABOR & ARTE",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=(20, 5))

        subtitulo = ttk.Label(
            contenedor,
            text="Sistema de gestión del restaurante"
        )

        subtitulo.pack(pady=(0, 25))

        ttk.Label(
            contenedor,
            text="Usuario"
        ).pack(anchor="w")

        self.entry_usuario = ttk.Entry(
            contenedor,
            width=35
        )

        self.entry_usuario.pack(
            fill="x",
            pady=(5, 15)
        )

        ttk.Label(
            contenedor,
            text="Contraseña"
        ).pack(anchor="w")

        self.entry_password = ttk.Entry(
            contenedor,
            width=35,
            show="*"
        )

        self.entry_password.pack(
            fill="x",
            pady=(5, 20)
        )

        ttk.Button(
            contenedor,
            text="Iniciar sesión",
            command=self.iniciar_sesion
        ).pack(
            pady=10,
            ipadx=15
        )

        self.entry_password.bind(
            "<Return>",
            self.iniciar_con_enter
        )

        self.entry_usuario.focus()

    def iniciar_con_enter(self, event):

        self.iniciar_sesion()

    def iniciar_sesion(self):

        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()

        if not usuario or not password:

            messagebox.showwarning(
                "Inicio de sesión",
                "Complete todos los campos."
            )

            return

        usuario_encontrado = (
            self.servicio.buscar_usuario_login(
                usuario,
                password
            )
        )

        if usuario_encontrado is None:

            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )

            return

        self.root.withdraw()

        self.abrir_principal(
            usuario_encontrado
        )