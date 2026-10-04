# 🍽️ Restaurante App

Sistema de gestión para un restaurante desarrollado en Python utilizando Tkinter.

El proyecto permite administrar usuarios, productos y ventas mediante una interfaz gráfica, manteniendo la información persistida en archivos JSON.

## 📚 Semana 16 - Manejo de eventos en Tkinter

En esta semana se evolucionó el proyecto para incorporar la gestión de usuarios mediante una interfaz gráfica con formulario y tabla `Treeview`.

Se mantuvo la arquitectura modular del proyecto y se agregaron eventos de Tkinter para mejorar la interacción con el usuario.

## 🎯 Objetivo

Implementar el manejo de eventos en Tkinter dentro de un sistema de gestión de restaurante, utilizando:

- `bind()`
- `command=`
- Callbacks
- `Treeview`
- `<<TreeviewSelect>>`
- `<Return>`
- `<Escape>`
- `<<ComboboxSelected>>`

## 🏗️ Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── assets/
│   └── logo.png
│
├── main.py
└── README.md







👥 Gestión de usuarios

La aplicación permite al administrador:

Registrar usuarios.
Consultar usuarios.
Actualizar usuarios.
Eliminar usuarios.
Limpiar el formulario.
Seleccionar usuarios desde un Treeview.

Cada usuario posee:

Identificador.
Nombre.
Nombre de usuario.
Contraseña.
Rol.
🔐 Roles

El sistema utiliza tres roles:

Administrador
Empleado
Cliente

La gestión administrativa de usuarios está disponible únicamente para el usuario con rol Administrador.

El administrador puede gestionar usuarios de tipo Empleado y Cliente.

La cuenta actualmente utilizada para iniciar sesión no puede eliminarse desde la gestión de usuarios.

📋 Treeview de usuarios

Los usuarios se muestran mediante un Treeview.

La tabla muestra únicamente información necesaria para identificar cada registro:

ID
Nombre
Usuario
Rol

La contraseña no se muestra en la tabla.

Al seleccionar una fila se ejecuta el evento:

<<TreeviewSelect>>

mediante bind().

El callback obtiene el identificador seleccionado y consulta el usuario mediante RestauranteServicio.

Después, los datos se cargan automáticamente en el formulario.

⌨️ Eventos implementados
<<TreeviewSelect>>

Permite detectar la selección de una fila del Treeview.

self.tree_usuarios.bind(
    "<<TreeviewSelect>>",
    self.seleccionar_usuario
)

El evento permite cargar los datos del usuario seleccionado en el formulario.

<Return>

Se utiliza como atajo de teclado para registrar un usuario.

self.root.bind(
    "<Return>",
    self.registrar_con_enter
)

El callback reutiliza el método:

self.registrar_usuario()

De esta manera no se duplica la lógica de registro.

<Escape>

Permite limpiar el formulario y cancelar la selección actual.

self.root.bind(
    "<Escape>",
    self.limpiar_con_escape
)

El callback reutiliza:

self.limpiar_usuario()
<<ComboboxSelected>>

Se utiliza para detectar cuando el usuario cambia el rol seleccionado.

self.usuario_rol.bind(
    "<<ComboboxSelected>>",
    self.cambio_de_rol
)

El evento permite responder al cambio del rol seleccionado.

🔘 Uso de command=

Los botones principales utilizan command=.

Por ejemplo:

ttk.Button(
    botones,
    text="Registrar",
    command=self.registrar_usuario
)

También se utiliza para:

Registrar.
Actualizar.
Eliminar.
Limpiar.
Cerrar sesión.

La diferencia principal es que command= se utiliza directamente para ejecutar una función desde un botón, mientras que bind() permite asociar callbacks a diferentes eventos, como teclas o eventos de widgets.

🧠 Callbacks

Los callbacks reciben y procesan las interacciones generadas por los eventos.

Por ejemplo:

def registrar_con_enter(self, event):

    self.registrar_usuario()

El callback no contiene nuevamente toda la lógica del registro. En su lugar, reutiliza el método existente.

Esto permite mantener el código organizado y evitar duplicación.

🏢 Separación de responsabilidades

La aplicación mantiene una arquitectura modular.

Modelos

Representan los datos del sistema:

Usuario
Producto
Venta
Servicios

RestauranteServicio contiene las operaciones y validaciones relacionadas con los datos.

También administra la persistencia mediante archivos JSON.

Interfaz

Los archivos dentro de ui/ se encargan de mostrar la información y recibir las interacciones del usuario.

La interfaz no realiza directamente la lectura o escritura de los archivos JSON.

Datos

La información se almacena en:

datos/usuarios.json
datos/productos.json
datos/ventas.json
💾 Persistencia

Los usuarios registrados se guardan en:

datos/usuarios.json

La información se recupera nuevamente al iniciar la aplicación.

Esto permite conservar los registros aunque la aplicación sea cerrada.

🔄 Flujo de gestión de usuarios
Administrador
      ↓
Sección Usuarios
      ↓
Formulario + Treeview
      ↓
Seleccionar usuario
      ↓
<<TreeviewSelect>>
      ↓
bind()
      ↓
Callback
      ↓
RestauranteServicio
      ↓
Consulta del usuario
      ↓
Carga en formulario
      ↓
Actualizar / Eliminar / Limpiar
      ↓
usuarios.json
      ↓
Actualización del Treeview
🖥️ Interfaz

La aplicación utiliza Tkinter y ttk para construir la interfaz gráfica.

Se incorporó la carpeta:

assets/

para almacenar recursos visuales del sistema, como el logotipo.

La interfaz busca mantener una distribución clara de formularios, botones y tablas.

▶️ Instalación y ejecución

Se necesita tener instalado Python 3.

No se requieren librerías externas para ejecutar la aplicación, ya que se utilizan módulos incluidos en Python como:

tkinter
json
os

Para ejecutar el sistema:

python main.py
🔑 Usuario administrador inicial

La aplicación crea automáticamente un usuario administrador inicial si todavía no existe el archivo usuarios.json.

Usuario: admin
Contraseña: 1234
Rol: Administrador

Se recomienda cambiar estos datos si el sistema se utiliza fuera del entorno académico.

🧪 Comprobaciones realizadas

Se verificó el funcionamiento de:

Inicio de sesión.
Acceso a la ventana principal.
Gestión de productos.
Gestión de ventas.
Gestión de usuarios.
Registro de usuarios.
Consulta mediante Treeview.
Actualización de usuarios.
Eliminación de usuarios.
Confirmación antes de eliminar.
Protección de la cuenta actualmente autenticada.
Evento <<TreeviewSelect>>.
Evento <Return>.
Evento <Escape>.
Evento <<ComboboxSelected>>.
Persistencia mediante archivos JSON.
Control básico de acceso según el rol.
👩‍💻 Proyecto académico

Proyecto desarrollado para la asignatura de Programación Orientada a Objetos.

Semana 16 - Manejo de eventos en Tkinter.


---

# PASO 7 — Revisa la estructura

Ahora tu proyecto debería verse así:

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── assets/
│   └── logo.png
│
├── main.py
└── README.md
 Importante

No necesitas crear archivos adicionales que no estén en tu proyecto.