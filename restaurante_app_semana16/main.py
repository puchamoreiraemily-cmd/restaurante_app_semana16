import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class Aplicacion:

    def __init__(self):

        self.servicio = RestauranteServicio()

        self.root = tk.Tk()

        self.mostrar_login()

        self.root.mainloop()

    def mostrar_login(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        LoginView(
            self.root,
            self.servicio,
            self.mostrar_principal
        )

    def mostrar_principal(self, usuario):

        ventana = tk.Toplevel(
            self.root
        )

        MainView(
            ventana,
            self.servicio,
            usuario,
            lambda: self.cerrar_sesion(ventana)
        )

    def cerrar_sesion(self, ventana):

        ventana.destroy()

        self.root.deiconify()

        self.mostrar_login()


if __name__ == "__main__":
    Aplicacion()